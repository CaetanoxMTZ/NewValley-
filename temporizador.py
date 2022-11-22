import pygame

class Temporizador:
    def __init__(self,duration,func = None):
         self.duracao = duration
         self.func = func 
         self.tempo_inicial= 0
         self.ativo = False
    
    def ativacao(self):
        self.ativo  = True
        self.tempo_inicial = pygame.time.get_ticks()

    def desativar(self):
        self.ativo = False
        self.tempo_inicial = 0

    def atualiza(self):
        h_atual = pygame.time.get_ticks()
        if h_atual - self.tempo_inicial >= self.duracao:
            self.desativar() 
            if self.func:
                self.func()