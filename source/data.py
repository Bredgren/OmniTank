
import pygame, os

root = '..'
sound_file = os.path.join(root, 'data', 'sounds')
image_file = os.path.join(root, 'data', 'images')
    
def load_sound(file):
    file = os.path.join(sound_file, file)
    sound = pygame.mixer.Sound(file)
    return sound

def load_image(file):
    file = os.path.join(image_file, file)
    image = pygame.image.load(file)
    return image
