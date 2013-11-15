
import pygame

class Window:
    def __init__(self, size, caption):
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption(caption)
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.running = True

    def run(self):
        while self.running:
            time_passed = self.clock.tick(self.fps)
            self.handleInput()
            self.update(time_passed)
            self.draw()

    def update(self, time_passed):
        pass

    def handleInput(self):
        pass

    def draw(self):
        pass


