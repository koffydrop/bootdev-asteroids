import pygame as pg

from constants import *  # noqa: F403


def main():
    _, fail_count = pg.init()
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # noqa: F405
    while True:
        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                return
        screen.fill(pg.color.Color(0, 0, 0))
        pg.display.flip()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")  # noqa: F405
    print(f"Screen height: {SCREEN_HEIGHT}")  # noqa: F405


if __name__ == "__main__":
    main()
