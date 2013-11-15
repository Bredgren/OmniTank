
import pygame
from pygame.locals import *
from data import GameData
from window import Window
from button import Button

WIDTH = 1024
HEIGHT = 768

class MainWindow(Window):
    def __init__(self, size, caption=None):
        Window.__init__(self, size, 'OmniTank Menu')
        self.background = GameData.getImage('main_menu.png')

        self.buttons = pygame.sprite.LayeredDirty()
        button_image = GameData.getImage('selection_outline.png')
        self.start_button = Button((367, 311), button_image, self.buttons)
        self.instructions_button = Button((367, 363), button_image, self.buttons)
        self.highscores_button = Button((367, 413), button_image, self.buttons)
        self.quit_button = Button((367, 465), button_image, self.buttons)

        self.rollover_sound = GameData.getSound('menu_rollover.wav')
        self.click_sound = GameData.getSound('menu_click.wav')

        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()

    def handleInput(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False

    def clear(self):
        self.buttons.clear(self.screen, self.background)

    def update(self, time_passed):
        self.buttons.update()
        
    def draw(self):
        dirty = self.buttons.draw(self.screen)
        pygame.display.update(dirty)

if __name__ == '__main__':
    pygame.init()
    
    main = MainWindow((WIDTH, HEIGHT))
    main.run()

    pygame.quit()
