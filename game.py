# main.py
import pygame
from character import Character
import math

rectangle = Character(100, 0, 0, 0, 0, 0)

print(rectangle.attack)

pygame.init()

tank_body = pygame.image.load("tank.png")  # Replace "tank.png" with the path to your image
tank_turret = pygame.image.load("turret.png")  # Replace "turret.png" with the path to your image
shell = pygame.image.load("bullet.png")

# Sizing and coordinates
pixels = pygame.display.Info()
screenW = pixels.current_w - 50
screenH = pixels.current_h - 50

sizeW = 50
sizeH = 50

x = screenW // 2 - tank_body.get_width() // 2
y = screenH // 2 - tank_body.get_height() // 2
OGx = screenW // 2 - tank_body.get_width() // 2
OGy = screenH // 2 - tank_body.get_height() // 2

health = screenW - 80

# Screen things
dt = 0
clock = pygame.time.Clock()
pygame.display.set_caption("Thing")
run = True
screen = pygame.display.set_mode((screenW, screenH))
allowed = True

# Collision detection thing
allowW = True
allowS = True
allowA = True
allowD = True

# Initialize rotation angle
angle = 0
angle_radians = 0

# Turret rotation speed (degrees per second)
max_turret_rotation_speed = 40
current_turret_angle = 0
current_shell_angle = 0

# Miscellaneous (ie cheats)
actual_tankspeed = 2
tank_speed = 0  # Don't change this fella
body_rotation_speed = 1
backward_speed = 1

#Other things
allowed_rotation = True

# Normalize angles to the range [-180, 180]
def normalize_angle(angle):
    while angle <= -180:
        angle += 360
    while angle > 180:
        angle -= 360
    return angle

while run:
    
    screen.fill("green")

    key = pygame.key.get_pressed()

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

    if health < 0:
        health = 0
        allowed = False

    if allowed:
        if key[pygame.K_l]:
            health -= 5
        if health < screenW - 80:
            if key[pygame.K_p]:
                health += 5

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
    rotated_body = pygame.transform.rotate(tank_body, angle)
    rotated_rect = rotated_body.get_rect(center=(x + sizeW // 2, y + sizeH // 2))

    # Get mouse position
    if allowed_rotation == True:
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Calculate the center of the turret body
        turret_x = x + sizeW // 2
        turret_y = y + sizeH // 2

        shell_x = x +sizeW // 2
        shell_y = y +sizeH // 2

        # Calculate the angle between the turret and the mouse cursor using atan2
        dx = mouse_x - turret_x
        dy = mouse_y - turret_y
        target_turret_angle = math.degrees(math.atan2(-dy, dx))

        dsx = shell_x - turret_x
        dsy = shell_y - turret_y
        target_shell_angle = math.degrees(math.atan2(-dy, dx))

        # Normalize the current and target turret angles (no idea what this does)
        current_turret_angle = normalize_angle(current_turret_angle)
        target_turret_angle = normalize_angle(target_turret_angle)

        current_shell_angle = normalize_angle(current_shell_angle)
        target_shell_angle = normalize_angle(target_shell_angle)

        # Calculate the difference between the target angle and the current angle
        turret_angle_diff = target_turret_angle - current_turret_angle
        turret_angle_diff = normalize_angle(turret_angle_diff)

        shell_angle_diff = target_shell_angle - current_shell_angle
        shell_angle_diff = normalize_angle(shell_angle_diff)

        # Calculate the amount to rotate this frame (no idea what this does either)
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

    # Rotating the shell and turret
    rotated_shell = pygame.transform.rotate(shell, current_shell_angle - 90)
    rotated_rect_shell = rotated_shell.get_rect(center=rotated_rect.center)

    rotated_turret = pygame.transform.rotate(tank_turret, current_turret_angle - 90)
    rotated_rect_turret = rotated_turret.get_rect(center=rotated_rect.center)

    # Draw the rotated images
    screen.blit(rotated_body, rotated_rect.topleft)
    screen.blit(rotated_shell, rotated_rect_shell.topleft)
    screen.blit(rotated_turret, rotated_rect_turret.topleft)


    playerC1 = pygame.draw.rect(screen, "green", (x, y, 1, 1))
    playerC2 = pygame.draw.rect(screen, "green", (x + sizeW, y, 1, 1))
    playerC3 = pygame.draw.rect(screen, "green", (x + sizeW, y + sizeH, 1, 1))
    playerC4 = pygame.draw.rect(screen, "green", (x, y + sizeH, 1, 1))

    # Health bar stuff
    healthbar = pygame.draw.rect(screen, "black", (35, 5, screenW - 70, 60))
    pygame.draw.rect(screen, "red", (40, 10, health, 50))
    font = pygame.font.Font(None, 36)
    text_surface = font.render(f"Tank Health: {round(health / ((screenW - 80) / 100), 1)}", True, (255, 255, 255))
    screen.blit(text_surface, (screenW / 2 - text_surface.get_width() / 2, 20))


    # Make sure things are displayed well
    pygame.display.update()
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()