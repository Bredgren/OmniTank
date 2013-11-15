
import pygame
from data import GameData
from constants import *

class Window:
    def __init__(self, size, caption):
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption(caption)
        pygame.display.set_icon(GameData.image(ICON_IMG))
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.running = True
        self.buttons = pygame.sprite.LayeredDirty()

    def run(self):
        while self.running:
            time_passed = self.clock.tick(self.fps)
            self.handleInput()
            self.clear()
            self.update(time_passed)
            self.draw()
        self.cleanup()

    def clear(self):
        pass

    def handleInput(self):
        pass

    def update(self, time_passed):
        pass

    def draw(self):
        pass

    def cleanup(self):
        pass

    def selectedButton(self):
        for button in self.buttons:
            if button.visible:
                return button
        return None


