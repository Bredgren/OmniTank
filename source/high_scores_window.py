
import pygame
from pygame.locals import *
from constants import *
from data import GameData
from window import Window
from button import Button

#TODO: external database for global high scores (how to securely access?)
class HighScoresWindow(Window):
    def __init__(self, size, caption=None, win=None):
        Window.__init__(self, size, caption, win)
        self.background = GameData.image(HIGH_SCORES_BGD_IMG)

        button_image = GameData.image(BUTTON_IMG)
        self.main_menu_button = Button((368, 694), button_image, self.buttons)

    def setup(self):
        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()

    def handleEvent(self, event):
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                self.running = False
        elif event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                selection = self.selectedButton()
                if selection == self.main_menu_button:
                    self.running = False

if __name__ == '__main__':
    pygame.init()
    
    main = HighScoresWindow((SCREEN_WIDTH, SCREEN_HEIGHT), 'OmniTank High Scores - Standalone')
    main.run()

    pygame.quit()
