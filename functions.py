import pygame
import v 
import time


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


        for i in pygame.event.get():

            if i.type == pygame.QUIT:
                v.jogo = True



        print(v.jogo)
        
        pygame.display.update()

loop()
    
