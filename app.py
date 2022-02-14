import pygame
import pygame.gfxdraw
import constants as utils
import time

pygame.display.init()
clock = pygame.time.Clock()
animation = pygame.time.Clock()
animation2 = pygame.time.Clock()

time_elapsed = 0
time_elapsed_reset = 0
time_elapsed_check = 0
reset_animation = False
check_animation = False
timer = 0


cells = []
init_buttons = False
buttons = []
init_list = False
pause = False
pause_title_rect = pygame.Rect(0, 0, 500, 500)

grid = [[[2, -1], [2, -1], [1, -1], [5, -1], [3, -1]],
        [[2, -1], [3, -1], [1, -1], [4, -1], [5, -1]],
        [[1, -1], [1, -1], [1, -1], [3, -1], [5, -1]],
        [[1, -1], [3, -1], [5, -1], [4, -1], [2, -1]],
        [[5, -1], [4, -1], [3, -1], [2, -1], [1, -1]]]

def main():
    pygame.display.set_caption(utils.NAME)
    pygame.display.set_icon(utils.LOGO)
    screen = pygame.display.set_mode((utils.WIDTH, utils.HEIGHT))

    global pause
    global reset_animation
    global check_animation
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
                    if button[0].collidepoint(pos):
                        if button[1] == 0:
                            buttons[0][1] = 0
                            buttons[1][1] = 0
                            buttons[2][1] = 0
                            if buttons.index(button) == 0: # if check
                                checkGrid(grid)
                                check_animation = True
                                button[1] = 1
                            elif buttons.index(button) == 1: # if pause
                                if pause == False:
                                    button[1] = 1
                                    pause = True
                            elif buttons.index(button) == 2: # if reset
                                resetGrid()
                                reset_animation = True
                                button[1] = 1
                        else:
                            if buttons.index(button) == 2:
                                if pause == False:
                                    button[1] = 0
                if pause and pause_title_rect.collidepoint(pos) and buttons[1][0].collidepoint(pos) == False:
                    pause = False
                    buttons[1][1] = 0

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

        resetButtonAnimation()
        checkButtonAnimation()

        printTitle("Victoire! c'est génial mec", True, screen)

        if pause == True:
            setInPause(screen)

        # Update    
        pygame.display.update()

def drawBoard(screen, x, y):
    margin = (50 + utils.MARGIN)
    global init_list
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

            if init_list == False:
                cells.append(rect)
    init_list = True

def drawTimer(screen, x, y):
    global time_elapsed
    global timer
    global pause
    if pause == False:
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
    global init_buttons
    x = (utils.WIDTH / 2) - 27
    y = utils.HEIGHT - (utils.HEIGHT / 8) - 19

    pauseRect = pygame.Rect(x, y, 50, 50)
    restartRect = pygame.Rect(x + 80, y, 50, 50)
    checkRect = pygame.Rect(x - 80, y, 50, 50)

    if init_buttons == False:
        buttons = [[checkRect, 0], [pauseRect, 0], [restartRect, 0]]
    init_buttons = True

    pause = utils.PAUSE
    pause = pygame.transform.scale(pause, (50, 50))
    pause_pressed = utils.PAUSE_PRESSED
    pause_pressed = pygame.transform.scale(pause_pressed, (50, 50))
    if (buttons[1][1] == 0):
        screen.blit(pause, (x, y))
    else:
        screen.blit(pause_pressed, (x, y))

    restart = utils.RESTART
    restart = pygame.transform.scale(restart, (50,50))
    restart_pressed = utils.RESTART_PRESSED
    restart_pressed = pygame.transform.scale(restart_pressed, (50, 50))
    screen.blit(restart, (x + 80, y))
    if buttons[2][1] == 0:
        screen.blit(restart, (x + 80, y))
    else:
        screen.blit(restart_pressed, (x + 80, y))

    check = utils.CHECK
    check = pygame.transform.scale(check, (50,50))
    check_pressed = utils.CHECK_PRESSED
    check_pressed = pygame.transform.scale(check_pressed, (50, 50))
    screen.blit(check, (x - 80, y))
    if buttons[0][1] == 0:
        screen.blit(check, (x - 80, y))
    else:
        screen.blit(check_pressed, (x - 80, y))

def checkGrid(grid:list):
    print("Checking...")
    buttons[0][1] = 0

def setInPause(screen):
    rect = pygame.Surface((500,500), pygame.SRCALPHA, 32)
    rect.fill((0, 0, 0, 150))
    screen.blit(rect, (0,0))

    text = utils.FONT_PAUSED.render("GAME PAUSED", False, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.center = pygame.Rect(utils.WIDTH / 2 - 25, utils.HEIGHT / 2 - 25, 50, 50).center
    screen.blit(text, text_rect)

def resetGrid():
    global grid
    for row in range(len(grid)):
        for column in range(len(grid)):
            grid[row][column][1] = -1
    print(grid)

def resetButtonAnimation():
    global reset_animation
    global time_elapsed_reset
    global buttons
    tick = animation.tick()
    if reset_animation == True:
        time_elapsed_reset += tick
        if time_elapsed_reset > 100:
            reset_animation = False
            time_elapsed_reset = 0
            buttons[2][1] = 0

def checkButtonAnimation():
    global check_animation
    global time_elapsed_check
    global buttons
    tick = animation2.tick()
    if check_animation == True:
        time_elapsed_check += tick
        if time_elapsed_check > 100:
            check_animation = False
            time_elapsed_check = 0
            buttons[0][1] = 0

def printTitle(text, type, screen):
    color = (255, 242, 0)
    if type == False:
        color = (255, 0, 0)
    text = utils.FONT_TIMER.render(text, False, color)
    text_rect = text.get_rect()
    text_rect.center = pygame.Rect(0, 55, utils.HEIGHT, 50).center
    screen.blit(text, text_rect)


def convertGridCoord(cell):
    x_cell = (cell[0] - 103) / 60
    y_cell = (cell[1] - 110) / 60
    return int(x_cell), int(y_cell)

def convertTime(timer) -> str:
    return time.strftime('%M:%S', time.gmtime(timer))

if __name__ == "__main__":
    main()