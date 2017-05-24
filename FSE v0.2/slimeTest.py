#slimeTest
from pygame import*
X=0
Y=1
VY=2
ONGROUND=3
SCREENX=4
VX=5
slime=[400,300,0,True,624,0]

def moveSlime(slime):
    keys= key.get_pressed()
    if keys[K_d] and keys[K_a]:
        slimeFrame=0
        pass
    if keys[K_d] and slime[ONGROUND]:
        slime[ONGROUND]=False
        slime[VY]-=10
        slime[VX]+=10
    if keys[K_a] and slime[ONGROUND]:
        slime[ONGROUND]=False
        slime[VY]-=10
        slime[VX]-=10
    slime[Y]+=slime[VY]
    if slime[Y]>=324:
        slime[Y]=324
        slime[VY]=0
        slime[ONGROUND]=0
    slime[VY]+=0.7
    if slime[VX]<=0:
        slime[X]+=slime[VX]
        slime[VX]+=0.7
    if slime[VX]>=0:
        slime[X]+=slime[VX]
        slime[VX]-=0.7

def drawSlime(slime):
    slimePic=image.load("slime001.png")
    screen.blit(slimePic,(600-slimePic.get_width()//2,slime[Y]-slimePic.get_height()))
    display.flip()


background=image.load("background.png")
screen=display.set_mode((800,600))
screen.fill((111,111,111))

running=True
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False
#-------------------------------------------------------
    drawSlime(slime)
    moveSlime(slime)
#-------------------------------------------------------
    display.flip()
quit()
