# main.py
import pygame
from character import Character
import math

rectangle = Character(100, 0, 0, 0, 0, 0)

print(rectangle.attack)

pygame.init()

player_image = pygame.image.load("tank.png")  # Replace "player.png" with the path to your image

player_image = pygame.transform.scale(player_image, (50, 50))

# sizing and coordinates
screenW = 1000
screenH = 800

sizeW = 50
sizeH = 50

x = screenW // 2 - player_image.get_width() // 2
y = screenH // 2 - player_image.get_height() // 2
OGx = screenW // 2 - player_image.get_width() // 2
OGy = screenH // 2 - player_image.get_height() // 2

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
angle_radians = 0

# miscellneos (ie cheats)
actual_tankspeed = 5
tank_speed = 0 # dont change this fella
rotation_speed = 5
backward_speed = 1

while run:
    
    screen.fill("green")

    key = pygame.key.get_pressed()    
    
    if key[pygame.K_d]:
        angle -= rotation_speed  # Rotate counter-clockwise
        angle_radians -= math.radians(rotation_speed)

    if key[pygame.K_a]:
        angle += rotation_speed
        angle_radians += math.radians(rotation_speed)

    if allowW and key[pygame.K_w]:
        tank_speed = actual_tankspeed
        y -= tank_speed*math.cos(angle_radians)
        x -= tank_speed*math.sin(angle_radians)
    else:
        tank_speed = 0

    if allowS and key[pygame.K_s]:
        tank_speed = backward_speed
        y += backward_speed*math.cos(angle_radians)
        x += backward_speed*math.sin(angle_radians)
    else:
        tank_speed = 0

    if key[pygame.K_r]:
        x = OGx
        y = OGy
        angle_radians = 0
        angle = 0

    if health < 0:
        health = 0
        allowed = False
    
    if allowed:
        if key[pygame.K_l]:
            health -= 5
        if health < screenW - 80:
            if key[pygame.K_p]:
                health += 5
                
    # if allowW and key[pygame.K_w]:
    #     y -= tank_speed
    
    # if allowS and key[pygame.K_s]:
    #     y += tank_speed
    
    # if allowA and key[pygame.K_a]:
    #     x -= tank_speed
    
    # if allowD and key[pygame.K_d]:
    #     x += tank_speed
    
    playerC1 = pygame.draw.rect(screen, "purple", (x, y, 1, 1))
    playerC2 = pygame.draw.rect(screen, "purple", (x + sizeW, y, 1, 1))
    playerC3 = pygame.draw.rect(screen, "purple", (x + sizeW, y + sizeH, 1, 1))
    playerC4 = pygame.draw.rect(screen, "purple", (x, y + sizeH, 1, 1))
    
    # Update collision detection
    if x < 0:
        x = 0
    elif x > screenW - sizeW:
        x = screenW - sizeW
    if y < 0:
        y = 0
    elif y > screenH - sizeH:
        y = screenH - sizeH

    # Rotate the image
    rotated_image = pygame.transform.rotate(player_image, angle)
    rotated_rect = rotated_image.get_rect(center=(x + sizeW // 2, y + sizeH // 2))


    # Draw the rotated image
    screen.blit(rotated_image, rotated_rect.topleft)

    # Health bar stuff
    healthbar = pygame.draw.rect(screen, "black", (35, 5, screenW - 70, 60))
    pygame.draw.rect(screen, "red", (40, 10, health, 50))
    font = pygame.font.Font(None, 36)
    text_surface = font.render(f"Tank Health: {round(health/((screenW - 80)/100), 1)}", True, (255, 255, 255))
    screen.blit(text_surface, (screenW/2 - text_surface.get_width()/2, 20))

    # Make sure things are displayed well
    pygame.display.update()
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


pygame.quit()
