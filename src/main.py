#!/usr/bin/env python
"""Main entrance point for the game."""
import game
from MainMenu import MainMenu

def main():
    """The game's main function. Just starts the game at the main menu."""
    display, clock = game.init_pygame()
    main_menu = MainMenu(display, clock)
    main_menu.run()

if __name__ == "__main__":
    main()
