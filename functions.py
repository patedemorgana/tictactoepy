import pygame
import v 
import time

for linha in range(10):
    v.malha.append([])
    for v.coluna in range(10):
        v.malha[v.linha].append(0)

pygame.init()
pygame.display.set_caption("joguin da veia")

def loop():
    v.tela.fill(v.w)
    while not v.jogo:

        pygame.display.update()    
        for i in pygame.event.get():
            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_q:
                    v.jogo = True
            elif i.type == pygame.MOUSEBUTTONDOWN:  
                v.malha[v.linha][v.coluna] = 1
                print("Clicado,", v.pos, "Coordenadas:", v.linha, v.coluna)
        v.tela.fill(w)



        
        
        pygame.display.update()

loop()
    
