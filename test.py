import pygame

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# Colors
green = pygame.Surface((10, 10))
green.fill((0, 255, 0))

purple = pygame.Surface((10, 10))
purple.fill((128, 0, 128))

# Coordinates
x, y = 100, 100
sizeW, sizeH = 50, 50

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Blit the colored rectangles (1x1 pixel)
    screen.blit(green, (x, y))
    screen.blit(purple, (x + sizeW, y + sizeH))

    # Update the display
    pygame.display.flip()

pygame.quit()
