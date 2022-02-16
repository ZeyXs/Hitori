import pygame
import os
import sys
pygame.font.init()

if getattr(sys, 'frozen', False):
    wd = sys._MEIPASS
else:
    wd = ''

def resourcePath(relativePath):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        basePath = sys._MEIPASS
    except Exception:
        basePath = os.path.abspath(".")

    return os.path.join(basePath, relativePath)

# --- TEXTURES ---
LOGO = pygame.image.load(resourcePath("resources/favicon.png"))
GUI_TIMER = pygame.image.load(resourcePath("resources/gui_timer.png"))

PAUSE = pygame.image.load(resourcePath("resources/pause_button.png"))
PAUSE_PRESSED = pygame.image.load(resourcePath("resources/pause_button_pressed.png"))

RESTART = pygame.image.load(resourcePath("resources/restart_button.png"))
RESTART_PRESSED = pygame.image.load(resourcePath("resources/restart_button_pressed.png"))

CHECK = pygame.image.load(resourcePath("resources/check_button.png"))
CHECK_PRESSED = pygame.image.load(resourcePath("resources/check_button_pressed.png"))

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
FONT_PAUSED = pygame.font.Font("resources/font/Pixeled.ttf", 30)

# --- TEXT ---
VICTORY_TITLE = "You have won!"