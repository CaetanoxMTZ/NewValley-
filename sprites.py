import pygame 
from configs import * 

class G_neric(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups, z = CAMADAS['main']):
        super().__init__(groups)
        self.image = surf 
        self.rect = self.image.get_rect(topleft = pos)
        self.z = z
