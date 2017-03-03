#!/usr/bin/env python
"""GUI button classes."""

import pygame

class ButtonOutline(pygame.sprite.DirtySprite):
    """A sprite that is only visible when the mouse is within the given bounds."""
    def __init__(self, pos, image, bounds, *groups):
        super().__init__(*groups)
        self.pos = pos
        self.image = image
        self.bounds = bounds
        self.rect = self.image.get_rect(topleft=pos)
        self.visible = 0
        self.dirty = 1

    def show(self):
        """Makes the sprite visible."""
        self.visible = 1
        self.dirty = 1

    def hide(self):
        """Makes the sprite invisible."""
        self.visible = 0
        self.dirty = 1

    def update(self):
        """Sets visiblity based on mouse position."""
        if self.bounds.collidepoint(pygame.mouse.get_pos()):
            self.show()
        else:
            self.hide()
