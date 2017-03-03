#!/usr/bin/env python
"""Functions and classes used for the game's main menu. This file can also be run on it's
own to start the game from the main menu."""
import button
import data
import pygame

def run(display, clock):
    """Runs the main menu using the given pygame display and clock."""
    pygame.display.set_caption("OmniTank Menu")
    pygame.mouse.set_visible(True)

    # images
    outline = data.load_image("selection_outline.png")
    icon = data.load_image("icon.png")
    pygame.display.set_icon(icon)

    # sounds/music
    rolloverSound = data.load_sound("menu_rollover.wav")
    clickSound = data.load_sound("menu_click.wav")
    data.load_music("Mechanolith.mp3")
    pygame.mixer.music.play(-1)

    top = (367, 311)
    second = (367, 363)
    third = (367, 413)
    bottom = (367, 465)
    xLeft = 367
    xRight = 657
    selection = ""
    playsound = False
    running = True
    musicPaused = False

    btnGroup = pygame.sprite.RenderUpdates()

    while running:
        time_passed = clock.tick(60)
        running = False

    print("Bye")

def main():
    import game
    display, clock = game.init_pygame()
    run(display, clock)

if __name__ == "__main__":
    main()
