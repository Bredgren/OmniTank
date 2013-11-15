
import pygame

class Window:
    def __init__(self, size, caption):
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption(caption)
##        icon_img = os.path.join("images", "icon.png")
##        icon = pygame.image.load(icon_img)
##        pygame.display.set_icon(icon)
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.running = True

    def run(self):
        while self.running:
            time_passed = self.clock.tick(self.fps)
            self.handleInput()
            self.clear()
            self.update(time_passed)
            self.draw()

    def clear(self):
        pass

    def handleInput(self):
        pass

    def update(self, time_passed):
        pass

    def draw(self):
        pass


