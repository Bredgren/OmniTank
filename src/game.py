#!/usr/bin/env python
"""General game utilities."""
import pygame

WIDTH = 1024
HEIGHT = 768

def init_pygame():
    """Sets up pygame. Returns the main display and the clock."""
    pygame.init() # pylint: disable=no-member
    display = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    return display, clock
