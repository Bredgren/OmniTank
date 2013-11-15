
import pygame
from pygame.locals import *
from constants import *
from data import GameData
from window import Window
from button import Button

class MainWindow(Window):
    def __init__(self, size, caption=None):
        Window.__init__(self, size, 'OmniTank Menu')
        self.background = GameData.image(MAIN_BGD_IMG)

        button_image = GameData.image(BUTTON_IMG)
        self.start_button = Button((367, 311), button_image, self.buttons)
        self.instructions_button = Button((367, 363), button_image, self.buttons)
        self.highscores_button = Button((367, 413), button_image, self.buttons)
        self.quit_button = Button((367, 465), button_image, self.buttons)

        GameData.musicVolumeIs(0.5)
        GameData.startMusic(BGD_MUSIC)

        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()

    def handleInput(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.running = False
                elif event.key == K_m:
                    GameData.toggleMusic()
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    selection = self.selectedButton()
                    if selection:
                        GameData.playSound(CLICK_SFX)
                        if selection == self.start_button:
                            pass
                        elif selection == self.instructions_button:
                            pass
                        elif selection == self.highscores_button:
                            pass
                        elif selection == self.quit_button:
                            self.running = False

    def clear(self):
        self.buttons.clear(self.screen, self.background)

    def update(self, time_passed):
        pre_selected = self.selectedButton()
            
        self.buttons.update()
        
        post_selected = self.selectedButton()
            
        # Play sound when the mouse enters a button or enters a different button
        if post_selected and pre_selected != post_selected:
            GameData.playSound(ROLLOVER_SFX)
        
    def draw(self):
        dirty = self.buttons.draw(self.screen)
        pygame.display.update(dirty)

    def cleanup(self):
        # Wait to let the click sound play
        pygame.time.wait(300)

if __name__ == '__main__':
    pygame.init()
    
    main = MainWindow((SCREEN_WIDTH, SCREEN_HEIGHT))
    main.run()

    pygame.quit()
