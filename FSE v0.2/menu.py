#menu.py
from pygame import*
from time import time as tm
import pygame

pygame.init()
pygame.mixer.init()
pygame.mixer.pre_init(22050,-16,2,2048)

screen=display.set_mode((1248,704))
#////////////////////////////////////////////////////////////////
background=image.load("background.png")
title=image.load("menuImages/title.png")
#////////////////////////////////////////////////////////////////
background=transform.scale(background,(1248,704))
#/////////////////////////////////////////////////////////////////
andy58 = font.Font("fonts/HW ANDY.ttf",58)
andy44 = font.Font("fonts/HW ANDY.ttf",44)
andy18 = font.Font("fonts/HW ANDY.ttf", 18)
andy16 = font.Font("fonts/HW ANDY.ttf", 16)

play = andy44.render("Play",True,(200,200,200))
play2 = andy58.render("Play",True,(255,255,0))
settings = andy44.render("Settings", True, (200,200,200))
settings2 = andy58.render("Settings", True, (255,255,0))
leave = andy44.render("Exit",True,(200,200,200))
leave2 = andy58.render("Exit",True,(255,255,0))
back = andy44.render("Back",True,(200,200,200))
back2 = andy58.render("Back",True,(255,255,0))


#////////////////////////////////////////////////////////////////
file1="Audio/01-Menu.mp3"

pygame.mixer.music.load(file1)
pygame.mixer.music.play()
END_MUSIC_EVENT=pygame.USEREVENT+0
pygame.mixer.music.set_endevent(END_MUSIC_EVENT)
#////////////////////////////////////////////////////////////////
tempClock=time.Clock()
tempCount=0
positive=True
optionsMenu=False
infoMenu=False
screening=True
###################################################################
while screening:
    menu=True
###################################################################
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
        mx,my=mouse.get_pos()
        
        screen.fill(0)
        background.set_alpha(tempCount)
        screen.blit(background,(0,0))
        screen.blit(title,(380,100))
#/////////////////////////////////////////////////////////////////       
        buttonRectStart = Rect(613,312,65,50)
        if buttonRectStart.collidepoint((mx,my)):
            screen.blit(play2,(603,302))
            if leftClick:
                screen.fill(0)
                menu=False
                screening=False
                pygame.mixer.music.pause()
        else:
            screen.blit(play,(613,312))
#/////////////////////////////////////////////////////////////////
        buttonRectOptions = Rect(585,400,140,50)
        if buttonRectOptions.collidepoint((mx,my)):
            screen.blit(settings2,(570,390))
            if leftClick:
                screen.fill(0)
                menu=False
                optionsMenu=True
                display.flip()

        else:
            screen.blit(settings,(585,400))
        
#/////////////////////////////////////////////////////////////////
        buttonRectQuit = Rect(613,480,80,50)
        if buttonRectQuit.collidepoint((mx,my)):
            screen.blit(leave2,(603,470))
            if leftClick:
                quit()
        else:
            screen.blit(leave,(613,480))
            
        display.flip()
   
        
#################################################################
    while optionsMenu:
        leftClick=False
        for evt in event.get():
            if evt.type==MOUSEBUTTONDOWN:
                if evt.button==1:
                    leftClick=True
#///////////////////////////////////////////////////////////////
        display.flip()
#//////////////////////////////////////////////////////////////
        mx,my=mouse.get_pos()
        background.set_alpha(100)
        screen.blit(background,(0,0))
        buttonRectBack = Rect(620,600,80,50)
        if buttonRectBack.collidepoint((mx,my)):
            screen.blit(back2,(600,590))
            if leftClick:
                optionsMenu=False
                screen.fill(0)
                menu=True
        else:
            screen.blit(back,(610,600))
            
################################################################


        
    
                
