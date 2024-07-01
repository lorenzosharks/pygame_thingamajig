import pygame

def turret_fire():
    #Sprite sheet thing
    
    current_sprite = 18
    animation_clock = pygame.time.Clock()
    animation_speed = 10 
    animation_complete = True
    
    # Load the spritesheet image
    spritesheet_image = pygame.image.load('better_turret_sprite_sheet.png')
    
    # Dimensions of each sprite
    sprite_height = spritesheet_image.get_height()
    
    # Calculate the number of sprites in the image
    num_sprites = spritesheet_image.get_width() // 50
    
    # Create a list to hold each sprite
    sprites = []
    for i in range(num_sprites):
        sprite = spritesheet_image.subsurface((i * 50, 0, 50, sprite_height))
        sprites.append(sprite)
    
    current_sprite = (current_sprite + 1) % num_sprites
    
    return current_sprite

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    sprites = turret_fire()
    
    rotated_sprite = pygame.transform.rotate(sprites, 90)

    rotated_rect_sprite = rotated_sprite.get_rect(center=(300, 300))


    # Draw rotated sprite

    screen.blit(rotated_sprite, rotated_rect_sprite.topleft)




    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()