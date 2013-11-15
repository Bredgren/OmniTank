
import pygame

class Button(pygame.sprite.DirtySprite):
    def __init__(self, pos, image, container=None):
        pygame.sprite.DirtySprite.__init__(self, container)
        self.image = image
        self.rect = self.image.get_rect(topleft=pos)
        self.visible = 0

    def update(self):
        prev_vis = self.visible
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.visible = 1
        else:
            self.visible = 0
        self.dirty = 1
        if prev_vis != self.visible:
            self.dirty = 1
