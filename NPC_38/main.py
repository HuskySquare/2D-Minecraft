#main.py
from pygame import*
from random import*
import os

init()
screen=display.set_mode((1248,704))
backPic=image.load("full.png")
X=0
Y=1
VY=2
ONGROUND=3
SCREENX=4
player= [624,660,0,True,624]




def movePlayer(player):
    global move, frame
    keys = key.get_pressed()

    newMove = -1        
    if keys[K_d] and player[X]<7400:
        newMove = RIGHT
        player[X]+=3
    elif keys[K_a] and player[X]>624:
        newMove = LEFT
        player[X]-=3
    else:
        frame = 0
    if keys[K_w] and player[ONGROUND]:
        player[VY]=-10
        player[ONGROUND]=False
        
    player[Y]+=player[VY]
    if player[Y]>=660:
       player[Y]=660
       player[VY]=0
       player[ONGROUND]=True
    player[VY]+=0.7
    
    if move == newMove: 
        frame = frame + 0.2 
        if frame >= len(pics[move]):
            frame = 1
    elif newMove != -1: 
        move = newMove      
        frame = 1

def makeMove(name,start,end):
    move = []
    for i in range(start,end+1):
        move.append(image.load("%s/%s%03d.png" % (name,name,i)))
    return move


def drawScene(screen,player):
    offsetX=player[SCREENX]-player[X]
    screen.blit(backPic, (0,0))
    pic = pics[move][int(frame)]
    screen.blit(pic,(624,player[Y]))
    for pl in plats:
        p=pl.move(offsetX,0)
        draw.rect(screen,(0,0,0),p)
    display.flip()

def checkCollide(player,points):
    rec=Rect(player[X],player[Y],39,41)
    for p in points:
        if rec.colliderect(p):
            if player[VY]>0 and rec.move(0,-player[VY]).colliderect(p)==False:
                player[ONGROUND]=True
                player[VY]=0
                player[Y] = p.y -41
                
    

RIGHT = 1 
LEFT = 0
pics = []
pics.append(makeMove("NPC_38",1,17))      # LEFT
pics.append(makeMove("NPC_38",18,34))    #RIGHT

frame=0 
move=0      

plats=[]
for i in range(80):
    plats.append(Rect(randint(100,2000),randint(500,700),60,10))
    
    
running=True
myClock=time.Clock()
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False
        if evt.type==MOUSEBUTTONDOWN:
            if evt.button==1:
                leftClick=True
            if evt.button==3:
                rightClick=True
            if evt.button==4:
                scrollUp=True
            if evt.button==5:
                scrollDown=False
    movePlayer(player)          
    checkCollide(player,plats)
    drawScene(screen,player)
    myClock.tick(60)
    print(myClock)
#-------------------------------------------------------
#-------------------------------------------------------
    display.flip()
quit()
