#!/usr/bin/env python
"""Functions and classes used for the game's main menu. This file can also be run on it's
own to start the game from the main menu."""
import button
import data
import pygame
from pygame.locals import (QUIT, MOUSEBUTTONDOWN)
import time

def run(display, clock):
    """Runs the main menu using the given pygame display and clock."""
    pygame.display.set_caption("OmniTank Menu")
    pygame.mouse.set_visible(True)

    # images
    background = data.load_image("main_menu.png")
    outline = data.load_image("selection_outline.png")
    icon = data.load_image("icon.png")
    pygame.display.set_icon(icon)

    # sounds/music
    rollover_sound = data.load_sound("menu_rollover.wav")
    click_sound = data.load_sound("menu_click.wav")
    data.load_music("Mechanolith.mp3")
    pygame.mixer.music.play(-1)

    can_play_sound = True
    running = True
    #musicPaused = False

    btn_group = pygame.sprite.LayeredDirty()

    btn_size = (290, 40)
    btn_group.add(button.Outline("start", pygame.Rect((367, 311), btn_size), outline))
    btn_group.add(button.Outline("instructions", pygame.Rect((367, 363), btn_size), outline))
    btn_group.add(button.Outline("highscores", pygame.Rect((367, 413), btn_size), outline))
    btn_group.add(button.Outline("quit", pygame.Rect((367, 465), btn_size), outline))

    display.blit(background, (0, 0))
    pygame.display.flip()
    while running:
        clock.tick(30)

        btn_group.update(pygame.mouse.get_pos())

        # Only play rollover_sound the fist frame a button is hovered over.
        hovered_btns = [btn for btn in btn_group if btn.visible]
        if can_play_sound and hovered_btns:
            rollover_sound.play()
            can_play_sound = False
        elif not can_play_sound and not hovered_btns:
            can_play_sound = True

        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == MOUSEBUTTONDOWN and hovered_btns:
                click_sound.play()
                clicked = hovered_btns[0]
                print("clicked", clicked.name)
                if clicked.name == "start":
                    pass
                elif clicked.name == "instructions":
                    pass
                elif clicked.name == "highscores":
                    pass
                elif clicked.name == "quit":
                    running = False

        btn_group.clear(display, background)
        dirty = btn_group.draw(display)
        pygame.display.update(dirty)

    # Let final click sound play
    time.sleep(0.5)
    print("Bye")

def main():
    import game
    display, clock = game.init_pygame()
    run(display, clock)

if __name__ == "__main__":
    main()
