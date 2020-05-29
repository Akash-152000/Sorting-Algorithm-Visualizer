import pygame
import random

screen=pygame.display.set_mode((900,650))
pygame.display.set_caption("Sorting visuallizer")

pygame.init()

gameLoop=True

green=(0,204,102)
red=(255,0,0)
blue=(0,0,255)
yellow=(255,255,0)



array=[0]*151
arr_clr=[green]*151
color=[red,blue,yellow]

while gameLoop:
    
    for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameLoop=False

    surface.fill(black)
    pygame.display.flip()
pygame.quit()
    
