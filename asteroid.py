from constants import *
import pygame
from circleshape import CircleShape
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        # Move the asteroid in a straight line
        self.position += self.velocity * dt

    def split(self):
        

        # If the asteroid is too small, don't split it further
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        else:
            # Generate a random angle between 20 and 50 degrees
            random_angle = random.uniform(20, 50)

            # Create two new velocity vectors by rotating the current velocity
            new_velocity1 = self.velocity.rotate(random_angle)
            new_velocity2 = self.velocity.rotate(-random_angle)

            # Calculate the new radius for the smaller asteroids
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            # Create two new Asteroid objects
            new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

            # Set velocities for the new asteroids, scaling them up by 1.2
            new_asteroid1.velocity = new_velocity1 * 1.2
            new_asteroid2.velocity = new_velocity2 * 1.2

            # The new asteroids will be automatically added to the necessary groups
            # because of the Asteroid.containers setting in main.py

            self.kill()
