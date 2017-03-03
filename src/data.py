#!/usr/bin/env python

imgPath = "img"
sndPath = "snd"

def loadImage(filename):
    """Loads an image, prepares it for use"""
    imgFile = os.path.join(imgPath, filename)
    try:
        surface = pygame.image.load(imgFile)
        return surface
    except pygame.error:
        raise SystemExit("Could not load image '%s' %s" % (filename, pygame.get_error()))

def loadSound(filename):
    """loads a sound, prepares it for play"""
    sndFile = os.path.join(sndPath, filename)
    try:
        sound = pygame.mixer.Sound(sndFile)
        return sound
    except pygame.error:
        raise SystemExit("Could not load sound '%s' %s" % (filename, pygame.get_error()))

def loadMusic(filename):
    pygame.mixer.music.load(os.path.join(sndPath, 'Mechanolith.mp3'))
