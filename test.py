import pygame
import sys
import random  # We'll use this to generate random positions

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Tank Shell Random Spawn')

# Load an image for the shell (make sure you have a shell.png in the working directory)
shell = pygame.Surface((20, 20))  # This is a placeholder for an actual image
shell.fill((255, 0, 0))  # Fill it with red color to differentiate

# Define the tank shell class
class tank_shell(pygame.sprite.Sprite):
    def __init__(self, x, y, velocity=0):
        super().__init__()
        self.image = shell
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.velocity = velocity

    def clone(self, x, y):
        return tank_shell(x, y, self.velocity)

# Create an initial tank shell to clone from
initial_shell = tank_shell(100, 100)

# Create a sprite group to manage tank shells
all_sprites = pygame.sprite.Group()
all_sprites.add(initial_shell)

# Main loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Get the mouse button state
            mouse_buttons = pygame.mouse.get_pressed()
            
            # Check for left mouse button click
            if mouse_buttons[0]:
                # Generate random x and y coordinates
                random_x = random.randint(0, screen_width - shell.get_width())
                random_y = random.randint(0, screen_height - shell.get_height())
                
                # Clone the initial shell at the random position
                cloned_shell = initial_shell.clone(random_x, random_y)
                
                # Add the cloned shell to the sprite group
                all_sprites.add(cloned_shell)
                
                print(f"Left click at {event.pos}. Shell cloned at ({random_x}, {random_y})")

    # Clear the screen
    screen.fill((255, 255, 255))

    # Update and draw all sprites
    all_sprites.update()
    all_sprites.draw(screen)

    # Update the display
    pygame.display.flip()

# Clean up
pygame.quit()
sys.exit()
