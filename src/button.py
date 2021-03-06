#!/usr/bin/env python
"""GUI button classes."""

import pygame

class Maker(object):
    def make_button(self, config):
        config.make_button(self)

    def make_text_button(self, config):
        return Text(config.label, config.pos, config.size)

    def make_img_button(self, config):
        return Text(config.label, config.img, config.pos, config.size)

class Button(pygame.sprite.DirtySprite):
    def __init__(self, action, *groups):
        super().__init__(*groups)
        self.action = action

class Text(Button):
    def __init__(self, label, pos, size, action, *groups):
        super().__init__(action, *groups)
        self.label = label
        self.pos = pos
        self.size = size

class Image(Button):
    def __init__(self, label, img, pos, size, action, *groups):
        super().__init__(action, *groups)
        self.label = label
        self.img = img
        self.pos = pos
        self.size = size

class Outline(pygame.sprite.DirtySprite):
    """A sprite that is only visible when the mouse is within the given bounds."""
    def __init__(self, name, rect, image, *groups):
        super().__init__(*groups)
        self.name = name
        self.bounds = rect
        self.image = image
        self.rect = self.image.get_rect(topleft=rect.topleft)
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

    def update(self, mouse_pos):
        """Sets visiblity based on mouse position."""
        if self.bounds.collidepoint(mouse_pos):
            self.show()
        elif self.visible:
            self.hide()
