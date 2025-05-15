import pygame as pg

from asteroid import Asteroid
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from field import AsteroidField
from player import Player, Shot


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    clock = pg.time.Clock()
    dt = 0

    updatable = pg.sprite.Group()
    drawable = pg.sprite.Group()
    asteroids = pg.sprite.Group()
    shots = pg.sprite.Group()

    Player.containers = (drawable, updatable)
    Asteroid.containers = (drawable, updatable, asteroids)
    AsteroidField.containers = updatable
    Shot.containers = (drawable, updatable, shots)

    _, fail_count = pg.init()
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    AsteroidField()

    while True:
        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for d in drawable:
            d.draw(screen)
        for asteroid in asteroids:
            if player.check_collide(asteroid):
                print("Game over!")
                return
        for asteroid in asteroids:
            for bullet in shots:
                if asteroid.check_collide(bullet):
                    asteroid.split()
                    bullet.kill()
        pg.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
