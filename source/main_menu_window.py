
import pygame, data
from pygame.locals import *
from window import Window
from button import Button

WIDTH = 1024
HEIGHT = 768

class MainWindow(Window):
    def __init__(self, size, caption=None):
        Window.__init__(self, size, "OmniTank Menu")
        self.background = data.load_image("main_menu.png")

        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()

    def update(self, time_passed):
        pass

    def handleInput(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False

    def draw(self):
        pass

if __name__ == '__main__':
    pygame.init()
    
    main = MainWindow((WIDTH, HEIGHT))
    main.run()

    pygame.quit()
