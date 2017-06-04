#LoadingScreenTest
from pygame import*
screen=display.set_mode((800,600))
screen.fill((0,0,0)) #fills screen
buttonRect=Rect(250,100,75,75) #start Button
draw.rect(screen,(255,0,0),buttonRect) 
display.flip()
menu=True
while menu: #event loop for menu
    leftClick=False
    running=False
    for evt in event.get(): #checks events
        if evt.type==MOUSEBUTTONDOWN:
            if evt.button==1:
                leftClick=True
    mx,my=mouse.get_pos()
    if buttonRect.collidepoint((mx,my)) and leftClick:
        #if mouse clicks on button
        print("running")
        menu=False #starts game
        running=True 

while running:
    print("RUnning")
    screen.fill((255,0,0))
    display.flip()
display.flip()
