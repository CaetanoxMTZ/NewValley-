import pygame
from configs import *
from player import Player
from sobreposicao import Sobreposicao
from sprites import G_neric

class Level:
    def __init__(self):
        self.display_superficie = pygame.display.get_surface() #Chama o display da superficie 

        #Grupamento de Sprites
        self.todas_sprites = CameraGroup() #sprites são elementos estáticos ou movéis dentro do jogo, como árvores, casas, e o character em si

        self.setup()
        self.sobreposicao = Sobreposicao(self.player)
   
    def setup(self):
        G_neric(
            pos = (0,0),
            surf = pygame.image.load('PyDew-Valley/s3 - import/graphics/world/ground.png').convert_alpha(),
            groups = self.todas_sprites, z = CAMADAS['ground'])
        self.player = Player((640,360), self.todas_sprites)

    def run(self,dt):   #definições de background e update constante das sprites
        self.display_superficie.fill('black')
        self.todas_sprites.customize_draw()
        self.todas_sprites.update(dt)
        self.sobreposicao.display()

class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_superficie = pygame.display.get_surface()

    def customize_draw(self):
        for sprite in self.sprites():
            self.display_superficie.blit(sprite.image, sprite.rect)