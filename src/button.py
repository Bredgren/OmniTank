#!/usr/bin/env python

class ButtonOutline(pygame.sprite.DirtySprite):
    def __init__(self, pos, image, bounds *groups):
        super().__init__(*groups)
        self.pos = pos
        self.image = image
        self.bounds = bounds
        self.rect = self.image.get_rect(topleft=pos)

    def show(self):
        self.visible = 1
        self.dirty = 1

    def hide(self):
        self.visible = 0
        self.dirty = 1

    def update(self):
        if bounds.collidepoint(pygame.mouse.get_pos()):
            self.show()
        else:
            self.hide()
