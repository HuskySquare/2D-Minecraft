#menu.py
from pygame import*
from time import time as tm
screen=display.set_mode((1248,704))
#////////////////////////////////////////////////////////////////
background=image.load("background.png")
title=image.load("menuImages/title.png")
start=image.load("menuImages/titleStart.png")
options=image.load("menuImages/titleOptions.png")
#////////////////////////////////////////////////////////////////
background=transform.scale(background,(1248,704))
#////////////////////////////////////////////////////////////////
tempClock=time.Clock()
tempCount=0
positive=True
optionsMenu=False
screening=True
#////////////////////////////////////////////////////////////////
while screening:
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
        buttonRectStart=Rect(543,358,240,80)
        screen.blit(start,(513,312))
        buttonRectOptions=Rect(500,480,330,80)
        screen.blit(options,(475,435))
        display.flip()
#/////////////////////////////////////////////////////////////////    
        mx,my=mouse.get_pos()
        if buttonRectStart.collidepoint((mx,my)) and leftClick:
            screen.fill(0)
            menu=False
            screening=False
        if buttonRectOptions.collidepoint((mx,my)) and leftClick:
            screen.fill(0)
            menu=False
            optionsMenu=True
            background.set_alpha(100)
            screen.blit(background,(0,0))
            optionsBack=image.load("menuImages/OptionsBack.png")
            optionsBack=transform.scale(optionsBack,(160,70))
            display.flip()
#////////////////////////////////////////////////////////////////
    while optionsMenu:
        leftClick=False
        for evt in event.get():
            if evt.type==MOUSEBUTTONDOWN:
                if evt.button==1:
                    leftClick=True
#///////////////////////////////////////////////////////////////
        buttonRectBack=Rect(40,40,140,70)
        screen.blit(optionsBack,(34,40))
        display.flip()
#//////////////////////////////////////////////////////////////
        mx,my=mouse.get_pos()
        if buttonRectBack.collidepoint((mx,my)) and leftClick:
            optionsMenu=False
            screen.fill(0)
            menu=True
        
    
                
