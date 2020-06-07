import pygame
import random
pygame.init()


surface=pygame.display.set_mode((1200,600))
pygame.display.set_caption("Sorting visualizer")
clock=pygame.time.Clock()

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
pygame.event.pump()


###Displays text on buttons.
def messageDisplay(text,font):
    pygame.event.pump()
    textSurf=font.render(text,True,black)
    return textSurf, textSurf.get_rect()

def text_(text,buttons):
    pygame.event.pump()
    font=pygame.font.Font("freesansbold.ttf",18)
    textsurf,textrect=messageDisplay(text,font)
    textrect.center=buttons.center
    surface.blit(textsurf,textrect)
    #pygame.display.update()

#Generates new array every time you press r on your keyboard.
def generate_array():
    pygame.event.pump()
    for i in range(1,150):
        color_array[i]=orange
        array[i]=random.randrange(1,150)
generate_array()

check_sort=False

def redraw():
    pygame.event.pump()
    surface.fill(white)
    draw_lines()
    pygame.display.update()


##This Function draws 3 types of lines 
def draw_lines():
    pygame.event.pump()
    #Horizontal grey lines
    for i in range(1,150):
        pygame.draw.line(surface,grey,(0,5*i),(900,5*i),1)

    for i in range(1,150):
        pygame.draw.line(surface,color_array[i],(6*i,6),(6*i,array[i]*3),5)
    pygame.draw.rect(surface,grey,(900,0,400,600))
    if check_sort == True:
        pygame.draw.rect(surface, grey,text_message)
        text_("Array is sorted",text_message)
              
    pygame.draw.rect(surface, red, button1)
    pygame.draw.rect(surface, red, button2)
    pygame.draw.rect(surface, red, button3)
    pygame.draw.rect(surface, red, button4)
    pygame.draw.rect(surface, red, button5)
    pygame.draw.rect(surface, red, button6)
    pygame.draw.rect(surface, grey,textbox)
    pygame.draw.line(surface,black,(0,0),(1500,0),10)#1st black line    
    pygame.draw.line(surface,black,(900,0),(900,600),6)#1st vertical balck line
    pygame.draw.line(surface,black,(0,600),(1500,600),10)#2nd horiontal black line
    pygame.draw.line(surface,black,(1200,0),(1200,600),10)#2nd Vertical black line
    text_("Regenerate array",button1)
    text_("Bubble Sort",button2)
    text_("Selection Sort",button3)
    text_("Merge Sort",button4)
    text_("Heap Sort",button5)
    text_("Quick Sort",button6)
    text_("Click on the above buttons",textbox)
    
##Buttons
button1=pygame.Rect(930,30,250,30)
button2=pygame.Rect(930,70,250,30)
button3=pygame.Rect(930,110,250,30)
button4=pygame.Rect(930,150,250,30)
button5=pygame.Rect(930,190,250,30)
button6=pygame.Rect(930,230,250,30)
text_message=pygame.Rect(350,300,200,50)
textbox=pygame.Rect(930,280,250,30)
    
##Sorting algorithms

##Bubble sort
def bubbleSort(arr):
    pygame.event.pump()
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
    pygame.event.pump()
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
    pygame.event.pump()
    mid =(l + r)//2
    if l<r: 
        mergesort(array, l, mid) 
        mergesort(array, mid + 1, r) 
        merge(array, l, mid,mid + 1, r) 
def merge(array, x1, y1, x2, y2):
    pygame.event.pump()
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


##Heap Sort
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        color_array[i] = blue
        color_array[l] = black
        redraw()
        color_array[i] = orange
        color_array[l] = orange
        redraw()
        largest = l
    if r < n and arr[i] < arr[r] and arr[l] < arr[r]:
        color_array[i] = blue
        color_array[r] = black
        redraw()
        color_array[i] = orange
        color_array[r] = orange
        redraw()
        largest = r
    if largest != i:
        color_array[largest] = blue
        color_array[i] = black
        redraw()
        arr[i], arr[largest] = arr[largest], arr[i]
        color_array[largest] = orange
        color_array[i] = orange
        redraw()
        heapify(arr, n, largest)


def heapsort(arr, n):
    pygame.event.pump()
    for i in range(n//2-1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        color_array[i] = green
        color_array[0] = green
        redraw()
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)


## Quick Sort
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high+1):
        color_array[j] = black
        color_array[high] = blue
        redraw()
        color_array[j] = orange
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            color_array[i] = orange
            redraw()

    arr[i+1], arr[high] = arr[high], arr[i+1]
    redraw()
    return i + 1


def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quicksort(arr, low, pi-1)
        quicksort(arr, pi+1, high)


   
gameLoop=True
while gameLoop:
    pygame.event.pump()
    surface.fill(white)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gameLoop=False

                
        if event.type==pygame.MOUSEBUTTONDOWN:
            mouse_pos=event.pos
            if button1.collidepoint(mouse_pos):
                if event.button==1:
                    generate_array()
                    check_sort=False

            if button2.collidepoint(mouse_pos):
                if event.button==1 and check_sort==False:
                    bubbleSort(array)
                    check_sort=True

            if button3.collidepoint(mouse_pos):
                if event.button==1 and check_sort==False:
                    selectionSort(array)
                    check_sort=True

            if button4.collidepoint(mouse_pos):
                if event.button==1 and check_sort==False:
                    mergesort(array, 1, len(array)-1)
                    check_sort=True

            if button5.collidepoint(mouse_pos):
                if event.button==1 and check_sort==False:
                    heapsort(array, len(array))
                    check_sort=True

            if button6.collidepoint(mouse_pos):
                if event.button==1:
                    quicksort(array, 0, len(array)-1)
                    for i in range(1,150):
                        color_array[i]=green
                        redraw()
                    check_sort=True
                
    #pygame.draw.rect(surface, [255, 0, 0], button1)  
    draw_lines()
    pygame.display.update()
    clock.tick(90)
pygame.quit()
