import pygame

class SpriteSheet():
    def __init__(self, image):
        self.sheet = image

    def play_image(self, frame, image_width, image_height):
        image = pygame.Surface((image_width, image_height), pygame.SRCALPHA).convert_alpha()
    
        image.blit(self.sheet, (0, 0), (frame * image_width, 0, image_width, image_height))
    
        image.set_colorkey((0, 0, 0))
    
        return image