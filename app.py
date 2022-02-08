import pygame
import constants as utils
import time

pygame.display.init()
clock = pygame.time.Clock()

time_elapsed = 0
timer = 0

cells = []
initButtons = False
buttons = []
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
                for button in buttons:
                    if button.collidepoint(pos):
                        print(button)
            if right:
                for cell in cells:
                    if cell.collidepoint(pos):
                        x,y = convertGridCoord(cell)
                        if grid[y][x][1] == -1: #blank
                            grid[y][x][1] = 1
                        elif grid[y][x][1] == 1: #green
                            grid[y][x][1] = -1
                        elif grid[y][x][1] == 0: #red
                            grid[y][x][1] = 1

        # Draw Scene
        screen.fill(utils.BACKGROUND_COLOR)
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
            color = utils.CELLS_COLOR # blank

            # DEBUG
            if grid[row][column][1] == 0: # red
                color = (255, 163, 163)
            elif grid[row][column][1] == 1: # green
                color = (193, 255, 179)

            rect = pygame.draw.rect(screen, color, (xRect, yRect, 50, 50), 0)
            pygame.draw.rect(screen, utils.BORDER_COLOR, (xRect, yRect, 50, 50), 6)

            text = utils.FONT.render(str(grid[row][column][0]), False, (0, 0, 0))
            text_rect = text.get_rect()
            text_rect.center = pygame.Rect(xRect+3, yRect-4, 50, 50).center
            screen.blit(text, text_rect)

            drawButton(screen)

            if initList == False:
                cells.append(rect)
    initList = True

def drawTimer(screen, x, y):
    global time_elapsed
    global timer
    tick = clock.tick()
    time_elapsed += tick
    if time_elapsed > 1000:
        timer += 1
        time_elapsed = 0

    texture = utils.GUI_TIMER
    texture = pygame.transform.scale(texture, (120, 48))
    screen.blit(texture, (x,y))

    text = utils.FONT_TIMER.render(convertTime(timer), False, (0, 0, 0))
    text_rect = text.get_rect()
    text_rect.center = pygame.Rect(x+18, y, 120, 40).center
    screen.blit(text, text_rect)

def drawButton(screen):
    global buttons
    global initButtons
    x = (utils.WIDTH / 2) - 27
    y = utils.HEIGHT - (utils.HEIGHT / 8) - 19

    pause = utils.PAUSE
    pause = pygame.transform.scale(pause, (50,50))
    pauseRect = pygame.Rect(x, y, 50, 50)
    screen.blit(pause, (x, y))

    restart = utils.RESTART
    restart = pygame.transform.scale(restart, (50,50))
    restartRect = pygame.Rect(x + 80, y, 50, 50)
    screen.blit(restart, (x + 80, y))

    check = utils.CHECK
    check = pygame.transform.scale(check, (50,50))
    checkRect = pygame.Rect(x - 80, y, 50, 50)
    screen.blit(check, (x - 80, y))

    if initButtons == False:
        buttons = [pauseRect, restartRect, checkRect]
    initButtons = True


def convertGridCoord(cell):
    x_cell = (cell[0] - 103) / 60
    y_cell = (cell[1] - 110) / 60
    return int(x_cell), int(y_cell)

def convertTime(timer) -> str:
    return time.strftime('%M:%S', time.gmtime(timer))

if __name__ == "__main__":
    main()