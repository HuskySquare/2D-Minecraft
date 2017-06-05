#menu.py
from pygame import*
from time import time as tm
screen=display.set_mode((1248,704))
background=image.load("background.png")
bacground=transform.scale(background,(1248,704))
tempClock=time.Clock()
tempCount=0
positive=True

menu=True
while menu:
    leftClick=False
    for evt in event.get():
        if evt.type==MOUSEBUTTONDOWN:
            if evt.button==1:
                 leftClick=True
    tempClock.tick(60)
    if tempCount<255 and positive:
        tempCount+=1
    else:
        positive=False
    if tempCount>0 and not positive:
        tempCount-=1
    else:
        positive=True
    screen.fill(0)
    background.set_alpha(tempCount)
    screen.blit(background,(0,0))
    buttonRect=Rect(623,352,50,50)
    draw.rect(screen,(255,0,0),buttonRect)
    display.flip()
    
    mx,my=mouse.get_pos()
    if buttonRect.collidepoint((mx,my)) and leftClick:
        screen.fill(0)
        menu=False
