import pygame
import random
pygame.init()


surface=pygame.display.set_mode((1200,600))
pygame.display.set_caption("Sorting visualizer")

#Colours
red=(255,99,71)
green=(0,204,104)
blue=(0,0,255)
black=(0,0,0)
orange=(255,104,0)
white=(255,255,255)
grey=(180,180,180)
color_array=[orange]*150
array=[0]*150


#Generates new array every time you press r on your keyboard.
def generate_array():
    for i in range(1,150):
        color_array[i]=orange
        array[i]=random.randrange(1,150)
generate_array()

def redraw():
    surface.fill(white)
    draw_lines()
    pygame.display.update()


##This Function draws 3 types of lines 
def draw_lines():
    #Horizontal grey lines
    for i in range(1,150):
        pygame.draw.line(surface,grey,(0,5*i),(900,5*i),1)

    for i in range(1,150):
        pygame.draw.line(surface,color_array[i],(6*i,6),(6*i,array[i]*3),5)
    pygame.draw.rect(surface,grey,(900,0,400,600))
    pygame.draw.rect(surface, red, button1)
    pygame.draw.rect(surface, red, button2)
    pygame.draw.rect(surface, red, button3)
    pygame.draw.rect(surface, red, button4)
    pygame.draw.line(surface,black,(0,0),(1500,0),10)#1st black line    
    pygame.draw.line(surface,black,(900,0),(900,600),6)#1st vertical balck line
    pygame.draw.line(surface,black,(0,600),(1500,600),10)#2nd horiontal black line
    pygame.draw.line(surface,black,(1200,0),(1200,600),10)#2nd Vertical black line


##Buttons
button1=pygame.Rect(930,30,250,30)
button2=pygame.Rect(930,70,250,30)
button3=pygame.Rect(930,110,250,30)
button4=pygame.Rect(930,150,250,30)
    
##Sorting algorithms

##Bubble sort
def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[i]>arr[j]:
                color_array[i]=blue
                color_array[j]=black
                arr[i],arr[j]=arr[j],arr[i]
                redraw()
                color_array[i]=green
                color_array[j]=orange
        color_array[i]=green

##Selection sort
def selectionSort(A):
    for i in range(len(A)): 
        min_idx = i
        prev=min_idx
        color_array[min_idx]=blue
        for j in range(i+1, len(A)): 
            if A[min_idx] > A[j]:
                min_idx = j
                color_array[j]=black
                redraw()
                color_array[prev]=green
                color_array[j]=orange
        A[i], A[min_idx] = A[min_idx], A[i] 
        color_array[prev]=green

##Merge sort
def mergesort(array, l, r): 
    mid =(l + r)//2
    if l<r: 
        mergesort(array, l, mid) 
        mergesort(array, mid + 1, r) 
        merge(array, l, mid,mid + 1, r) 
def merge(array, x1, y1, x2, y2): 
    i = x1 
    j = x2 
    temp =[] 
    while i<= y1 and j<= y2: 
        color_array[i]=blue
        color_array[j]=black
        redraw()
        color_array[i]=orange
        color_array[j]=orange
        if array[i]<array[j]: 
                temp.append(array[i]) 
                i+= 1
        else: 
                temp.append(array[j]) 
                j+= 1
    while i<= y1: 
        color_array[i]=blue 
        redraw() 
        color_array[i]=orange
        temp.append(array[i]) 
        i+= 1
    while j<= y2: 
        color_array[j]=blue
        redraw()
        color_array[j]=orange
        temp.append(array[j]) 
        j+= 1
    j = 0
    
    for i in range(x1, y2 + 1):   
        array[i]= temp[j]
        j+= 1
        color_array[i]=orange 
        redraw()
        
        if y2-x1 == len(array)-2: 
            color_array[i]=green
        else:     
            color_array[i]=orange




   
gameLoop=True
while gameLoop:
    surface.fill(white)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gameLoop=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_r:
                generate_array()
            if event.key==pygame.K_UP:
                bubbleSort(array)
            if event.key==pygame.K_DOWN:
                selectionSort(array)
            if event.key==pygame.K_LEFT:
                mergesort(array, 1, len(array)-1)
        if event.type==pygame.MOUSEBUTTONDOWN:
            mouse_pos=event.pos
            if button1.collidepoint(mouse_pos):
                if event.button==1:
                    generate_array()

            if button2.collidepoint(mouse_pos):
                if event.button==1:
                    bubbleSort(array)

            if button3.collidepoint(mouse_pos):
                if event.button==1:
                    selectionSort(array)

            if button4.collidepoint(mouse_pos):
                if event.button==1:
                    mergesort(array, 1, len(array)-1)

                    
    #pygame.draw.rect(surface, [255, 0, 0], button1)  
    draw_lines()
    pygame.display.update()
pygame.quit()
