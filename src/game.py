#!/usr/bin/env python
import pygame

width = 1024
height = 768

def initPygame():
    """Sets up pygame. Returns the main display and the clock."""
    pygame.init()
    display = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    return display, clock
