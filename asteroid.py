import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        angles = (
            self.velocity.rotate(random.uniform(20, 50)),
            self.velocity.rotate(random.uniform(20, 50)),
        )

        for i in range(len(angles)):
            child = Asteroid(*self.position, self.radius - ASTEROID_MIN_RADIUS)
            child.velocity = angles[i] * 1.2 * (lambda x: -1 if x == 0 else x)(i)
