#!/usr/bin/env python

import button
import data

def run(display, clock):
    pygame.display.set_caption("OmniTank Menu")
    pygame.mouse.set_visible(True)

    # images
    outline = data.loadImage("selection_outline.png")
    icon = data.loadImage("icon.png")
    pygame.display.set_icon(icon)

    # sounds/music
    rolloverSound = data.loadSound("menu_rollover.wav")
    clickSound = load_sound("menu_click.wav")
    data.loadMusic("Mechanolith.mp3")
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


def main():
    import game
    display, clock = game.initPygame()
    run(display, clock)

if __name__ == "__main__":
    main()
