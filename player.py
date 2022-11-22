import pygame
from configs import *
from suporte import *
from temporizador import Temporizador

class Player(pygame.sprite.Sprite):
    
    def __init__(self, pos, group):
        super().__init__(group)

        self.import_assets()
        self.status = 'down_idle'
        self.frame_index = 0

        #definições gerais 
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center = pos)
        self.z = CAMADAS['main']

        #atributos de movimento
        self.direcao = pygame.math.Vector2()    #direção
        self.pos = pygame.math.Vector2(self.rect.center)    #posição
        self.velocidade = 200   #velocidade de movimento 

        #Cronometros 
        self.temporizadores = {
            'usa ferramenta': Temporizador(350,self.usa_ferramenta),
            'troca ferramenta': Temporizador(200),
            'usa semente': Temporizador(350, self.usa_semente),
            'troca semente': Temporizador(200)
        }
        #Ferramentas do jogador
        self.ferramentas = ['hoe', 'axe', 'water'] 
        self.index_fe = 0
        self.ferramenta_escolhida = self.ferramentas[self.index_fe]

        #Sementes 
        self.sementes = ['corn', 'tomato']
        self.semente_index = 0
        self.semente_escolhida = self.sementes[self.semente_index]

    def usa_ferramenta(self):
        pass
    
    def usa_semente(self):
        pass


    def import_assets(self): #importando os gráficos do jogo conforme ação realizada, no dicionário
        self.animations = {'up': [], 'down': [], 'left': [], 'right': [],
                            'right_idle':[], 'left_idle':[], 'up_idle':[], 'down_idle':[],
                            'right_hoe':[], 'left_hoe':[], 'up_hoe':[], 'down_hoe':[],
                            'right_axe':[], 'left_axe':[], 'up_axe':[], 'down_axe':[],
                            'right_water':[], 'left_water':[], 'up_water':[], 'down_water':[]}
        
        for animation in self.animations.keys():
            full_path = 'PyDew-Valley/s3 - import/graphics/character/' + animation
            self.animations[animation] = import_folder(full_path)
            print(self.animations)

    def anima(self,dt): #faz a animação da sprite do jogador 
        self.frame_index += 4 * dt      #percorre os arquivos dentro das paginas
        if self.frame_index >= len(self.animations[self.status]): 
            self.frame_index = 0

        self.image = self.animations[self.status][int(self.frame_index)]
    
    def input(self):    #faz controle direcional do movimento e define chave q executa o mesmo. 
        chaves = pygame.key.get_pressed()

        if not self.temporizadores['usa ferramenta'].ativo:
            if chaves[pygame.K_UP]:
                self.direcao.y = -1
                self.status = 'up'
            elif chaves[pygame.K_DOWN]:
                self.direcao.y = 1
                self.status = 'down'
            else: 
                self.direcao.y = 0

            if chaves[pygame.K_RIGHT]:
                self.direcao.x = 1
                self.status = 'right'
            elif chaves[pygame.K_LEFT]:
                self.direcao.x = -1
                self.status = 'left'
            else: 
                self.direcao.x = 0
            
            # Uso de ferramentas 

            if chaves[pygame.K_SPACE]:
                self.temporizadores['usa ferramenta'].ativacao()
                self.direcao = pygame.math.Vector2()
                self.frame_index = 0
           
            # Troca de ferramentas
            if chaves[pygame.K_q] and not self.temporizadores['troca ferramenta'].ativo:
                self.temporizadores['troca ferramenta'].ativacao()
                self.index_fe += 1
                self.index_fe = self.index_fe if self.index_fe < len(self.ferramentas) else 0
                self.ferramenta_escolhida = self.ferramentas[self.index_fe]

            #Uso da semente
            if chaves[pygame.K_LCTRL]:
                self.temporizadores['troca semente'].ativacao()
                self.direcao = pygame.math.Vector2()
                self.frame_index = 0
            #Troca da semente
            if chaves[pygame.K_e] and not self.temporizadores['troca semente'].ativo:
                self.temporizadores['troca semente'].ativacao()
                self.semente_index += 1
                self.semente_index = self.semente_index if self.semente_index < len(self.sementes) else 0
                self.semente_escolhida = self.sementes[self.semente_index]

    def atualiza_temporizadores(self):  #Atualiza os temporizadores para não ficar em loop eterno durante animação da ferramenta
        for temporizador in self.temporizadores.values():
            temporizador.atualiza()

    def get_status(self):   #checa se o jogador não está se movendo. 

        if self.direcao.magnitude() == 0:
            #adiciona string "_idle" ao status e evita erro de concatenação
            self.status = self.status.split('_')[0] +'_idle'

        # Uso de ferramentas
        if self.temporizadores['usa ferramenta'].ativo:
            self.status = self.status.split('_')[0] +'_' +self.ferramenta_escolhida

    def move(self,dt):
        #normalizando o vetor
        if self.direcao.magnitude() > 0:
            self.direcao = self.direcao.normalize()

        #movimento  vertical
        self.pos.x += self.direcao.x * self.velocidade * dt
        self.rect.centerx = self.pos.x

        #movimento  horizontal
        self.pos.y += self.direcao.y * self.velocidade * dt
        self.rect.centery = self.pos.y

    def update(self, dt): #mantém atualizado com o Delta time
        self.input()
        self.get_status()
        self.atualiza_temporizadores()
        self.move(dt)
        self.anima(dt)