
import pygame, os, constants

"""A class for managing the games sound and image assets. It can be used to load
data when it is fist needed or to load things ahead of time."""
class Data:
    def __init__(self):
        self.sound_file = constants.SOUND_FILE
        self.image_file = constants.IMAGE_FILE

        self.images = {}
        self.sounds = {}

        # pygame.mixes.music.get_busy() returns True when paused so there
        # is no other way to check for paused music.
        self._music_paused = False

    def playSound(self, file):
        sound = None
        if file in self.sounds:
            sound = self.sounds
        else:
            sound = self.loadSound(file)
        pygame.mixer.stop()
        sound.play()

    def sound(self, file):
        if file in self.sounds:
            return self.sounds[file]
        return self.loadSound(file)

    def image(self, file):
        if file in self.images:
            return self.images[file]
        return self.loadImage(file)
    
    def loadSound(self, file):
        if file not in self.sounds:
            file = os.path.join(self.sound_file, file)
            sound = pygame.mixer.Sound(file)
            self.sounds[file] = sound
            return sound
        return self.sound(file)

    def loadImage(self, file):
        if file not in self.images:
            file = os.path.join(self.image_file, file)
            image = pygame.image.load(file)#.convert()
            self.images[file] = image
            return image
        return self.image(file)

    def unloadSound(self, file):
        if file in self.sounds:
            del self.sounds[file]

    def unloadImage(self, file):
        if file in self.images:
            del self.images[file]

    def startMusic(self, file):
        pygame.mixer.music.load(os.path.join(self.sound_file, file))
        pygame.mixer.music.play(-1)

    def pauseMusic(self):
        pygame.mixer.music.pause()

    def unpauseMusic(self):
        pygame.mixer.music.unpause()

    def toggleMusic(self):
        if self._music_paused:
            self.unpauseMusic()
        else:
            self.pauseMusic()
        self._music_paused = not self._music_paused

    def musicVolumeIs(self, vol):
        pygame.mixer.music.set_volume(vol)

# Gobal variable acts as Singleton
GameData = Data()
