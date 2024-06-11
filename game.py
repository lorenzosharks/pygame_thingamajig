#random things
import pygame
from character import Character

rectangle = Character(100, 0, 0, 0, 0, 0)

print(rectangle.attack)

pygame.init()

#player_image = pygame.image.load("")  # Replace "player.png" with the path to your image

#sizing and coordinates
screenW = 1000
screenH = 800

sizeW = 50
sizeH = 50

x = screenW/2 - sizeW/2
y = screenH/2 - sizeH/2

OGx = screenW/2 - sizeW/2
OGy = screenH/2 - sizeH/2

#x = screenW // 2 - player_image.get_width() // 2
#y = screenH // 2 - player_image.get_height() // 2

#OGx = screenW // 2 - player_image.get_width() // 2
#OGy = screenH // 2 - player_image.get_height() // 2


health = screenW-80

#screen things
dt = 0
clock = pygame.time.Clock()
pygame.display.set_caption("Thing")
run = True
screen = pygame.display.set_mode((screenW, screenH))
allowed = True


while run:
    #keys pressing thingamajig
    key = pygame.key.get_pressed()

    if key[pygame.K_w]:
        y = y-5
    if key[pygame.K_s]:
        y = y+5
    if key[pygame.K_a]:
        x = x-5
    if key[pygame.K_d]:
        x = x+5
    if key[pygame.K_r]:
        x = OGx
        y = OGy
    if allowed == True:
        if key[pygame.K_l]:
            health = health-5
        if health < screenW-80:
            if key[pygame.K_p]:
                health = health+5

    if health < 0:
        health = 0
        allowed = False


    screen.fill("green")

    pygame.draw.rect(screen, "purple", (x ,y, sizeW, sizeH))

    # screen.blit(player_image, (x, y))


    #health bar
    pygame.draw.rect(screen, "black", (35 ,5, screenW-70, 60))

    pygame.draw.rect(screen, "red", (40 , 10, health, 50))


    font = pygame.font.Font(None, 36)

    text_surface = font.render(f"Health: {round(health/((screenW-80)/100), 1)}", True, (255, 255, 255))
    
    screen.blit(text_surface, (screenW/2 - text_surface.get_width()/2, 20))

    #makes sure things are displayed well
    pygame.display.update()
    dt = clock.tick(60) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()
