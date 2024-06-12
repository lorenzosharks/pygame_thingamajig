import pygame

def handle_key_presses(allowW, allowS, allowA, allowD, allowed, x, y, OGx, OGy, health, screenW):
    key = pygame.key.get_pressed()
    
    if allowW and key[pygame.K_w]:
        y -= 5
        
    if allowS and key[pygame.K_s]:
        y += 5
        
    if allowA and key[pygame.K_a]:
        x -= 5
        
    if allowD and key[pygame.K_d]:
        x += 5
        
    if key[pygame.K_r]:
        x = OGx
        y = OGy
        
    if allowed:
        if key[pygame.K_l]:
            health -= 5
        if health < screenW - 80:
            if key[pygame.K_p]:
                health += 5

    return x, y, health
