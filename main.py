import pygame, sys
from configs import *
from level import Level



class Game:     #define a classe 
    def __init__(self):     #Seta a inicialização do jogo, display e relogio
        pygame.init()
        self.tela = pygame.display.set_mode((LARGURA_TELA,ALTURA_TELA)) #aqui se faz a tela 
        self.relogio = pygame.time.Clock() #aqui faz o relógio
        self.level = Level() #chama a classe Level 
        pygame.display.set_caption('Nutridew Valley') #aqui faz o título 
    
    def run(self): #Seta loop do jogo, define a opção de saída. 
        while True:
            for event in pygame.event.get():    #checando se há saída solicitada 
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            dt = self.relogio.tick() / 1000  #Delta time
            self.level.run(dt) 
            pygame.display.update()

if __name__ == "__main__":  #Checa se estamos na pasta principal 
    game = Game()   #criando objeto a partir da classe 
    game.run()  #chamando o método de inicialização, contém o loop principal do jogo. 

       