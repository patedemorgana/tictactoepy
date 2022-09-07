import pygame

jogo = False

width = 500
height = 400
margem = 5

xo = 'x'

vencedor = None
empate = None

b = (0, 0 , 0)
w = (255, 255, 255)

tabuleiro = [[None]*3, [None]*3, [None]*3]
malha = []

tela = pygame.display.set_mode((width, height))

pos = pygame.mouse.get_pos()
coluna = pos [0] // (width + margem)
linha = pos [1] // (height + margem)