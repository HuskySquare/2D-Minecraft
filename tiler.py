
from pygame import *

init()
newX = 8000
backPic = image.load("background.png")
x,y = backPic.get_size()
double = Surface((x*2,y))
back = transform.flip(backPic,True,False)
double.blit(backPic,(0,0))
double.blit(back,(x,0))
full = Surface((newX,y))
p=0
while p < newX:
    full.blit(double,(p,0))
    print(p)
    p += double.get_width()
image.save(full,"full.png")

