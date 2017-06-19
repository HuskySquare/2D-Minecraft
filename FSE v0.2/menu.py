#menu.py
from pygame import*
from time import time as tm
import pygame
import os
pygame.init()
pygame.mixer.init()
pygame.mixer.pre_init(22050,-16,2,2048)


screen=display.set_mode((1280,720))
#////////////////////////////////////////////////////////////////
background=image.load("Images/background.png")
title=image.load("menuImages/title.png")
#////////////////////////////////////////////////////////////////
background=transform.scale(background,(1280,720))
#/////////////////////////////////////////////////////////////////
andy58 = font.Font("fonts/HW ANDY.ttf",58)
andy44 = font.Font("fonts/HW ANDY.ttf",44)
andy18 = font.Font("fonts/HW ANDY.ttf", 18)
andy16 = font.Font("fonts/HW ANDY.ttf", 16)

play = andy44.render("Play", True,(200,200,200))
play2 = andy58.render("Play", True,(255,255,0))
world = andy44.render("World", True,(200,200,200))
world2 = andy58.render("World", True,(255,255,0))
generate = andy44.render("Generate", True,(200,200,200))
generate2 = andy58.render("Generate", True,(255,255,0))
Player = andy44.render("Player" , True,(200,200,200))
player2 = andy58.render("Player",True,(255,255,0))
playworld = andy44.render("Play World" , True,(200,200,200))
playworld2 = andy58.render("Play World",True,(255,255,0))
settings = andy44.render("Settings", True, (200,200,200))
settings2 = andy58.render("Settings", True, (255,255,0))
leave = andy44.render("Exit",True,(200,200,200))
leave2 = andy58.render("Exit",True,(255,255,0))
back = andy44.render("Back",True,(200,200,200))
back2 = andy58.render("Back",True,(255,255,0))

volume = andy44.render("Volume",True,(200,200,200))

text={"smaller"}

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
screening=True
playSelect = False
worldSelect = False
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
                playSelect = True
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
                pos = 760
                moving = False
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
        for evt in event.get():
            if evt.type == MOUSEBUTTONDOWN:
                if evt.button == 1:
                    leftClick = True
            if evt.type == MOUSEBUTTONUP:
                if evt.button==1:
                    leftClick = False
#///////////////////////////////////////////////////////////////
        display.flip()
#//////////////////////////////////////////////////////////////
        mx,my=mouse.get_pos()
        background.set_alpha(100)
        screen.blit(background,(0,0))
        screen.blit(volume,(600,100))
        barRect = Rect(560,200,200,10)
        sliderRect = Rect(pos,185,10,40)
        draw.rect(screen,(200,200,200),barRect)
        if (barRect.collidepoint(mx,my) or sliderRect.collidepoint(mx,my)) and leftClick:
            moving = True
        if moving and 560<=mx<=760:
            pos = mx
        if not leftClick:
            moving = False
        draw.rect(screen,(0,0,0), sliderRect)
        buttonRectBack = Rect(620,600,80,50)

        selectedVolume = andy44.render(str(round((pos-560)*(1/200),2)),True,(200,200,200))
        screen.blit(selectedVolume,(630,250))

        pygame.mixer.music.set_volume(round((pos-560)*(1/200),2))
        
        if buttonRectBack.collidepoint((mx,my)):
            screen.blit(back2,(600,590))
            if leftClick:
                optionsMenu=False
                screen.fill(0)
                menu=True
        else:
            screen.blit(back,(610,600))
            
################################################################

    while playSelect:
        leftClick = False
        for evt in event.get():
            if evt.type == MOUSEBUTTONDOWN:
                if evt.button == 1:
                    leftClick = True
        mx,my = mouse.get_pos()
        screen.fill(0)
        background.set_alpha(100)
        screen.blit(background,(0,0))
        playerRect = Rect(600,200,80,50)
        worldRect = Rect(600,400,80,50)
        if playerRect.collidepoint(mx,my):
            screen.blit(player2,(585,190))
            if leftClick:
                playSelect = False
                screening = False
                playerSelect=True
                import character
        else:
            screen.blit(Player,(600,200))

        if worldRect.collidepoint(mx,my):
            screen.blit(world2,(585,390))
            if leftClick:
                playSelect = False
                worldSelect = True
                ##screening = False
        else:
            screen.blit(world,(600,400))

        display.flip()

    while worldSelect:
        leftClick = False
        for evt in event.get():
            if evt.type == MOUSEBUTTONDOWN:
                if evt.button == 1:
                    leftClick = True
        mx,my = mouse.get_pos()
        screen.fill(0)
        background.set_alpha(100)
        screen.blit(background,(0,0))
        playworldRect = Rect(600,200,80,50)
        generateRect = Rect(600,400,80,50)
        if playworldRect.collidepoint(mx,my):
            screen.blit(playworld2,(585,190))
            if leftClick:
                worldSelect = False
                screening = False
        else:
            screen.blit(playworld,(600,200))

        if generateRect.collidepoint(mx,my):
            screen.blit(generate2,(585,390))
            if leftClick:
                import generation
        else:
            screen.blit(generate,(600,400))

        display.flip()
                
