#!/usr/bin/env python
"""The main game."""
import game
import pygame
from pygame.locals import ( # pylint: disable=no-name-in-module
    QUIT, KEYDOWN,
    K_m)

class OmniTank(game.GameState):
    """The class for the game play state."""
    caption = "OmniTank Menu"
    img_assets = {
        "icon": "icon.png",
        "background": "grey_background.png",
        "omnitank_blue": "omnitank_blue.png",
        "omnitank_red": "omnitank_red.png",
        "omnitank_green": "omnitank_green.png",
        "omnitank_dark": "omnitank_dark.png",
        "omnitank_light": "omnitank_light.png",
        "saucer": "saucer_enemy.png",
        "triangle": "triangle_enemy.png",
        "tank": "tank_enemy.png",
        "mine": "mine_enemy.png",
        "trishot": "trishot_enemy.png",
        "boss": "boss.png",
        "target": "target_S.png",
        "player_bullet": "omni_bullet.png",
        "saucer_bullet": "saucer_bullet.png",
        "triangle_bullet": "triangle_bullet.png",
        "tank_bullet": "tank_bullet.png",
        "mine1": "mine1.png",
        "mine2": "mine2.png",
        "trishot_laser": "trishot_laser.png",
        "boss_laser": "boss_laser.png",
        "expl1": "explosion1.png",
        "expl2": "explosion2.png",
        "expl3": "explosion3.png",
    }
    snd_assets = {
        "player_shot": "player_shot.wav",
        "saucer_shot": "saucer_shot.wav",
        "triangle_shot": "tirangle_shot.wav",
        "tank_shot": "tank_shot.wav",
        "mine_drop": "mine_drop.wav",
        "explosion": "explosion.wav",
        "trishot": "trishot_shot.wav",
        "boss_shot": "boss_shot.wav",
    }

    def __init__(self, display, clock):
        super().__init__(display, clock)
        self.music_paused = False

    def setup(self):
        super().setup()
        pygame.mouse.set_visible(False)

    def update(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
            elif event.type == KEYDOWN:
                if event.key == K_m:
                    self.music_paused = not self.music_paused
                    if self.music_paused:
                        pygame.mixer.music.unpause()
                    else:
                        pygame.mixer.music.pause()

def main():
    """Sets up pygame and runs the game."""
    display, clock = game.init_pygame()
    main_game = OmniTank(display, clock)
    main_game.run()

if __name__ == "__main__":
    main()
