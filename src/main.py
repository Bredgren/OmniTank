#!/usr/bin/env python
"""Main entrance point for the game."""
import game
import MainMenu

def main():
    """The game's main function. Just starts the game at the main menu."""
    display, clock = game.init_pygame()
    MainMenu.run(display, clock)

if __name__ == "__main__":
    main()
