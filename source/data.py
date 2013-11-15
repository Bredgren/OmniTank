
import pygame, os

class Data:
    def __init__(self, root):
        self.sound_file = os.path.join(root, 'data', 'sounds')
        self.image_file = os.path.join(root, 'data', 'images')

        self.images = {}
        self.sounds = {}
    
    def getSound(self, file):
        sound = None
        if file in self.sounds:
            sound = self.sounds[file]
        else:
            file = os.path.join(self.sound_file, file)
            sound = pygame.mixer.Sound(file)
            self.sounds[file] = sound
        return sound

    def getImage(self, file):
        image = None
        if file in self.images:
            image = self.images[file]
        else:
            file = os.path.join(self.image_file, file)
            image = pygame.image.load(file)#.convert()
            self.images[file] = image
        return image

    def startMusic(self, file):
        pygame.mixer.music.load(os.path.join(sound_file, file))
        pygame.mixer.music.play(-1)

    def pauseMusic(self):
        pygame.mixer.music.pause()

    def unpauseMusic(self):
        pygame.mixer.music.unpause()

# Gobal variable acts as Singleton
GameData = Data('..')
