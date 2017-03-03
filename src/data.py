#!/usr/bin/env python
"""Functions for loading image and sound data."""
import os
import pygame

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
