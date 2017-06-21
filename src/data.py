#!/usr/bin/env python
"""Functions for loading image and sound data."""
import os
import re
from collections import namedtuple
import pygame
import yaml

IMG_PATH = "img"
SND_PATH = "snd"

def load_image(filename):
    """Loads an image, prepares it for use."""
    img_file = os.path.join(IMG_PATH, filename)
    surface = pygame.image.load(img_file)
    return surface

def load_sound(filename):
    """Loads a sound, prepares it for play."""
    snd_file = os.path.join(SND_PATH, filename)
    sound = pygame.mixer.Sound(snd_file)
    return sound

def load_music(filename):
    """Loads a music file."""
    pygame.mixer.music.load(os.path.join(SND_PATH, filename))

class SafeYaml(yaml.YAMLObject):
    """Class for using safe YAML loader."""
    yaml_loader = yaml.SafeLoader

class Data(SafeYaml):
    """Top level holder for everything in data.yaml."""
    yaml_tag = u"!Data"
    def __repr__(self):
        attrs = ["%s=%r" % (attr, getattr(self, attr)) for attr in
                 ("icon", "width", "height", "target_fps", "main_menu",
                  "instruction_menu", "highscore_menu", "color_menu",
                  "game")]
        return "Data(%s)" % ", ".join(attrs)

class Menu(SafeYaml):
    """Config for a menu."""
    yaml_tag = u"!Menu"

class TextButton(SafeYaml):
    """Config for a button that has text."""
    yaml_tag = u"!TextButton"

    def make_button(self, maker):
        """Uses the given button maker to make an actual text button."""
        maker.make_text_button(self)

class ImgButton(SafeYaml):
    """Confit for a button that used image(s)."""
    yaml_tag = u"!ImgButton"

    def make_button(self, maker):
        """Uses the given button maker to make an actual image button."""
        maker.make_img_button(self)

class Game(SafeYaml):
    """Config for the main game state."""
    yaml_tag = u"!Game"

class Tanks(SafeYaml):
    """Holder for all tank info."""
    yaml_tag = u"!Tanks"

class Tank(SafeYaml):
    """Config for a single tank."""
    yaml_tag = u"!Tank"

Vec = namedtuple("Vec", "x, y")
def pos_constructor(loader, node):
    """Interprets two nubmers separated by a comma and a space as a vector."""
    value = loader.construct_scalar(node)
    x, y = map(float, value.split(", "))
    return Vec(x, y)

def parse_data_file(filename):
    """Parses yaml file and returns it as a Data class."""
    yaml.add_constructor(u"!vec", pos_constructor, Loader=yaml.SafeLoader)
    yaml.add_implicit_resolver(u"!vec", re.compile(r"[0-9.]+, [0-9.]+"),
                               Loader=yaml.SafeLoader)

    with open(filename) as contents:
        yaml_data = yaml.safe_load(contents)
    return yaml_data

# if __name__ == "__main__":
#     parsed = parse_data_file("data.yaml")
#     print(parsed)
#     print(parsed.width, parsed.height)
#     print(parsed.tanks.player.max_hp)
#     print(parsed.tanks.enemies)
