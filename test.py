import pygame
import sys
import math

pygame.init()

# Load images
tank_body = pygame.image.load("better_body.png")  # Replace "tank.png" with the path to your image
tank_turret = pygame.image.load("better_turret.png")  # Replace "turret.png" with the path to your image
shell = pygame.image.load("bullet.png")

# Screen setup
pixels = pygame.display.Info()
screenW = pixels.current_w - 50
screenH = pixels.current_h - 50

sizeW = 50
sizeH = 100

x = screenW // 2 - tank_body.get_width() // 2
y = screenH // 2 - tank_body.get_height() // 2
OGx = screenW // 2 - tank_body.get_width() // 2
OGy = screenH // 2 - tank_body.get_height() // 2

health = screenW - 80

# Screen and clock setup
dt = 0
clock = pygame.time.Clock()
pygame.display.set_caption("Tank Game")
run = True
screen = pygame.display.set_mode((screenW, screenH))
allowed = True

# Debugging purposes
print(tank_body.get_width())
print(tank_body.get_height())

# Movement and rotation flags
allowW = True
allowS = True
allowA = True
allowD = True

# Initialize rotation angle
angle = 0
angle_radians = 0

# Turret rotation speed (degrees per second)
max_turret_rotation_speed = 60
current_turret_angle = 0
current_shell_angle = 0

# Miscellaneous (ie cheats)
actual_tankspeed = 2
tank_speed = 0
body_rotation_speed = 1
backward_speed = 1
muzzle_velocity = 10000
rounds = 79
reload_speed = 5000 # In milliseconds
tank_shell_reload_time = 1000 # In milliseconds

# Other flags
allowed_rotation = True
allowed_fire = True
disable_reload =False
tank_reload_time = False

# Other thingamajigs
velocity_x = 0
velocity_y = 0

# Reload logic
start_reload = None
reload = False
bruh = False

# Shell data structure
shells = []

# Normalize angles to the range [-180, 180]
def normalize_angle(angle):
    while angle <= -180:
        angle += 360
    while angle > 180:
        angle -= 360
    return angle

#Sprite sheet thing

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
clock = pygame.time.Clock()

while run:
    
    screen.fill("Green")  # Green background

    # Reload, shooting, and closing things
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
        if event.type == pygame.MOUSEBUTTONDOWN:
            if reload == False and allowed_fire == True:
                mouse_buttons = pygame.mouse.get_pressed()
                if mouse_buttons[0]:
                    turret_x = x + sizeW // 2
                    turret_y = y + sizeH // 2

                    # Calculate initial velocity components based on turret angle
                    velocity_x = muzzle_velocity * math.cos(math.radians(current_shell_angle))
                    velocity_y = -muzzle_velocity * math.sin(math.radians(current_shell_angle))
                    shells.append((turret_x, turret_y, current_shell_angle, velocity_x, velocity_y, pygame.time.get_ticks()))
                    reload = True
                    
                    if animation_complete:  # Reset animation if it was complete
                        i = 0
                        animation_complete = False
                    animation_started = True  # Start the animation

                    rounds -= 1                    

                    start_reload = pygame.time.get_ticks()
    
    if animation_started and not animation_complete:
        i = (i + 1) % 19  # Increment the frame counter and wrap around at 19
        # Check if animation is complete
        if i == 0:  # If i is 0, it means we have completed a full loop
            animation_complete = True  # Mark the animation as complete
            animation_started = False  # Stop the animation

    rotated_sprite = pygame.transform.rotate(sprite[i], current_turret_angle-90)
    rect = rotated_sprite.get_rect(center=(x + sizeW // 2, y + sizeH // 2))
    screen.blit(rotated_sprite, rect.topleft)


    if reload:
        current_time = pygame.time.get_ticks()
        elapsed_time_reload = current_time - start_reload

        if elapsed_time_reload >= reload_speed:
            reload = False

    if rounds <= 0:
        allowed_fire = False
    elif rounds > 0:
        allowed_fire = True

    if 0<rounds<79:
        disable_reload = False
    
    if rounds >= 79:
        disable_reload = True
    
    if rounds == 0:
        disable_reload = False

    # Key pressing
    key = pygame.key.get_pressed()

    if disable_reload == False and tank_reload_time == False:
        key_reload = pygame.key.get_pressed()
        if key_reload[pygame.K_b]:
            rounds += 1
            tank_start_reload_time = pygame.time.get_ticks()
            bruh = True
            tank_reload_time = True

    if bruh:
        bruh_current_time = pygame.time.get_ticks()
        bruh_elapsed_time_reload = bruh_current_time - tank_start_reload_time

        if bruh_elapsed_time_reload >= tank_shell_reload_time:
            tank_reload_time = False
            bruh = False

    if key[pygame.K_1]:
        allowed_rotation = False

    if key[pygame.K_2]:
        allowed_rotation = True
    
    if key[pygame.K_d]:
        angle -= body_rotation_speed  # Rotate counter-clockwise
        angle_radians -= math.radians(body_rotation_speed)
        current_turret_angle -= body_rotation_speed
        current_shell_angle -= body_rotation_speed

    if key[pygame.K_a]:
        angle += body_rotation_speed
        angle_radians += math.radians(body_rotation_speed)
        current_turret_angle += body_rotation_speed
        current_shell_angle += body_rotation_speed

    if allowW and key[pygame.K_w]:
        tank_speed = actual_tankspeed
        y -= tank_speed * math.cos(angle_radians)
        x -= tank_speed * math.sin(angle_radians)
    else:
        tank_speed = 0

    if allowS and key[pygame.K_s]:
        tank_speed = backward_speed
        y += backward_speed * math.cos(angle_radians)
        x += backward_speed * math.sin(angle_radians)
    else:
        tank_speed = 0

    if key[pygame.K_r]:
        x = OGx
        y = OGy
        angle_radians = 0
        angle = 0
        shells.clear()

    if health < 0:
        health = 0
        allowed = False

    if allowed:
        if key[pygame.K_l]:
            health -= 5
        if health < screenW - 80:
            if key[pygame.K_p]:
                health += 5

    #Screen logic
    if x < 0:
        x = 0
    elif x > screenW - sizeW:
        x = screenW - sizeW
    if y < 0:
        y = 0
    elif y > screenH - sizeH:
        y = screenH - sizeH

    #Turret lock
    if allowed_rotation:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        turret_x = x + sizeW // 2
        turret_y = y + sizeH // 2

        dx = mouse_x - turret_x
        dy = mouse_y - turret_y
        target_turret_angle = math.degrees(math.atan2(-dy, dx))
        target_shell_angle = target_turret_angle

        current_turret_angle = normalize_angle(current_turret_angle)
        target_turret_angle = normalize_angle(target_turret_angle)

        current_shell_angle = normalize_angle(current_shell_angle)
        target_shell_angle = normalize_angle(target_shell_angle)

        turret_angle_diff = target_turret_angle - current_turret_angle
        turret_angle_diff = normalize_angle(turret_angle_diff)

        shell_angle_diff = target_shell_angle - current_shell_angle
        shell_angle_diff = normalize_angle(shell_angle_diff)

        rotation_speed = max_turret_rotation_speed * dt

        if abs(turret_angle_diff) < rotation_speed:
            current_turret_angle = target_turret_angle
        elif turret_angle_diff > 0:
            current_turret_angle += rotation_speed
        else:
            current_turret_angle -= rotation_speed

        if abs(shell_angle_diff) < rotation_speed:
            current_shell_angle = target_shell_angle
        elif shell_angle_diff > 0:
            current_shell_angle += rotation_speed
        else:
            current_shell_angle -= rotation_speed

    # Rotations and whatnot
    rotated_body = pygame.transform.rotate(tank_body, angle)
    rotated_rect = rotated_body.get_rect(center=(x + sizeW // 2, y + sizeH // 2))

    #Shells
    rotated_shell = pygame.transform.rotate(shell, current_shell_angle - 90)
    rotated_rect_shell = rotated_shell.get_rect(center=(rotated_rect.centerx + 25, rotated_rect.centery + 25))

    #Turret
    rotated_turret = pygame.transform.rotate(tank_turret, current_turret_angle - 90)
    rotated_rect_turret = rotated_turret.get_rect(center=rotated_rect.center)
    
    #Turret animation
    
    # Update and draw shell positions
    shells_to_remove = []
    for i, shell_pos in enumerate(shells):
        turret_x, turret_y, shell_angle, velocity_x, velocity_y, start_time = shell_pos
        elapsed_time = pygame.time.get_ticks() - start_time

        # Update shell position based on velocity
        shell_x = turret_x + velocity_x * elapsed_time / 1000
        shell_y = turret_y + velocity_y * elapsed_time / 1000

        if elapsed_time > 5000:  # 5000 milliseconds = 5 seconds
            shells_to_remove.append(i)
        else:
            rotated_shell = pygame.transform.rotate(shell, shell_angle - 90)
            rotated_rect_shell = rotated_shell.get_rect(center=(shell_x, shell_y))
            screen.blit(rotated_shell, rotated_rect_shell.topleft)
    
    # Remove shells that have expired
    for index in sorted(shells_to_remove, reverse=True):
        del shells[index]

    # Draw the rotated images
    screen.blit(rotated_body, rotated_rect.topleft)
    screen.blit(rotated_turret, rotated_rect_turret.topleft)

    # Draw health bar
    healthbar = pygame.draw.rect(screen, (0, 0, 0), (35, 5, screenW - 70, 60))
    pygame.draw.rect(screen, (255, 0, 0), (40, 10, health, 50))
    font = pygame.font.Font(None, 36)
    text_surface = font.render(f"Tank Health: {round(health / ((screenW - 80) / 100), 1)}%", True, (255, 255, 255))
    screen.blit(text_surface, (screenW // 2 - text_surface.get_width() // 2, 20))

    # Rounds display
    number_of_rounds = font.render(f"Rounds: {rounds}", True, (255, 255, 255))
    ammo = pygame.draw.rect(screen, (0, 0, 0), (35, 70, 165, 60))
    screen.blit(number_of_rounds, (50, 87))


    pygame.display.flip()
    dt = clock.tick(animation_speed) / 1000

pygame.quit()
sys.exit()
