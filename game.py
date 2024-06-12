# main.py

import pygame
from character import Character
from bordercontrol import border_control

rectangle = Character(100, 0, 0, 0, 0, 0)

print(rectangle.attack)

pygame.init()

player_image = pygame.image.load("actualskibidi.png")  # Replace "player.png" with the path to your image

smallerimage = pygame.transform.scale(player_image, (50, 50))

# sizing and coordinates
screenW = 1000
screenH = 800

sizeW = 50
sizeH = 50

# x = screenW / 2 - sizeW / 2
# y = screenH / 2 - sizeH / 2

# OGx = screenW / 2 - sizeW / 2
# OGy = screenH / 2 - sizeH / 2

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

while run:
    
    # keys pressing thingamajig
    key = pygame.key.get_pressed()
    if allowW:
        if key[pygame.K_w]:
            y = y-5
    if allowS:
        if key[pygame.K_s]:
            y = y+5
    if allowA:
        if key[pygame.K_a]:
            x = x-5
    if allowD:
        if key[pygame.K_d]: 
            x = x-5
    if key[pygame.K_r]:
        x = OGx
        y = OGy
    if allowed:
        if key[pygame.K_l]:
            health = health-5
        if health < screenW - 80:
            if key[pygame.K_p]:
                health = health+5

    if health < 0:
        health = 0
        allowed = False

    screen.fill("green")
    
    #player = pygame.draw.rect(screen, "purple", (x, y, sizeW, sizeH))
    screen.blit(smallerimage, (x, y))
    playerC1 = pygame.draw.rect(screen, "green", (x, y, 1, 1))
    playerC3 = pygame.draw.rect(screen, "purple", (x + sizeW, y + sizeH, 1, 1))










    # update collision detection
    allowA, allowW, allowD, allowS = border_control(playerC1, playerC3, screenW, screenH)











































    # health bar stuff
    healthbar = pygame.draw.rect(screen, "black", (35, 5, screenW - 70, 60))
    pygame.draw.rect(screen, "red", (40, 10, health, 50))
    font = pygame.font.Font(None, 36)
    text_surface = font.render(f"Skibidi's Health: {round(health/((screenW - 80)/100), 1)}", True, (255, 255, 255))
    screen.blit(text_surface, (screenW/2 - text_surface.get_width()/2, 20))

    # makes sure things are displayed well
    pygame.display.update()
    dt = clock.tick(60) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()
