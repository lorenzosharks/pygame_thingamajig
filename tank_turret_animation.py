import pygame
import sys

def run_spritesheet_animation(image_path, sprite_width, x, y, angle):


    # Load the spritesheet image
    spritesheet_image = pygame.image.load(image_path)

    # Dimensions of each sprite
    sprite_height = spritesheet_image.get_height()

    # Calculate the number of sprites in the image
    num_sprites = spritesheet_image.get_width() // sprite_width

    # Create a list to hold each sprite
    sprites = []
    for i in range(num_sprites):
        sprite = spritesheet_image.subsurface((i * sprite_width, 0, sprite_width, sprite_height))
        sprites.append(sprite)

    # Animation settings
    current_sprite = 0
    clock = pygame.time.Clock()


# Usage example:
run_spritesheet_animation('better_turret_sprite_sheet.png', 50, 250, 250, 1000)
