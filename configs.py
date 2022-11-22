from pygame.math import Vector2

#tela 
LARGURA_TELA = 1280
ALTURA_TELA = 720
TAMANHO_TITULO = 60

#Posições das sobreposições, definições de deslocamento e camadas.

SOBREPOSICOES = {
    'tool' : (40, ALTURA_TELA - 15),
    'seed' : (70, ALTURA_TELA - 5)}

FERRAMENTAS_DESLOCAMENTO_PLAYER = {
    'left' : Vector2(-50, 40),
    'right' : Vector2(50, 50),
    'up' : Vector2(0, -10),
    'down': Vector2(0, 50)
}

CAMADAS = {
    'water': 0,
    'ground': 1,
    'soil': 2, 
    'soil water': 3,
    'rain floor': 4,
    'house bottom': 5,
    'ground plant': 6,
    'main': 7,
    'house top': 8,
    'fruit': 9,
    'rain drops': 10,

}

MACA_POS = {
    'Small': [(18,17), (30,37), (12,50), (30,45), (20,30), (30,10)],
    'Large': [(30,24), (60,65), (50,50), (16,40), (45,50), (42,70)]
}

TEMPO_COLHEITA = {
    'corn': 1,
    'tomato': 0.7
}

PRECO_VENDA = {
    'wood': 4,
    'apple': 2,
    'corn': 10,
    'tomato': 20
}

PRECO_COMPRA =  {
    'corn': 4,
    'tomato': 5
}

