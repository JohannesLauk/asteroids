import pygame
from constants import *
from circleshape import CircleShape
from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        # Add a new variable for the shooting cooldown timer
        self.shoot_cooldown = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)  # Invert dt for left rotation
        if keys[pygame.K_d]:
            self.rotate(dt)  # Right rotation

        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)

        # Handle shooting
        if keys[pygame.K_SPACE]:
            self.shoot()

        # Decrease the shooting cooldown timer
        self.shoot_cooldown = max(0, self.shoot_cooldown - dt)

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        # Check if the cooldown has expired before shooting
        if self.shoot_cooldown <= 0:
            # Create a forward vector pointing downwards
            forward = pygame.Vector2(0, 1)
            # Rotate it to match the player's rotation
            forward = forward.rotate(self.rotation)
            # Scale it up to set the shot's speed
            shot_velocity = forward * PLAYER_SHOOT_SPEED
            # Create a new Shot at the player's position with the calculated velocity
            shot = Shot(self.position.x, self.position.y, shot_velocity)
            # Reset the cooldown timer
            self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN
