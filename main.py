import pygame
from constants import *

def main():
    # Initialize Pygame
    pygame.init()
    
    # Create the game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Set the window title
    pygame.display.set_caption("Asteroids Game")
    
    # Game loop
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Fill the screen with black color
        screen.fill((0, 0, 0))  # RGB value for black
        
        # Refresh the display
        pygame.display.flip()
    
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()