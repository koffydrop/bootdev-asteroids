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

        self.velocity = self.velocity.rotate(random.uniform(20, 50))

        for i in range(-1, 2, 2):
            child = Asteroid(*self.position, self.radius - ASTEROID_MIN_RADIUS)
            child.velocity = self.velocity * i * 1.2
