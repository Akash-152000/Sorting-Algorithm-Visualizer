import pygame
import pygame
import random
pygame.init()

surface=pygame.display.set_mode((900,700))
pygame.display.set_caption("Sorting visualizer")

#Colours
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
black=(0,0,0)
white=(255,255,255)

array=[0]*200

def generate_array():
    for i in range(1,200):
        array[i]=random.randrange(1,200)
generate_array()
#print(array)



gameLoop=True

while gameLoop:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gameLoop=False
    surface.fill(white)
    pygame.display.update()
pygame.quit()






