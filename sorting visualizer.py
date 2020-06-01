import pygame
import random
pygame.init()


surface=pygame.display.set_mode((1400,700))
pygame.display.set_caption("Sorting visualizer")

#Colours
red=(255,99,71)
green=(0,204,104)
blue=(0,0,255)
black=(0,0,0)
orange=(255,104,0)
white=(255,255,255)
grey=(180,180,180)
color_array=[orange]*200
array=[0]*200


#Generates new array every time you press r on your keyboard.iuigjyg
def generate_array():
    for i in range(1,200):
        color_array[i]=orange
        array[i]=random.randrange(1,200)
generate_array()

def redraw():
    surface.fill(white)
    draw_lines()
    pygame.display.update()


##This Function draws 3 types of lines 
def draw_lines():
    #Horizontal grey lines
    for i in range(1,150):
        pygame.draw.line(surface,grey,(0,5*i),(1400,5*i),1)

    for i in range(1,200):
        pygame.draw.line(surface,color_array[i],(6*i,6),(6*i,array[i]*3),5)
    pygame.draw.line(surface,black,(0,0),(1400,0),10)
        

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
'''
def mergeSort(array):
    if len(array)>1:
        mid=len(array)//2
        left=array[:mid]
        right=array[mid:]
        mergeSort(left)
        mergeSort(right)
        temp=[]
        i=j=k=0
        while i<len(left) and j <len(right):
            color_array[1]=blue
            color_array[mid]=black
            redraw()
            color_array[1]=green
            color_array[mid]=green
            if left[i]<right[j]:
                temp.append(left[i])
                i+=1
                k+=1
            else:
                temp.append(right[j])
                j+=1
                k+=1
        while i<len(left):
            
            temp.append(left[i])
            i+=1
            k+=1
        while j<len(right):
            temp.append(right[j])
            j+=1
            k+=1
'''

def merge(left,right):
    result=[]
    i,j=0,0
    while i<len(left) and j<len(right):
        color_array[left[i]]=blue
        color_array[right[j]]=black
        redraw()
        color_array[left[i]]=green
        color_array[right[j]]=green
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    
    for k in range(i,len(left)):
        color_array[k]=blue
        result.append(left[k])
        redraw()
        color_array[k]=green
    for k in range(j,len(right)):
        color_array[k]=blue
        result.append(right[k])
        color_array[k]=green
    for k in range(len(result)):
        array[k]=result[k]
    redraw()
    return result

def mergeSort(arr):
    mid=len(arr)//2
    if len(arr)==1:
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
            if event.key==pygame.K_r:
                generate_array()
            if event.key==pygame.K_UP:
                bubbleSort(array)
            if event.key==pygame.K_DOWN:
                selectionSort(array)
            if event.key==pygame.K_LEFT:
                mergeSort(array)
            
    draw_lines()
    pygame.display.update()
pygame.quit()
