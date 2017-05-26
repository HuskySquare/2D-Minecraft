#Day and Night
from pygame import*
from time import time as tm
screen=display.set_mode((800,600))
screen.fill((0,0,0))
background=image.load("background.png")
clock=time.Clock()
clockCount=0
positive=True
filler=0
running=True
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False
#-------------------------------------------------------
    clock.tick(60)
    if clockCount<255 and positive:
        clockCount+=1
    else:
        positive=False
    if clockCount>0 and not positive:
        clockCount-=1
    else:
        positive=True
    screen.fill((clockCount,0,0))
    #background.set_alpha(clockCount)
    #screen.blit(background,(0,0))
    #print(background.get_alpha())
    display.set_caption("dank example fps = {0:.0f}".format(clock.get_fps()))
#-------------------------------------------------------
    display.flip()
quit()
