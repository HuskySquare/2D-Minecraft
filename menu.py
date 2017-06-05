#menu.py
from pygame import*
from time import time as tm
screen=display.set_mode((1248,704))
background=image.load("background.png")
title=image.load("title.png")
start=image.load("titleStart.png")
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
    screen.blit(title,(350,100))
    buttonRect=Rect(543,358,240,80)
    screen.blit(start,(513,312))
    display.flip()
    
    mx,my=mouse.get_pos()
    if buttonRect.collidepoint((mx,my)):
        draw.rect(screen,(0,0,0),buttonRect,2)
        if leftClick:
            screen.fill(0)
            menu=False
