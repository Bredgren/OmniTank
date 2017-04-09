#!/usr/bin/env python
"""The main game."""
import game
import tank
import pygame
from pygame.locals import ( # pylint: disable=no-name-in-module
    QUIT, KEYDOWN, KEYUP,
    K_m, K_w, K_a, K_s, K_d, K_l, K_j)

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

    move_keys = {
        "forward": K_w,
        "backward": K_s,
        "left": K_a,
        "right": K_d,
        "turn_right": K_l,
        "turn_left": K_j,
    }

    def __init__(self, display, clock):
        super().__init__(display, clock)
        self.music_paused = False
        self.player = None
        self.group = {}
        self.background = None

    def setup(self):
        super().setup()
        pygame.mouse.set_visible(False)
        self._setup_images()

        self.player = tank.Player(self.img("omnitank_blue"), self.display.get_rect())
        self.player.move_to(self.display.get_rect().center)

        self.group["all"] = pygame.sprite.RenderUpdates()
        self.group["all"].add(self.player)

        s = tank.SaucerEnemy(self.display.get_rect(), self.player, 1)
        s.move_to(self.display.get_rect().center)
        self.group["all"].add(s)

    def _setup_images(self):
        tank.SaucerEnemy.IMAGE = self.img("saucer")

        display_rect = self.display.get_rect()
        bgdtile = self.img("background")
        self.background = pygame.Surface(display_rect.size) # pylint: disable=E1121
        for x in range(0, display_rect.width, bgdtile.get_width()):
            for y in range(0, display_rect.height, bgdtile.get_height()):
                self.background.blit(bgdtile, (x, y))
        self.display.blit(self.background, (0, 0))

    def update(self):
        self._handle_input()

        self.group["all"].clear(self.display, self.background)
        self.group["all"].update()
        dirty = self.group["all"].draw(self.display)
        pygame.display.update(dirty)
        pygame.display.flip()

    def _handle_input(self):
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
                for move, key in self.move_keys.items():
                    if event.key == key:
                        self.player.move[move] = True
            elif event.type == KEYUP:
                for move, key in self.move_keys.items():
                    if event.key == key:
                        self.player.move[move] = False
        # elif event.key == K_p and down:
        #     pause_result = Pause_Menu.pause()

def main():
    """Sets up pygame and runs the game."""
    display, clock = game.init_pygame()
    main_game = OmniTank(display, clock)
    main_game.run()

if __name__ == "__main__":
    main()
