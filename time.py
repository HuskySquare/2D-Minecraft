#Day and Night
from pygame import*
from time import time as tm
screen=display.set_mode((800,600))
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
    if clockCount<86400:
        clockCount+=500
    else:
        clockCount=1
    filler=clockCount//339
    print(filler)
    if positive:
        if filler<255:
            screen.fill((filler,0,0))
        else:
            positive=False
    else:
        if 255-filler>0:
            screen.fill((255-filler,0,0))
        else:
            positive=True
    print(positive)
#-------------------------------------------------------
    display.flip()
quit()
