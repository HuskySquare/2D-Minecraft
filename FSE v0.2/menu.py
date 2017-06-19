#menu.py
from pygame import*
from time import time as tm
import pygame
import os
pygame.init() #initializing sounds
pygame.mixer.init()
pygame.mixer.pre_init(22050,-16,2,2048)


playerflag=bool(int (open("flag.txt","r").read())) #returns to menu
screen=display.set_mode((1280,720))
#////////////////////////////////////////////////////////////////
background=image.load("Images/background.png") #background
title=image.load("menuImages/title.png") #logo
#////////////////////////////////////////////////////////////////
background=transform.scale(background,(1280,720))
#/////////////////////////////////////////////////////////////////
#Fonts
andy58 = font.Font("fonts/HW ANDY.ttf",58)
andy44 = font.Font("fonts/HW ANDY.ttf",44)
andy18 = font.Font("fonts/HW ANDY.ttf", 18)
andy16 = font.Font("fonts/HW ANDY.ttf", 16)

play = andy44.render("Play", True,(200,200,200)) #Boring text Loading
play2 = andy58.render("Play", True,(255,255,0))
world = andy44.render("World", True,(200,200,200))
world2 = andy58.render("World", True,(255,255,0))
generate = andy44.render("Generate", True,(200,200,200))
generate2 = andy58.render("Generate", True,(255,255,0))
genback = andy44.render("Back", True,(200,200,200))
genback2 = andy58.render("Back", True,(255,255,0))
Player = andy44.render("Player" , True,(200,200,200))
player2 = andy58.render("Player",True,(255,255,0))
playworld = andy44.render("Play World" , True,(200,200,200))
playworld2 = andy58.render("Play World",True,(255,255,0))
playback = andy44.render("Back" , True,(200,200,200))
playback2 = andy58.render("Play World",True,(255,255,0))
settings = andy44.render("Settings", True, (200,200,200))
settings2 = andy58.render("Settings", True, (255,255,0))
leave = andy44.render("Exit",True,(200,200,200))
leave2 = andy58.render("Exit",True,(255,255,0))
back = andy44.render("Back",True,(200,200,200))
back2 = andy58.render("Back",True,(255,255,0))

volume = andy44.render("Volume",True,(200,200,200))

text={"smaller"} 

#////////////////////////////////////////////////////////////////
file1="Audio/01-Menu.mp3" #Loading music using pygame.mixer

pygame.mixer.music.load(file1)
pygame.mixer.music.play()
END_MUSIC_EVENT=pygame.USEREVENT+0
pygame.mixer.music.set_endevent(END_MUSIC_EVENT)
#////////////////////////////////////////////////////////////////
tempClock=time.Clock() #for day/night cycle
tempCount=0 #keeps track of alpha
positive=True #up or down
optionsMenu=False #boolean variables to indicate location in meny
screening=True
playSelect = False
worldSelect = False
menu=True
###################################################################
while screening: # if this is false, the game is playing
###################################################################
    while playSelect or playerflag: 
        leftClick = False #leftClick will only be true for one interation
        for evt in event.get():
            if evt.type == MOUSEBUTTONDOWN:
                if evt.button == 1:
                    leftClick = True
        mx, my = mouse.get_pos()
        screen.fill(0) #fills screen
        background.set_alpha(100) #alpha starts as 100
        screen.blit(background, (0, 0))
        playerRect = Rect(600, 200, 80, 50) #button
        worldRect = Rect(600, 300, 80, 50) #button
        playbackRect = Rect(625, 400, 75, 50)
        if playerRect.collidepoint(mx,my):
            screen.blit(player2,(585,190)) #yellow highlights
            if leftClick: #if clicked
                playSelect = False
                screening = False
                playerSelect=True #moving to next menu, character selection.
                import character
        else:
            screen.blit(Player,(600,200)) #regular text

        if worldRect.collidepoint(mx,my): #yellow highlights
            screen.blit(world2,(585,290))
            if leftClick:
                playSelect = False
                worldSelect = True
                menu = False
                playerflag = False #moving to next menu
                ##screening = False
        else:
            screen.blit(world,(600,300)) #regular text

        if playbackRect.collidepoint(mx,my): #yellow highlights
            screen.blit(genback2,(600,390))
            if leftClick:
                playerflag = False
                playSelect = False
                menu = True #goes back to regular menu
        else: 
            screen.blit(genback,(615,400)) #regular text

        display.flip() #update screen

    while menu:
        leftClick=False
        for evt in event.get():
            if evt.type==MOUSEBUTTONDOWN:
                if evt.button==1:
                     leftClick=True
        tempClock.tick(60)
        if tempCount<255 and positive:
            tempCount+=1 #daynight cycle to change alpha
        else:
            positive=False
        if tempCount>0 and not positive:
            tempCount-=1
        else:
            positive=True
        mx,my=mouse.get_pos()
        
        screen.fill(0) #black bacground
        background.set_alpha(tempCount) #changing alpha makes things appear darker
        screen.blit(background,(0,0))
        screen.blit(title,(380,100))
#/////////////////////////////////////////////////////////////////       
        buttonRectStart = Rect(613,312,65,50) #button
        if buttonRectStart.collidepoint((mx,my)):
            screen.blit(play2,(603,302)) #yellow background
            if leftClick:
                screen.fill(0)
                menu=False
                playSelect = True #moving to next menu
        else:
            screen.blit(play,(613,312)) #normal text
#/////////////////////////////////////////////////////////////////
        buttonRectOptions = Rect(585,400,140,50)
        if buttonRectOptions.collidepoint((mx,my)):
            screen.blit(settings2,(570,390)) #yellow highlights
            if leftClick:
                screen.fill(0) #moving to next menu
                menu=False
                optionsMenu=True
                pos = 760 #position of slider
                moving = False
                display.flip()

        else:
            screen.blit(settings,(585,400))
        
#/////////////////////////////////////////////////////////////////
        buttonRectQuit = Rect(613,480,80,50)
        if buttonRectQuit.collidepoint((mx,my)):
            screen.blit(leave2,(603,470))
            if leftClick: #keeps track of default settings
                out=open("falg.txt","w")
                out.write("0")
                out.close()
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



    while worldSelect: #world generation menu
        leftClick = False
        for evt in event.get():
            if evt.type == MOUSEBUTTONDOWN:
                if evt.button == 1:
                    leftClick = True
        mx,my = mouse.get_pos()
        screen.fill(0)
        background.set_alpha(100)
        screen.blit(background,(0,0))
        playworldRect = Rect(550,225,200,50) #button rects
        generateRect = Rect(600,300,150,50)
        genbackRect = Rect(625,385,75,50)
        if playworldRect.collidepoint(mx,my):
            screen.blit(playworld2,(555,190)) #yellow highlights
            if leftClick:
                worldSelect = False #moving to next menu
                screening = False
                out = open("flag.txt", "w") #keeps track in .txt file
                out.write("0")
                out.close()
                import FSE #goes to game
        else:
            screen.blit(playworld,(580,200)) #button

        if generateRect.collidepoint(mx,my):
            screen.blit(generate2,(580,290)) #yellow highlights
            if leftClick:
                import generation #generates world in seperate py file
                screen.blit(andy18.render("World has been generated!", True, (200, 200, 200)), (500, 600))
        else:
            screen.blit(generate,(600,300))

        if genbackRect.collidepoint(mx,my):
            screen.blit(genback2,(610,375)) #yellow highlights
            if leftClick:
                worldSelect = False
                playSelect = True #returns to menu

        else:
            screen.blit(genback,(625,385)) #regular text


        display.flip()
                
out=open("flag.txt","w")
out.write("0")
out.close()