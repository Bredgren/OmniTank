
import pygame, os

root = '..'
sound_file = os.path.join(root, 'data', 'sounds')
image_file = os.path.join(root, 'data', 'images')
    
def loadSound(file):
    file = os.path.join(sound_file, file)
    sound = pygame.mixer.Sound(file)
    return sound

def startMusic(file):
    pygame.mixer.music.load(os.path.join(sound_file, file))
    pygame.mixer.music.play(-1)

def pauseMusic():
    pygame.mixer.music.pause()

def unpauseMusic():
    pygame.mixer.music.unpause()

def loadImage(file):
    file = os.path.join(image_file, file)
    image = pygame.image.load(file)#.convert()
    return image
