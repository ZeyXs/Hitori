import pygame
pygame.font.init()

# --- TEXTURES ---
LOGO = pygame.image.load("resources/favicon.png")
GUI_TIMER = pygame.image.load("resources/gui_timer.png")

PAUSE = pygame.image.load("resources/pause_button.png")
PAUSE_PRESSED = pygame.image.load("resources/pause_button_pressed.png")

RESTART = pygame.image.load("resources/restart_button.png")
RESTART_PRESSED = pygame.image.load("resources/restart_button_pressed.png")

CHECK = pygame.image.load("resources/check_button.png")
CHECK_PRESSED = pygame.image.load("resources/check_button_pressed.png")

# --- COLORS ---
BACKGROUND_COLOR = (247, 247, 247)
CELLS_COLOR = (255, 255, 255)
BORDER_COLOR = (209, 209, 209)

# --- SCREEN ---
NAME = "Hitori"
HEIGHT = 500
WIDTH = 500
MARGIN = 10

# --- FONT ---
FONT = pygame.font.Font("resources/font/Pixeled.ttf", 22)
FONT_TIMER = pygame.font.Font("resources/font/Pixeled.ttf", 15)
