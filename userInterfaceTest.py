#UserInterfaceTesting
from pygame import*
from random import*
screen=display.set_mode((800,600))
playerInventory=["5","6","1","11","13","14"]
squares=[]
font.init()
algerFont=font.SysFont("Algerian",25)

def keyCheck():
    keys=key.get_pressed()
    if keys[K_i]:
        pass
running=True
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False
#-------------------------------------------------------
    for i in range(5):
        squares.append(playerInventory[i])
        tempText=algerFont.render(str(playerInventory[i]),True,(255,0,0))
        draw.rect(screen,(0,0,0),(50+i*55,55,50,50))
        draw.rect(screen,(255,0,0),(50+i*55,55,50,50),1)
        screen.blit(tempText,(50+i*55,55))
    time.wait(100)
    shuffle(playerInventory)
#-------------------------------------------------------
    display.flip()
quit()
