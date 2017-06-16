from pygame import *
init()     #Initialzie directly after importing to avoid module conflicts
from glob import glob
img={"hair":[],
     "head":image.load("Player_Head.png").subsurface(0,0,40,56).copy(),
     "undershirt":image.load("Player_Undershirt.png").subsurface(0,0,40,56).copy(),
     "shirt":image.load("Player_Shirt.png").subsurface(0,0,40,56).copy(),
     "pants":image.load("Player_Shirt.png").subsurface(0,0,40,56).copy(),
     "shoes":image.load("Player_Shoes.png").subsurface(0,0,40,56).copy(),
     "hands":image.load("Player_Hands.png").subsurface(0,0,40,56).copy()}
colour=Color(171,181,198)
names=[]

anchor="intro"
x=glob("hair/*.png") #Temperory Variable


for i,j in zip(x,range(1,len(x)+1)):
    names.append("Hair {0}".format(j))
    img["hair"].append(image.load(i))
del x
screen=display.set_mode((1248,704))
screen.fill((255,255,255))

bar=image.load("Hue.png")
andy=font.Font("HW ANDY.ttf",50)
clock=time.Clock()
counter=0  #Used to control what hair to use
text=andy.render(names[counter],1,colour)
# h=transform.scale(transform.chop(hair[counter],(0,0,40,56)),(200,280))
# h=transform.chop(hair[counter],(0,0,40,56)).convert_alpha()
# h=transform.scale(hair[counter],(400,7840))
h=img["hair"][counter].subsurface(0,0,40,56).copy()
h.fill(Color(255,255,255)-colour, special_flags=BLEND_SUB)
rect={"intro":{"hair":(440,121,78,61),"skin":(440,186,83,61),"clothes":(440,251,138,61)},
      "hair":{"hair":(530,65,40,56),"bar":(478,298,178,16),"back":(495,412,93,61)},
      "clothes":{},
      "skin":{"bar":(478,298,40,56),"back":(478,474,93,61)}}  #Two dimensional dictionary
options={"hair":andy.render("Hair",1,(0,0,0)),"skin":andy.render("Skin",1,(0,0,0)),"clothes":andy.render("Clothes",1,(0,0,0)),
         "back":andy.render("Back",1,(0,0,0)),"create":andy.render("Create",1,(0,0,0))}

#--------------------------RECT---------------------------------
textRect=Rect((499,208),text.get_size())
barRect=Rect((478,298),bar.get_size())
#-----------------------------------------------------------------
class current():
    def __init__(self,head,hair,undershirt,shirt,pants,shoes,hands):
        self.head=head
        self.hair=hair
        self.undershirt=undershirt
        self.shirt=shirt
        self.pants=pants
        self.shoes=shoes
        self.hands=hands
    def draw(self, pos):
        screen.blit(self.head,pos)
        screen.blit(self.hair,pos)
        screen.blit(self.undershirt,pos)
        screen.blit(self.shirt,pos)
        screen.blit(self.pants,pos)
        screen.blit(self.shoes,pos)

img["head"].fill(Color(255,255,255)-colour, special_flags=BLEND_SUB)
img["undershirt"].fill(Color(255,255,255)-colour, special_flags=BLEND_SUB)
img["shirt"].fill(Color(255,255,255)-colour, special_flags=BLEND_SUB)
img["pants"].fill(Color(255,255,255)-colour, special_flags=BLEND_SUB)
img["shoes"].fill(Color(255,255,255)-colour, special_flags=BLEND_SUB)
img["hands"].fill(Color(255,255,255)-colour, special_flags=BLEND_SUB)
default=current(img["head"],
                h,
                img["undershirt"],
                img["shirt"],
                img["pants"],
                img["shoes"],
                img["hands"])


class intro():  #A class used for bliting the entire body

    def menu():
        screen.fill((255,255,255))
        screen.blit(options["hair"],rect["intro"]["hair"][:2])
        screen.blit(options["skin"], rect["intro"]["skin"][:2])
        screen.blit(options["clothes"], rect["intro"]["clothes"][:2])
        #screen.blit(options["create"],)
    def check():
        global anchor
        if Rect(rect["intro"]["hair"]).collidepoint(mx,my) and mb[0]==1:
            anchor="hair"
            hair.menu()
        elif Rect(rect["intro"]["skin"]).collidepoint(mx,my) and mb[0]==1:
            anchor="skin"
            skin.menu()
        elif Rect(rect["intro"]["clothes"]).collidepoint(mx,my) and mb[0]==1:
            anchor="clothes"
            clothes.menu()
class skin():

    def menu():
        global colour
        screen.fill((255,255,255))
        screen.blit(bar,rect["skin"]["bar"][:2])
        screen.blit(options["back"],rect["skin"]["back"][:2])

        # img["head"].fill(Color(255,255,255)-colour, special_flags=BLEND_SUB)
        # img["hands"].fill(Color(255,255,255)-colour, special_flags=BLEND_SUB)
        # default.head=default.head.copy()
        # default.hands=default.hands.copy()
        default.head.fill(Color(255,255,255)-colour, special_flags=BLEND_SUB)
        default.hands.fill(Color(255,255,255)-colour, special_flags=BLEND_SUB)
        # default.head=img["head"].copy()
        # default.hands=img["hands"].copy()

        current.draw(default,(476,157))
        # screen.blit()
    def check():
        global colour,anchor
        if Rect(rect["skin"]["bar"]).collidepoint(mx,my) and mb[0]==1:
            colour=screen.get_at((mx,my))
            print(colour)
            skin.menu()
        if Rect(rect["skin"]["back"]).collidepoint(mx,my) and mb[0]==1:
            anchor="intro"

class hair():
    def menu():
        screen.fill((255,255,255))
        screen.blit(bar,(478,298))


    def check():
        global anchor,colour
        if Rect(rect["hair"]["hair"]).collidepoint(mx,my) and mb[0]==1:
            hair.updatehair()
        elif Rect(rect["hair"]["bar"]).collidepoint(mx,my) and mb[0]==1:
            hair.updatecolour()
        elif Rect(rect["hair"]["back"]).collidepoint(mx,my) and mb[0]==1:
            anchor="intro"
            intro.menu()



    def updatehair():
        global counter,colour,h
        counter += 1
        try:
            screen.fill((255, 255, 255))
            screen.blit(bar, (478,298))
            screen.blit(andy.render(names[counter], 1, (0, 0, 0)), (499,208))
            h = hair[counter].subsurface(0, 0, 40, 56).copy()
            h.fill(Color(255,255,255)-colour, special_flags=BLEND_SUB)
            default.hair=h
            current.draw(default,(530,65))
            # screen.blit(h, (530,65))
        except IndexError:
            counter=0

    def updatecolour():
        global counter, colour, text
        colour = screen.get_at((mx, my))
        screen.fill((255, 255, 255))
        screen.blit(bar, (478, 298))
        screen.blit(andy.render(names[counter], 1, (0, 0, 0)), (499, 208))
        h = img["hair"][counter].subsurface(0, 0, 40, 56).copy()
        h.fill(Color(255, 255, 255) - colour, special_flags=BLEND_SUB)
        # screen.blit(h, (530, 65))
class clothes():
    def menu():
        screen.fill((255,255,255))
        # screen.blit(bar,)
    def check():
        global anchor,colour
        if Rect(rect["clothes"]["bar"]).collidepoint(mx,my):
            colour= screen.get_at((mx, my))
            clothes.menu()
        elif Rect(rect["clothes"]["back"]).collidepoint(mx,my):
            anchor="intro"
            intro.menu()



running= True

screen.blit(bar,(478,298))
screen.blit(andy.render(names[counter],1,(0,0,0)),(499,208))
screen.blit(h,(530,65))
intro()
# screen.blit()
while running:
    leftClick=False
    rightClick=False
    mx, my = mouse.get_pos()
    mb = mouse.get_pressed()

    if anchor=="intro":
        intro.menu()

        intro.check()
    elif anchor=="hair":
        hair.check()
    elif anchor=="skin":
        skin.check()
    elif anchor=="clothes":
        clothes.check()
    # print(mx,my)
    # if barRect.collidepoint(mx,my) and mb[0]==1:
    #     updatecolour()
    #
    # if textRect.collidepoint(mx,my) and mb[0]==1:
    #     hair.updatehair()

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


