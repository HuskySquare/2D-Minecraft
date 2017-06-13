from pygame import *
init()     #Initialzie directly after importing to avoid module conflicts
from glob import glob

colour=Color(171,181,198)
names,hair=[],[]
x=glob("hair/*.png")
anchor=0
for i,j in zip(x,range(1,len(x)+1)):
    names.append("Hair {0}".format(j))
    hair.append(image.load(i))
del x
screen=display.set_mode((1248,704))
screen.fill((255,255,255))
bar=image.load("Hue.png")
andy=font.Font("HW ANDY.ttf",50)
clock=time.Clock()

text=andy.render(names[anchor],1,colour)
# h=transform.scale(transform.chop(hair[anchor],(0,0,40,56)),(200,280))
# h=transform.chop(hair[anchor],(0,0,40,56)).convert_alpha()
h=transform.scale(hair[anchor],(400,7840))
h.fill((220, 141, 50), special_flags=BLEND_SUB)
x=transform.scale(h,(200,280))
# h=transform.scale(Surface((40,56),hair[anchor]),(200,280))
#--------------------------RECT---------------------------------
barRect=Rect((478,298),bar.get_size())
hairRect=Rect((499,208),text.get_size())

def updatecolour():
    global anchor,colour,text

    colour=screen.get_at((mx,my))
    screen.fill((255,255,255))
    screen.blit(bar, (478,298))
    screen.blit(andy.render(names[anchor],1,(0,0,0)),(499,208))
    h = transform.scale(hair[anchor], (400, 7840))
    h.fill(Color(255, 255, 255) - colour, special_flags=BLEND_SUB)
    screen.blit(h, (375, -75), (0, 0, 400, 560))
def updatehair():
    global anchor,colour,h
    anchor += 1
    try:
        screen.fill((255, 255, 255))
        screen.blit(bar, (478,298))
        screen.blit(andy.render(names[anchor], 1, (0, 0, 0)), (499,208))
        h = transform.scale(hair[anchor], (400, 7840))
        h.fill(Color(255,255,255)-colour, special_flags=BLEND_SUB)
        screen.blit(h, (375, -75), (0, 0, 400, 560))
    except IndexError:
        anchor=0


running= True

screen.blit(bar,(478,298))
screen.blit(andy.render(names[anchor],1,(0,0,0)),(499,208))
screen.blit(h,(375,-75),(0,0,400,560))
# scren.blit()
while running:

    leftClick=False
    rightClick=False
    mx, my = mouse.get_pos()
    mb = mouse.get_pressed()
    print(mx,my)
    if barRect.collidepoint(mx,my) and mb[0]==1:
        updatecolour()
    if hairRect.collidepoint(mx,my) and mb[0]==1:
        updatehair()
    for evt in event.get():
        if evt.type == QUIT:
            running = False
        if evt.type == MOUSEBUTTONDOWN:
            if evt.button == 1:
                leftClick = True
            if evt.button == 3:
                rightClick = True

    display.flip()
    clock.tick(10)

quit()