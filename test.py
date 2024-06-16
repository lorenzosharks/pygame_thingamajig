import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load tank body and turret images
tank_body = pygame.Surface((100, 60), pygame.SRCALPHA)
tank_body.fill(WHITE)

tank_turret = pygame.Surface((50, 20), pygame.SRCALPHA)
tank_turret.fill(WHITE)

# Initial position and size of the tank body and turret
x, y = 100, 100
body_width, body_height = tank_body.get_size()
turret_width, turret_height = tank_turret.get_size()

# Main loop
running = True
angle = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Calculate the angle between the turret and the mouse cursor
    dx = mouse_x - (x + body_width // 2)
    dy = mouse_y - (y + body_height // 2)
    turret_angle = math.degrees(math.atan2(-dy, dx))

    # Clear screen
    screen.fill(BLACK)

    # Rotate the tank body
    rotated_body = pygame.transform.rotate(tank_body, angle)
    rotated_rect = rotated_body.get_rect(center=(x + body_width // 2, y + body_height // 2))

    # Rotate the turret to face the mouse cursor
    rotated_turret = pygame.transform.rotate(tank_turret, turret_angle)
    rotated_rect_turret = rotated_turret.get_rect(center=rotated_rect.center)

    # Draw the rotated images
    screen.blit(rotated_body, rotated_rect.topleft)
    screen.blit(rotated_turret, rotated_rect_turret.topleft)

    # Update the display
    pygame.display.flip()

    # Increment the angle for continuous rotation of the body (if needed)
    angle += 1

    # Cap the frame rate
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
