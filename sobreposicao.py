import pygame 
from configs import * 

class Sobreposicao:
    def __init__(self,player):

        #Configuração geral 
        self.display_superficie =  pygame.display.get_surface()
        self.player = player 
        
        #importações 
        sobreposicao_path = 'PyDew-Valley/s3 - import/graphics/overlay/'
        self.ferramentas_surf = {ferramenta: pygame.image.load(f'{sobreposicao_path}{ferramenta}.png').convert_alpha() for ferramenta in player.ferramentas}
        self.sementes_surf = {sementes: pygame.image.load(f'{sobreposicao_path}{sementes}.png').convert_alpha() for sementes in player.sementes}

    def display(self):

        #Ferramentas 
        ferramenta_surf = self.ferramentas_surf[self.player.ferramenta_escolhida]
        ferramenta_rect = ferramenta_surf.get_rect(midbottom = SOBREPOSICOES['tool'])
        self.display_superficie.blit(ferramenta_surf,ferramenta_rect)
        
        # Sementes  
        semente_surf = self.sementes_surf[self.player.semente_escolhida]
        semente_rect = semente_surf.get_rect(midbottom = SOBREPOSICOES['seed'])
        self.display_superficie.blit(semente_surf,semente_rect) 