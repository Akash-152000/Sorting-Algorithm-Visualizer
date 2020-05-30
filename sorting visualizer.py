import pygame
import random
pygame.init()

surface=pygame.display.set_mode((900,700))
pygame.display.set_caption("Sorting visualizer")

#Colours
red=(255,99,71)
green=(0,255,0)
blue=(0,0,255)
black=(0,0,0)
white=(255,255,255)
grey=(211,211,211)

array=[0]*200

def generate_array():
    for i in range(1,200):
        array[i]=random.randrange(1,200)
generate_array()
#print(array)


##This Function draws 3 types of lines 
def draw_lines():
    #Horizontal grey lines
    for i in range(1,150):
        pygame.draw.line(surface,grey,(0,5*i),(900,5*i),1)

    for i in range(1,200):
        pygame.draw.line(surface,red,(5*i,6),(5*i,array[i]*3),3)
    pygame.draw.line(surface,black,(0,0),(900,0),10)

##Sorting algorithm
def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
                draw_lines()

    
gameLoop=True
while gameLoop:
    surface.fill(white)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gameLoop=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                bubbleSort(array)

    draw_lines()
    pygame.display.update()
pygame.quit()






