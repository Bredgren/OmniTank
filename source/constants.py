
import pygame

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768

ICON_IMG = 'icon.png'
BUTTON_IMG = 'selection_outline.png'
MAIN_BGD_IMG = 'main_menu.png'
INSTRUCTIONS_BGD_IMG = 'instructions.png'
HIGH_SCORES_BGD_IMG = 'high_scores.png'

BGD_COLOR = pygame.Color(192, 192, 192)
DEFAULT_FONT_COLOR = pygame.Color(0, 148, 255)
SELECTION_FONT_COLOR = pygame.Color(255, 255, 100)

FONT = 'courier'

BGD_MUSIC = 'Mechanolith.mp3'

ROLLOVER_SFX = 'menu_rollover.wav'
CLICK_SFX = 'menu_click.wav'

from os import path
SOUND_FILE = path.join('..', 'data', 'sounds')
IMAGE_FILE = path.join('..', 'data', 'images')
SCORES_DB = path.join('..', 'data', 'local_scores.db')

### Magic numbers
# General
BTN_SIZE = (290, 40)
# Main menu
# Instructions page
# High score page
HS_RETURN_BTN_POS = (368, 694)
HS_LOCAL_BTN_POS = (217, 58)
HS_GLOBAL_BTN_POS = (517, 58)
HS_TAB_SIZE = (290, 10)
HS_TAB_LOCAL_POS = (217, 98)
HS_TAB_GLOBAL_POS = (517, 98)
HS_ENTRY_FONT_SIZE = 25
HS_ENTRY_POSITIONS = 11
HS_ENTRY_TOP = (217, 108)
HS_ENTRY_GAP = 10
HS_ENTRY_OFFSET = (8, 7)
HS_ENTRY_SIZE = (590, BTN_SIZE[1])

HS_ENTRY_NUM_LENGTH = 4
HS_ENTRY_MAX_NAME_LENGTH = 10
HS_ENTRY_LEVEL_LENGTH = 2
HS_ENTRY_POINTS_LENGTH = 12

