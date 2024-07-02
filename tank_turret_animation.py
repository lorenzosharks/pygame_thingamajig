import pygame
import math

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

# Load sprites
sprite = [
    pygame.image.load("turret_frame/frame_1.png"),
    pygame.image.load("turret_frame/frame_2.png"),
    pygame.image.load("turret_frame/frame_3.png"),
    pygame.image.load("turret_frame/frame_4.png"),
    pygame.image.load("turret_frame/frame_5.png"),
    pygame.image.load("turret_frame/frame_6.png"),
    pygame.image.load("turret_frame/frame_7.png"),
    pygame.image.load("turret_frame/frame_8.png"),
    pygame.image.load("turret_frame/frame_9.png"),
    pygame.image.load("turret_frame/frame_10.png"),
    pygame.image.load("turret_frame/frame_11.png"),
    pygame.image.load("turret_frame/frame_12.png"),
    pygame.image.load("turret_frame/frame_13.png"),
    pygame.image.load("turret_frame/frame_14.png"),
    pygame.image.load("turret_frame/frame_15.png"),
    pygame.image.load("turret_frame/frame_16.png"),
    pygame.image.load("turret_frame/frame_17.png"),
    pygame.image.load("turret_frame/frame_18.png"),
    pygame.image.load("turret_frame/frame_19.png"),
]

i = 0
animation_complete = False
animation_started = False
animation_speed = 60  # Control the speed of the animation (frames per second)

# Turret base position
y=0
x=0
# Game loop
running = True
while running:
    turret_position = (x, y)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.MOUSEBUTTONDOWN:  # Check if a mouse button is pressed down
            mouse_buttons = pygame.mouse.get_pressed()  # Get the state of all mouse buttons
            if mouse_buttons[0]:  # Check if the left mouse button is pressed
                if animation_complete:  # Reset animation if it was complete
                    i = 0
                    animation_complete = False
                animation_started = True  # Start the animation

    if animation_started and not animation_complete:
        i = (i + 1) % 19  # Increment the frame counter and wrap around at 19
        # Check if animation is complete
        if i == 0:  # If i is 0, it means we have completed a full loop
            animation_complete = True  # Mark the animation as complete
            animation_started = False  # Stop the animation

    key = pygame.key.get_pressed()

    if key[pygame.K_w]:
        tank_speed = 10
        y -= tank_speed * math.cos(45)
        x -= tank_speed * math.sin(45)
    else:
        tank_speed = 0

    if key[pygame.K_s]:
        tank_speed = 5
        y += 5 * math.cos(45)
        x += 5 * math.sin(45)
    else:
        tank_speed = 0



    # Get mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()
    
    # Calculate angle between turret and mouse position
    rel_x, rel_y = mouse_x - turret_position[0], mouse_y - turret_position[1]
    angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)

    # Rotate the current sprite
    rotated_sprite = pygame.transform.rotate(sprite[i], angle-90)

    # Clear the screen
    screen.fill("White")
    
    # Draw the current rotated sprite
    rect = rotated_sprite.get_rect(center=turret_position)
    screen.blit(rotated_sprite, rect.topleft)
    
    # Update the display
    pygame.display.flip()
    
    # Control the animation speed
    clock.tick(animation_speed)

pygame.quit()
