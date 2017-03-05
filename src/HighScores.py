#!/usr/bin/env python
"""Functions and classes used for the game's highscores menu. This file can also be run
on it's own to start the game from the highscores menu."""
from collections import namedtuple
import button
import game
import pygame
from pygame.locals import ( # pylint: disable=no-name-in-module
    Rect,
    QUIT, MOUSEBUTTONDOWN, KEYDOWN,
    K_m)

class HighScores(game.GameState):
    """The class for the highscores menu of the game."""
    caption = "OmniTank High Scores"
    img_assets = {
        "icon": "icon.png",
        "background": "highscores.png",
        "outline": "selection_outline.png",
    }
    snd_assets = {
        "rollover": "menu_rollover.wav",
        "click": "menu_click.wav",
    }

    scores_file = "highscores.txt"
    dark_blue = (89, 141, 178)
    font_name = "arial"
    font_size = 30
    max_scores = 10

    def __init__(self, display, clock):
        super().__init__(display, clock)
        self.music_paused = False

        self.scores_drawn = False

    def setup(self):
        super().setup()
        pygame.mouse.set_visible(True)

        btn_size = (290, 40)
        outline = self.img("outline")
        self.btn_group.add(button.Outline("return", Rect((368, 695), btn_size), outline))

        self.snd("rollover").set_volume(0.5)

        self.draw_scores()
        pygame.display.flip()

    def draw_scores(self):
        """Reads the highscores file and draws then to the display."""
        font = pygame.font.SysFont(self.font_name, self.font_size)
        scores = parse_scores_file(self.scores_file)
        x = 330
        y = 163
        gap = 51
        for i, score in enumerate(scores):
            txt = "%s:  %s  lvl: %s" %(score.name, score.score, score.level)
            image = font.render(txt, True, self.dark_blue)
            self.display.blit(image, (x, y + (gap * i)))

    def update(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
            elif event.type == MOUSEBUTTONDOWN and self.hovered_btns:
                self.snd("click").play()
                clicked = self.hovered_btns[0]
                if clicked.name == "return":
                    self.running = False
            elif event.type == KEYDOWN:
                if event.key == K_m:
                    self.music_paused = not self.music_paused
                    if self.music_paused:
                        pygame.mixer.music.unpause()
                    else:
                        pygame.mixer.music.pause()

    def draw(self):
        if self.scores_drawn:
            return
        self.draw_scores()
        self.scores_drawn = True

Score = namedtuple("Score", ["name", "score", "level"])

def parse_scores_file(filename):
    """Parses a file that contains a list of high scores and returns a list of Score
    objects for each entry."""
    scores = []
    with open(filename, "r") as scores_file:
        for line in scores_file:
            line = line.rstrip()
            info = line.split(":")
            scores.append(Score(info[0], int(info[1]), float(info[2])))
    return scores

def main():
    """Sets up pygame and runs the highscores menu."""
    display, clock = game.init_pygame()
    highscores = HighScores(display, clock)
    highscores.run()

if __name__ == "__main__":
    main()
