# main.py

import pygame
from character import Character
from bordercontrol import border_control
import math


rectangle = Character(100, 0, 0, 0, 0, 0)

tank_speed = 1

print(rectangle.attack)

pygame.init()

player_image = pygame.image.load("tank.png")  # Replace "player.png" with the path to your image

smallerimage = pygame.transform.scale(player_image, (50, 50))

# sizing and coordinates
screenW = 1000
screenH = 800

sizeW = 50
sizeH = 50

x = screenW // 2 - smallerimage.get_width() // 2
y = screenH // 2 - smallerimage.get_height() // 2
OGx = screenW // 2 - smallerimage.get_width() // 2
OGy = screenH // 2 - smallerimage.get_height() // 2

health = screenW - 80

# screen things
dt = 0
clock = pygame.time.Clock()
pygame.display.set_caption("Thing")
run = True
screen = pygame.display.set_mode((screenW, screenH))
allowed = True

# collision detection thing
allowW = True
allowS = True 
allowA = True
allowD = True

# Initialize rotation angle
angle = 0

while run:
    
    key = pygame.key.get_pressed()    
    if key[pygame.K_e]:
        angle -= 1  # Rotate counter-clockwise
    if key[pygame.K_q]:
        angle += 1  # Rotate clockwis
    if allowW and key[pygame.K_w]:
        y -= tank_speed
    if allowS and key[pygame.K_s]:
        y += tank_speed
    if allowA and key[pygame.K_a]:
        x -= tank_speed
    if allowD and key[pygame.K_d]:
        x += tank_speed
    if key[pygame.K_r]:
        x = OGx
        y = OGy
    if allowed:
        if key[pygame.K_l]:
            health -= 5
        if health < screenW - 80:
            if key[pygame.K_p]:
                health += 5

    if health < 0:
        health = 0
        allowed = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Rotate the image
    rotated_image = pygame.transform.rotate(smallerimage, angle)
    rotated_rect = rotated_image.get_rect(center=(x + sizeW // 2, y + sizeH // 2))

    screen.fill("green")

    # Draw the rotated image
    screen.blit(rotated_image, rotated_rect.topleft)
    playerC1 = pygame.draw.rect(screen, "green", (x, y, 1, 1))
    playerC3 = pygame.draw.rect(screen, "purple", (x + sizeW, y + sizeH, 1, 1))

    # Update collision detection
    allowA, allowW, allowD, allowS = border_control(playerC1, playerC3, screenW, screenH)

    # Health bar stuff
    healthbar = pygame.draw.rect(screen, "black", (35, 5, screenW - 70, 60))
    pygame.draw.rect(screen, "red", (40, 10, health, 50))
    font = pygame.font.Font(None, 36)
    text_surface = font.render(f"Tank Health: {round(health/((screenW - 80)/100), 1)}", True, (255, 255, 255))
    screen.blit(text_surface, (screenW/2 - text_surface.get_width()/2, 20))

    # Make sure things are displayed well
    pygame.display.update()
    dt = clock.tick(60) / 1000

pygame.quit()
