
import pygame
from pygame.locals import *
from constants import *
from data import GameData
from window import Window
from button import Button
from high_scores_helpers import HighScores

class HighScoresWindow(Window):
    def __init__(self, size, caption=None, win=None):
        Window.__init__(self, size, caption, win)
        self.background = GameData.image(HIGH_SCORES_BGD_IMG)

        button_image = GameData.image(BUTTON_IMG)
        self.main_menu_button = Button((368, 694), button_image, self.buttons)
        self.local_button = Button((217, 58), button_image)
        self.global_button = Button((517, 58), button_image, self.buttons)

        self.tab_container = pygame.sprite.LayeredDirty()
        self.tab = Tab(self.tab_container)

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
                elif selection == self.local_button:
                    self.tab.setScopeLocal()
                    self.buttons.add(self.global_button)
                    self.buttons.remove(self.local_button)
                elif selection == self.global_button:
                    self.tab.setScopeGlobal()
                    self.buttons.add(self.local_button)
                    self.buttons.remove(self.global_button)

    def clear(self):
        self.tab_container.clear(self.screen, self.background)

    def draw(self):
        dirty = self.tab_container.draw(self.screen)
        return dirty

class Tab(pygame.sprite.DirtySprite):
    def __init__(self, container):
        pygame.sprite.DirtySprite.__init__(self, container)
        self.image = pygame.Surface((290, 10))
        self.image.fill(BGD_COLOR)
        self.rect = pygame.Rect(0, 0, 290, 10)
        self.visible = 1
        self.state = None
        self.setScopeLocal()

    def setScopeLocal(self):
        if self.state != 'local':
            self.state = 'local'
            self.rect.topleft = (217, 98)
            self.dirty = 1

    def setScopeGlobal(self):
        if self.state != 'global':
            self.state = 'global'
            self.rect.topleft = (517, 98)
            self.dirty = 1

##class Entry(pygame.sprite.DirtySprite):
##    def __init__(self, container):
##        pygame.sprite.DirtySprite.__init__(self, container)
##        self.image = pygame.Surface((290, 10))
##        self.image.fill(BGD_COLOR)
##        self.rect = pygame.Rect(0, 0, 290, 10)
##        self.visible = 1
##        self.setScopeLocal()

if __name__ == '__main__':
    pygame.init()
    
    main = HighScoresWindow((SCREEN_WIDTH, SCREEN_HEIGHT), 'OmniTank High Scores - Standalone')
    main.run()

    pygame.quit()
