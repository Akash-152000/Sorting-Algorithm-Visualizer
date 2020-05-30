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
grey=(211,211,211)
x=10
y=10
array=[0]*151
def arr_generate():
    for i in range(1,151):
        array[i]=random.randrange(1,151)
arr_generate()

def refill():
    surface.fill((255, 255, 255)) 
    draw() 
    pygame.display.update() 
    pygame.time.delay(20) 

def draw():
    element_width =(900-150)//150
    pygame.draw.line(surface, (0, 0, 0),  (0, 0), (900, 0), 6) 
    for i in range(1, 100): 
        pygame.draw.line(surface,grey,(0, 5.5* i),(900, 5.5* i), 1)
    
    for  i in range(1,151): 
        pygame.draw.line(surface, red,(6 * i-3,6),(6* i-3, array[i]*3 + 6),element_width-1) 



def merge(left,right):
    result=[]
    i,j=0,0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result+=left[i:]
    result+=right[j:]
    return result
        


def mergeSort(arr):
    mid=len(arr)//2
    if len(arr)==1:
        refill()
        return arr
    else:
        left=mergeSort(arr[:mid])
        right=mergeSort(arr[mid:])
        return merge(left,right)

    
gameLoop=True

while gameLoop:
    surface.fill(white)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gameLoop=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                mergeSort(array)
    
    draw()
    pygame.display.update()
pygame.quit()



