import pygame
from constants import *
from player import Player  # Import the Player class
from asteroid import Asteroid  # Import the Asteroid class
from asteroidfield import AsteroidField  # Import the AsteroidField class
from shot import Shot  # Import the Shot class

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Initialize Pygame
    pygame.init()

    # Create the game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Set the window title
    pygame.display.set_caption("Asteroids Game")

    # Create a clock object
    clock = pygame.time.Clock()

    # Initialize dt
    dt = 0

    # Create three groups: updatable, drawable, and asteroids
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Add the Player to both updatable and drawable groups
    Player.containers = (updatable, drawable)

    # Add Asteroid to asteroids, updatable, and drawable groups
    Asteroid.containers = (asteroids, updatable, drawable)

    # Set AsteroidField container to only updatable group
    AsteroidField.containers = (updatable,)
    
    Shot.containers = (shots, updatable, drawable)

    # Instantiate a Player object in the middle of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Create a new AsteroidField object
    asteroid_field = AsteroidField()

    # Game loop
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Fill the screen with black color
        screen.fill((0, 0, 0))  # RGB value for black

        # Control the frame rate and calculate delta time
        dt = clock.tick(60) / 1000.0  # Convert milliseconds to seconds

        # Update all updatable objects
        for updatable_object in updatable:
            updatable_object.update(dt)

        # Check for collisions between player and asteroids
        for asteroid in asteroids:
            if player.collision_check(asteroid):
                print("Game over!")
                return  # Exit the program immediately

        # Check for collisions between bullets and asteroids
        for asteroid in asteroids:
            for bullet in shots:
                if asteroid.collision_check(bullet):
                    asteroid.split()  # Call the split method instead of kill
                    bullet.kill()

        # Draw all drawable objects
        for drawable_object in drawable:
            drawable_object.draw(screen)

        # Refresh the display
        pygame.display.flip()


if __name__ == "__main__":
    main()
