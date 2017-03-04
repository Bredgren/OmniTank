#!/usr/bin/env python
"""Functions and classes used for the game's main menu. This file can also be run on it's
own to start the game from the main menu."""
import time
import button
import data
import game
import pygame
from pygame.locals import ( # pylint: disable=no-name-in-module
    Rect,
    QUIT, MOUSEBUTTONDOWN, KEYDOWN,
    K_m)

class MainMenu(game.GameState):
    """The class for the main menu of the game."""
    caption = "OmniTank Menu"
    img_assets = {
        "icon": "icon.png",
        "background": "main_menu.png",
        "outline": "selection_outline.png",
    }
    snd_assets = {
        "rollover": "menu_rollover.wav",
        "click": "menu_click.wav",
    }

    def __init__(self, display, clock):
        super().__init__(display, clock)
        self.can_play_sound = True
        self.btn_group = pygame.sprite.LayeredDirty()

    def setup(self):
        super().setup()
        pygame.mouse.set_visible(True)
        data.load_music("Mechanolith.mp3")
        pygame.mixer.music.play(-1)

        btn_size = (290, 40)
        outline = self.img("outline")
        self.btn_group.add(button.Outline("start", Rect((367, 311), btn_size), outline))
        self.btn_group.add(button.Outline("instructions", Rect((367, 363), btn_size), outline))
        self.btn_group.add(button.Outline("highscores", Rect((367, 413), btn_size), outline))
        self.btn_group.add(button.Outline("quit", Rect((367, 465), btn_size), outline))

        self.display.blit(self.img("background"), (0, 0))
        pygame.display.flip()

    def update(self):
        self.btn_group.update(pygame.mouse.get_pos())
        hovered_btns = [btn for btn in self.btn_group if btn.visible]

        self._update_btns(hovered_btns)

        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
            elif event.type == MOUSEBUTTONDOWN and hovered_btns:
                self.snd("click").play()
                clicked = hovered_btns[0]
                print("clicked", clicked.name)
                if clicked.name == "start":
                    pass
                elif clicked.name == "instructions":
                    pass
                elif clicked.name == "highscores":
                    pass
                elif clicked.name == "quit":
                    self.running = False
            elif event.type == KEYDOWN:
                if event.key == K_m:
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.unpause()

        self.btn_group.clear(self.display, self.img("background"))
        dirty = self.btn_group.draw(self.display)
        pygame.display.update(dirty)

    def _update_btns(self, hovered_btns):
        # Only play rollover_sound the fist frame a button is hovered over.
        if self.can_play_sound and hovered_btns:
            self.snd("rollover").play()
            self.can_play_sound = False
        elif not self.can_play_sound and not hovered_btns:
            self.can_play_sound = True

    def on_exit(self):
        time.sleep(0.5)
        print("Bye")

def main():
    """Sets up pygame and runs the main menu."""
    display, clock = game.init_pygame()
    main_menu = MainMenu(display, clock)
    main_menu.run()

if __name__ == "__main__":
    main()
