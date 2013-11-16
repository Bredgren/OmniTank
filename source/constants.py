
import pygame

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768

ICON_IMG = 'icon.png'
BUTTON_IMG = 'selection_outline.png'
MAIN_BGD_IMG = 'main_menu.png'
INSTRUCTIONS_BGD_IMG = 'instructions.png'
HIGH_SCORES_BGD_IMG = 'high_scores.png'

BGD_COLOR = pygame.Color(192, 192, 192)

BGD_MUSIC = 'Mechanolith.mp3'

ROLLOVER_SFX = 'menu_rollover.wav'
CLICK_SFX = 'menu_click.wav'

from os import path

SOUND_FILE = path.join('..', 'data', 'sounds')
IMAGE_FILE = path.join('..', 'data', 'images')
SCORES_DB = path.join('..', 'data', 'local_scores.db')
