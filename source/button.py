
import pygame

class Button(pygame.sprite.DirtySprite):
    def __init__(self, pos, image):
        pygame.sprite.DirtySprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect(topleft=pos)

    def update(self):
        prev_selected = self.selected
        if self.rect.collidefpoint:
            self.visible = 1
        else:
            self.visible = 0

        if prev_selected != self.selected:
            self.dirty = 1
