
import pygame
from pygame.locals import *
from constants import *
from data import GameData

class Window:
    def __init__(self, size, caption, other_window=None):
        if other_window:
            self.screen = other_window.screen
            self.clock = other_window.clock
        else:
            self.screen = pygame.display.set_mode(size)
            self.clock = pygame.time.Clock()

        self.caption = caption
        pygame.display.set_icon(GameData.image(ICON_IMG))
        
        self.fps = 60
        self.running = True
        self.buttons = pygame.sprite.LayeredDirty()

    def run(self, *args):
        self._setup(args)
        while self.running:
            time_passed = self.clock.tick(self.fps)
            self._handleInput()
            self._clear()
            self._update(time_passed)
            self._draw()
        self._cleanup()

    def setup(self, args=()):
        pass

    def handleEvent(self, event):
        pass

    def clear(self):
        pass

    def update(self, time_passed):
        pass

    def draw(self):
        return [] #important to return a list

    def cleanup(self):
        pass

    def selectedButton(self):
        for button in self.buttons:
            if button.visible:
                return button
        return None

    def delay(self):
        pygame.time.wait(200)

    def _setup(self, args=()):
        self.running = True
        pygame.display.set_caption(self.caption)
        self.setup(args)

    def _handleInput(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
            elif event.type == KEYDOWN:
                if event.key == K_m:
                    GameData.toggleMusic()
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1 and self.selectedButton():
                    GameData.playSound(CLICK_SFX)
            self.handleEvent(event)

    def _clear(self):
        self.buttons.clear(self.screen, self.background)
        self.clear()

    def _update(self, time_passed):
        pre_selected = self.selectedButton()
            
        self.buttons.update()
        
        post_selected = self.selectedButton()
            
        # Play sound when the mouse enters a button or enters a different button
        if post_selected and pre_selected != post_selected:
            GameData.playSound(ROLLOVER_SFX)

        self.update(time_passed)

    def _draw(self):
        dirty = self.draw()
        dirty += self.buttons.draw(self.screen)
        pygame.display.update(dirty)

    def _cleanup(self):
        self.cleanup()
        # Wait to let the click sound play
        self.delay()
