
import pygame
from pygame.locals import *
from constants import *
from data import GameData
from window import Window
from button import Button
from instructions_window import InstructionsWindow
#from high_scores_window import HighScoresWindow
#from color_choice_window import ColorChoiceWindow

class MainWindow(Window):
    def __init__(self, size, caption=None):
        Window.__init__(self, size, 'OmniTank Menu')
        self.background = GameData.image(MAIN_BGD_IMG)

        button_image = GameData.image(BUTTON_IMG)
        self.start_button = Button((367, 311), button_image, self.buttons)
        self.instructions_button = Button((367, 363), button_image, self.buttons)
        self.highscores_button = Button((367, 413), button_image, self.buttons)
        self.quit_button = Button((367, 465), button_image, self.buttons)

        self.instructions_window = InstructionsWindow(size, 'OmniTank Instructions', self)
        #self.high_scores_window = HighScoresWindow(size, 'OmniTank High Scores', self)
        #self.color_choice_window = ColorChoiceWindow(size, 'OmniTank Color Choice', self)

        GameData.musicVolumeIs(0.5)
        GameData.startMusic(BGD_MUSIC)

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
                self.delay() # Don't switch menus instantly
                if selection == self.start_button:
                    #self.color_choice_window.run()
                elif selection == self.instructions_button:
                    self.instructions_window.run()
                elif selection == self.highscores_button:
                    #self.high_scores_window.run()
                elif selection == self.quit_button:
                    self.running = False
                # Must reset caption if another window changed it
                pygame.display.set_caption(self.caption)


if __name__ == '__main__':
    pygame.init()
    
    main = MainWindow((SCREEN_WIDTH, SCREEN_HEIGHT))
    main.run()

    pygame.quit()
