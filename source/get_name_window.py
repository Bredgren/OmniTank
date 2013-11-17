
import pygame
from pygame.locals import *
from constants import *
from data import GameData
from window import Window
from button import Button

class GetNameWindow(Window):
    def __init__(self, size, caption=None, win=None):
        Window.__init__(self, size, caption, win)
        self.background = GameData.image(GET_NAME_BGD_IMG)

        button_image = GameData.image(BUTTON_IMG)
        self.ok_button = Button(GN_OK_BTN_POS, button_image, self.buttons)

        self.return_data = "NO NAME"

    def setup(self, args=()):
        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()

    def handleEvent(self, event):
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                self.running = False
                GameData.playSound(CLICK_SFX)
        elif event.type == MOUSEBUTTONDOWN:
            if event.button == LEFT_MOUSE:
                selection = self.selectedButton()
                if selection == self.ok_button:
                    self.running = False

if __name__ == '__main__':
    pygame.init()
    
    main = InstructionsWindow((SCREEN_WIDTH, SCREEN_HEIGHT), 'OmniTank Instructions - Standalone')
    main.run()

    pygame.quit()
