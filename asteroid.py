import random
import pygame
from constants import *
from circleshape import CircleShape
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        log_event("asteroid_split")
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            rand_angle = random.uniform(20, 50)
            new_asteroid1_vector = self.velocity.rotate(rand_angle)
            new_asteroid2_vector = self.velocity.rotate(-rand_angle)
            new_asteroid1 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            new_asteroid2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            new_asteroid1.velocity = new_asteroid1_vector * 1.2
            new_asteroid2.velocity = new_asteroid2_vector * 1.2
