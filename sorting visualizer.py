import pygame
import random

pygame.init()

surface=pygame.display.set_mode((900,650))
pygame.display.set_caption("Sorting visuallizer")



#colors
red=(255,0,0)
blue=(0,0,255)
green=(0,255,0)
white=(255,255,255)
black=(0,0,0)
x=10
y=10
array=[0]*151
def arr_generate():
    for i in range(1,151):
        array[i]=random.randrange(1,151)
arr_generate()

def draw():
    element_width =(900-150)//150
    pygame.draw.line(surface, (0, 0, 0),  (0, 95), (900, 95), 6) 
    for i in range(1, 100): 
        pygame.draw.line(surface,black,(0, 5* i + 100),(900, 5* i + 100), 1)
    
    for  i in range(1, 151): 
        pygame.draw.line(surface, red,(6 * i-3, 100),(6* i-3, array[i]*5 + 100),element_width) 


    
gameLoop=True

while gameLoop:
    
    for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameLoop=False
    surface.fill(white)
    draw()
    y+=1
    pygame.display.update()
pygame.quit()



