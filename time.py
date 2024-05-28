import pygame
import sys

pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Collision Detection Example")

# Define two rectangles as objects
rect1 = pygame.Rect(100, 100, 50, 50)
rect2 = pygame.Rect(200, 200, 50, 50)

# Define initial velocities for the objects
velocity1 = [2, 2]
velocity2 = [-2, -2]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update the positions of the objects
    rect1 = rect1.move(velocity1)
    rect2 = rect2.move(velocity2)

    # Check for collisions
    if rect1.colliderect(rect2):
        # Handle the collision (e.g., slow down the objects)
        velocity1 = [v * 0.5 for v in velocity1]
        velocity2 = [v * 0.5 for v in velocity2]

    # Draw the objects on the screen
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (255, 0, 0), rect1)
    pygame.draw.rect(screen, (0, 0, 255), rect2)
    pygame.display.flip()
