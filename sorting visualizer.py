import pygame
import random

pygame.init()

surface=pygame.display.set_mode((900,650))
pygame.display.set_caption("Sorting visuallizer")



gameLoop=True

while gameLoop:
    
    for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameLoop=False
            pygame.draw.rect(surface,(255,255,255),[random.randrange(1,100),20,20,20])

    surface.fill((0,0,0))
    pygame.draw.rect(surface,(255,255,255),[random.randrange(1,100),20,20,20])
    
    pygame.display.update()
pygame.quit()


    
