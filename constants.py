import pygame
import os
import sys
pygame.font.init()

if getattr(sys, 'frozen', False):
    wd = sys._MEIPASS
else:
    wd = ''   

# --- TEXTURES ---
LOGO = pygame.image.load(os.path.join(wd,'resources',"favicon.png"))
GUI_TIMER = pygame.image.load(os.path.join(wd,'resources',"gui_timer.png"))

PAUSE = pygame.image.load(os.path.join(wd,'resources',"pause_button.png"))
PAUSE_PRESSED = pygame.image.load(os.path.join(wd,'resources',"pause_button_pressed.png"))

RESTART = pygame.image.load(os.path.join(wd,'resources',"restart_button.png"))
RESTART_PRESSED = pygame.image.load(os.path.join(wd,'resources',"restart_button_pressed.png"))

CHECK = pygame.image.load(os.path.join(wd,'resources',"check_button.png"))
CHECK_PRESSED = pygame.image.load(os.path.join(wd,'resources',"check_button_pressed.png"))

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