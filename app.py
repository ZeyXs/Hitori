import pygame
import constants as utils

pygame.display.init()

cells = []
initList = False

grid = [[[2, -1], [2, -1], [1, -1], [5, -1], [3, -1]],
        [[2, -1], [3, -1], [1, -1], [4, -1], [5, -1]],
        [[1, -1], [1, -1], [1, -1], [3, -1], [5, -1]],
        [[1, -1], [3, -1], [5, -1], [4, -1], [2, -1]],
        [[5, -1], [4, -1], [3, -1], [2, -1], [1, -1]]]

def main():
    pygame.display.set_caption(utils.NAME)
    pygame.display.set_icon(utils.LOGO)
    screen = pygame.display.set_mode((utils.WIDTH, utils.HEIGHT))

    running = True
    while running:
        # Event Listener
        for event in pygame.event.get():
            left, middle, right = pygame.mouse.get_pressed()

            if event.type == pygame.QUIT:
                running = False

            pos = pygame.mouse.get_pos()
            if left or middle:
                for cell in cells:
                    if cell.collidepoint(pos):
                        x,y = convertGridCoord(cell)
                        if grid[y][x][1] == -1: #blank
                            grid[y][x][1] = 0
                        elif grid[y][x][1] == 0: #red
                            grid[y][x][1] = 1
                        elif grid[y][x][1] == 1: #green
                            grid[y][x][1] = -1
            if right:
                for cell in cells:
                    if cell.collidepoint(pos):
                        x,y = convertGridCoord(cell)
                        if grid[y][x][1] == -1: #blank
                            grid[y][x][1] = 1
                        elif grid[y][x][1] == 1: #green
                            grid[y][x][1] = -1

        # Draw Scene
        screen.fill((255, 253, 245))
        drawBoard(screen, 5, 5)
        drawTimer(screen, 5, 5)
            
        # Update    
        pygame.display.update()

def drawBoard(screen, x, y):
    margin = (50 + utils.MARGIN)
    global initList
    for row in range(x):
        for column in range(y):
            xRect = ((utils.WIDTH - margin - 25) // 4) + column * margin
            yRect = ((utils.HEIGHT - margin) // 4) + row * margin
            color = (255, 248, 230) # blank

            if grid[row][column][1] == 0: # red
                color = (255, 163, 163)
            elif grid[row][column][1] == 1: # green
                color = (193, 255, 179)

            rect = pygame.draw.rect(screen, color, (xRect, yRect, 50, 50), 0)
            pygame.draw.rect(screen, (235, 212, 152), (xRect, yRect, 50, 50), 6)

            text = utils.FONT.render(str(grid[row][column][0]), False, (0, 0, 0))
            text_rect = text.get_rect()
            text_rect.center = pygame.Rect(xRect+3, yRect-4, 50, 50).center
            screen.blit(text, text_rect)

            if initList == False:
                cells.append(rect)
    initList = True

def drawTimer(screen, x, y):
    screen.blit(utils.GUI_TIMER, (x,y))
    text = utils.FONT_TIMER.render("00:00", False, (0, 0, 0))
    text_rect = text.get_rect()
    text_rect.center = pygame.Rect(x+13, y-3, 120, 40).center
    screen.blit(text, text_rect)

def convertGridCoord(cell):
    x_cell = (cell[0] - 103) / 60
    y_cell = (cell[1] - 110) / 60
    return int(x_cell), int(y_cell)

if __name__ == "__main__":
    main()