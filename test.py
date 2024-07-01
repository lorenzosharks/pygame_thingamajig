import pygame

# Initialize Pygame
pygame.init()

def load_spritesheet(spritesheet_path, sprite_width):
    # Load the spritesheet image
    spritesheet_image = pygame.image.load(spritesheet_path)
    
    # Calculate the number of sprites in the image
    num_sprites = spritesheet_image.get_width() // sprite_width
    
    # Create a list to hold each sprite (like a Pokemon collection, but cooler)
    sprites = []
    for i in range(num_sprites):
        sprite = spritesheet_image.subsurface((i * sprite_width, 0, sprite_width, spritesheet_image.get_height()))
        sprites.append(sprite)
    
    return sprites

def get_next_sprite(sprites, current_sprite):
    # Update the current sprite index (like flipping through comic book pages)
    current_sprite = (current_sprite + 1) % len(sprites)
    return sprites[current_sprite], current_sprite

# Game setup
screen = pygame.display.set_mode((800, 600))
spritesheet_path = 'better_turret_sprite_sheet.png'
sprite_width = 50
animation_speed = 10  # Adjust as needed

# Load sprites
sprites = load_spritesheet('better_turret_sprite_sheet.png', sprite_width)
current_sprite = 0
animation_clock = pygame.time.Clock()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the next sprite
    sprite, current_sprite = get_next_sprite(sprites, current_sprite)
    
    # Clear the screen
    screen.fill((0, 0, 0))
    
    # Draw the current sprite (like a kid showing off their favorite toy)
    screen.blit(sprite, (375, 275))
    
    # Update the display
    pygame.display.flip()
    
    # Control the animation speed (like a chill DJ spinning tracks)
    animation_clock.tick(animation_speed)

pygame.quit()
