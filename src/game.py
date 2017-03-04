#!/usr/bin/env python
"""General game utilities."""
import data
import pygame

WIDTH = 1024
HEIGHT = 768

def init_pygame():
    """Sets up pygame. Returns the main display and the clock."""
    pygame.init() # pylint: disable=no-member
    display = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    return display, clock

class GameState(object):
    """Represents a single state of the game."""
    caption = "OmniTank"
    icon = "icon.png"
    fps = 60
    img_assets = {}
    snd_assets = {}
    def __init__(self, display, clock):
        self.display = display
        self.clock = clock
        self.running = False
        self._img = {}
        self._snd = {}

    def setup(self):
        """Sets up pygame and loads assets."""
        pygame.display.set_caption(self.caption)
        pygame.display.set_icon(data.load_image(self.icon))
        self._load_assets()

    def _load_assets(self):
        self._img = {name: data.load_image(filename) for name, filename in self.img_assets.items()}
        self._snd = {name: data.load_sound(filename) for name, filename in self.snd_assets.items()}

    def img(self, name):
        """Returns the image with the given name. It is assumed that setup has already
        been called."""
        return self._img[name]

    def snd(self, name):
        """Returns the sound with the given name. It is assumed that setup has already
        been called."""
        return self._snd[name]

    def run(self):
        """Runs the game state. Blocks until self.running is False."""
        self.setup()
        self.running = True
        while self.running:
            self.clock.tick(self.fps)
            self.update()
        self.on_exit()

    def update(self):
        """Process a single game loop."""
        raise NotImplementedError("Must implement the update method.")

    def on_exit(self):
        """Called right before the run method exits."""
        pass
