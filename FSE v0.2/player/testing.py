from pygame import *
init()     #Initialzie directly after importing to avoid module conflicts
from glob import glob
img={"hair":[],
     "head":image.load("Player_Head.png").subsurface(0,0,40,56).copy(),
     "undershirt":image.load("Player_Undershirt.png").subsurface(0,0,40,56).copy(),
     "shirt":image.load("Player_Shirt.png").subsurface(0,0,40,56).copy(),
     "pants":image.load("Player_Pants.png").subsurface(0,0,40,56).copy(),
     "shoes":image.load("Player_Shoes.png").subsurface(0,0,40,56).copy(),
     "hands":image.load("Player_Hands.png").subsurface(0,0,40,56).copy(),
     "eye1":image.load("Player_Eye1.png").subsurface(0,0,40,56).copy(),
     "eye2":image.load("Player_Eye2.png").subsurface(0,0,40,56).copy(),
     }
colour={"hair":Color(171,181,198),
        "skin":Color(171,181,198),
        "pants":Color(171,181,198),
        "shoes":Color(171,181,198),
        "shirt":Color(171,181,198),
        "undershirt":Color(171,181,198),
        "eye":Color(171,181,198),
        }
names=[]    #Used for hair number.

anchor="intro"
x=glob("hair/*.png") #Temperory Variable


for i,j in zip(x,range(1,len(x)+1)):
    names.append("Hair {0}".format(j))
    img["hair"].append(image.load(i).subsurface(0,0,40,56).copy())
del x
screen=display.set_mode((1248,704))
screen.fill((255,255,255))

bar=image.load("Hue.png")
andy=font.Font("HW ANDY.ttf",50)
clock=time.Clock()
counter=0  #Used to control what hair to use
# text=andy.render(names[counter],1,colour)
# h=transform.scale(transform.chop(hair[counter],(0,0,40,56)),(200,280))
# h=transform.chop(hair[counter],(0,0,40,56)).convert_alpha()
# h=transform.scale(hair[counter],(400,7840))
# h=img["hair"][counter].copy()
# h.fill(Color(255,255,255)-colour, special_flags=BLEND_SUB)
rect={"intro":{"body":(447,22,40,56),"hair":(440,121,78,61),"eye":(440,186,87,61),"skin":(440,251,83,61),"clothes":(440,360,138,61),"create":(455,532,121,61)},
      "hair":{"hair":(499,208,40,56),"bar":(478,298,178,16),"back":(511,491,93,61)},
      "eye":{"bar":(535,180,178,16),"back":(478,549,93,61)},
      "clothes":{"bar":(428,182,178,16),"back":(478,549,93,61),"shirt":(485,140,94,61),"undershirt":(485,215,203,61),"pants":(485,290,104,61),"shoes":(485,365,105,61)},
      "skin":{"bar":(478,298,178,16),"back":(478,474,93,61)},
      "shirt":{"back":(511,491,93,61)},
      "undershirt":{"back":(511,491,93,61)},
      "pants":{"back":(511,491,93,61)},
      "shoes":{"back":(511,491,93,61)}
      }  #Two dimensional dictionary
options={"hair":andy.render("Hair",1,(0,0,0)),"skin":andy.render("Skin",1,(0,0,0)),"clothes":andy.render("Clothes",1,(0,0,0)),
         "back":andy.render("Back",1,(0,0,0)),"create":andy.render("Create",1,(0,0,0)),"shirt":andy.render("Shirt",1,(0,0,0)),
         "undershirt":andy.render("Undershirt",1,(0,0,0)),"pants":andy.render("Pants",1,(0,0,0)),
         "shoes":andy.render("Shoes",1,(0,0,0)),"eye":andy.render("Eyes",1,(0,0,0))}

#--------------------------RECT---------------------------------
# textRect=Rect((499,208),text.get_size())
barRect=Rect((478,298),bar.get_size())
#-----------------------------------------------------------------
class current():
    def __init__(self,head,hair,undershirt,shirt,pants,shoes,hands,eye):
        self.head=head
        self.hair=hair
        self.undershirt=undershirt
        self.shirt=shirt
        self.pants=pants
        self.shoes=shoes
        self.hands=hands
        self.eye1=img["eye1"].copy()
        self.eye2=eye
    def draw(bg,self, pos):
        bg.blit(self.head,pos)
        bg.blit(self.eye1,pos)
        bg.blit(self.eye2,pos)
        bg.blit(self.hair,pos)
        bg.blit(self.undershirt,pos)
        bg.blit(self.shirt,pos)
        bg.blit(self.pants,pos)
        bg.blit(self.shoes,pos)
        bg.blit(self.hands,pos)
        #print("Finish drawing")

# img["head"].fill(Color(255,255,255)-colour, special_flags=BLEND_SUB)
# img["undershirt"].fill(Color(255,255,255)-colour, special_flags=BLEND_SUB)
# img["shirt"].fill(Color(255,255,255)-colour, special_flags=BLEND_SUB)
# img["pants"].fill(Color(255,255,255)-colour, special_flags=BLEND_SUB)
# img["shoes"].fill(Color(255,255,255)-colour, special_flags=BLEND_SUB)
# img["hands"].fill(Color(255,255,255)-colour, special_flags=BLEND_SUB)
x=[img["head"].copy(),img["hair"][counter].copy(),img["undershirt"].copy()
,img["shirt"].copy()
,img["pants"].copy()
,img["shoes"].copy()
,img["hands"].copy(),img["eye2"]]
for i in x:
    i.fill(Color(255,255,255)-colour["hair"], special_flags=BLEND_SUB)
default=current(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7])


class intro():  #A class used for bliting the entire body

    def menu():
        screen.fill((255,255,255))
        current.draw(screen,default,rect["intro"]["body"][:2])
        screen.blit(options["hair"],rect["intro"]["hair"][:2])
        screen.blit(options["eye"],rect["intro"]["eye"][:2])
        screen.blit(options["skin"], rect["intro"]["skin"][:2])
        screen.blit(options["clothes"], rect["intro"]["clothes"][:2])
        screen.blit(options["create"],rect["intro"]["create"][:2])
        #screen.blit(options["create"],)
    def check():
        global anchor
        if Rect(rect["intro"]["hair"]).collidepoint(mx,my) and mb[0]==1:
            anchor="hair"
            hair.menu()
        elif Rect(rect["intro"]["eye"]).collidepoint(mx,my) and mb[0]==1:
            anchor="eye"
            eye.menu()

        elif Rect(rect["intro"]["skin"]).collidepoint(mx,my) and mb[0]==1:
            anchor="skin"
            skin.menu()

        elif Rect(rect["intro"]["clothes"]).collidepoint(mx,my) and mb[0]==1:
            anchor="clothes"
            clothes.menu()
        elif Rect(rect["intro"]["create"]).collidepoint(mx,my) and mb[0]==1:
            create()
class eye():
    def menu():
        global colour
        screen.fill((255,255,255))
        screen.blit(bar,rect["eye"]["bar"][:2])
        screen.blit(options["back"],rect["eye"]["back"][:2])
        temp = img["eye2"].copy()
        temp.fill(Color(255, 255, 255) - colour["eye"], special_flags=BLEND_SUB)
        default.eye2 = temp
        current.draw(screen,default, (530, 65))
        # screen.blit(options["back"], rect["eye"]["back"][:2])
        # current.draw(default, (530, 65))
    def check():
        global anchor, colour
        if Rect(rect["eye"]["bar"]).collidepoint(mx,my) and mb[0]==1:
            colour["eye"]=screen.get_at((mx,my))
            eye.menu()
        elif Rect(rect["eye"]["back"]).collidepoint(mx,my) and mb[0]==1:
            anchor="intro"
            intro.menu()

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

        default.head=img["head"].copy()
        default.hands=img["hands"].copy()
        default.hands.fill(Color(255, 255, 255) - colour["skin"], special_flags=BLEND_SUB)
        default.head.fill(Color(255,255,255)-colour["skin"], special_flags=BLEND_SUB)


        current.draw(screen,default,(476,157))

    def check():
        global colour,anchor
        if Rect(rect["skin"]["bar"]).collidepoint(mx,my) and mb[0]==1:
            colour["skin"]=screen.get_at((mx,my))
            skin.menu()
        elif Rect(rect["skin"]["back"]).collidepoint(mx,my) and mb[0]==1:
            anchor="intro"

class hair():
    def menu():
       # global counter
        screen.fill((255,255,255))
        screen.blit(bar,rect["hair"]["bar"][:2])
        screen.blit(andy.render(names[counter], 1, (0, 0, 0)), (499, 208))

        temp = img["hair"][counter].copy()
        temp.fill(Color(255, 255, 255) - colour["hair"], special_flags=BLEND_SUB)
        default.hair = temp
        current.draw(screen,default, (530, 65))
        screen.blit(options["back"],rect["hair"]["back"][:2])


    def check():
        global anchor,colour,counter

        textRect=Rect((499,208),andy.render(names[counter],1,(0,0,0)).get_size())
        if textRect.collidepoint(mx,my) and mb[0]==1:
            counter+=1
            hair.menu()
        elif Rect(rect["hair"]["bar"]).collidepoint(mx,my) and mb[0]==1:
            colour["hair"]=screen.get_at((mx,my))
            hair.menu()

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
            h = hair[counter].copy()
            h.fill(Color(255,255,255)-colour, special_flags=BLEND_SUB)
            default.hair=h
            current.draw(screen,default,(530,65))
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
        screen.blit(options["shirt"], rect["clothes"]["shirt"][:2])
        screen.blit(options["undershirt"], rect["clothes"]["undershirt"][:2])
        screen.blit(options["pants"], rect["clothes"]["pants"][:2])
        screen.blit(options["shoes"],rect["clothes"]["shoes"][:2])
        #screen.blit(bar,rect["clothes"]["bar"][:2])
        screen.blit(options["back"],rect["clothes"]["back"][:2])
        current.draw(screen,default,(480,18))
        # screen.blit(bar,)
    def check():
        global anchor
        # if Rect(rect["clothes"]["bar"]).collidepoint(mx,my):
        #     colour= screen.get_at((mx, my))
        #     clothes.menu()
        if Rect(rect["clothes"]["back"]).collidepoint(mx,my) and mb[0]==1:
            anchor="intro"
            intro.menu()
        elif Rect(rect["clothes"]["shirt"]).collidepoint(mx,my) and mb[0]==1 :
            anchor="shirt"
            shirt.menu()
        elif Rect(rect["clothes"]["undershirt"]).collidepoint(mx, my) and mb[0]==1:
            anchor = "undershirt"
            undershirt.menu()
        elif Rect(rect["clothes"]["pants"]).collidepoint(mx, my) and mb[0]==1:
            anchor = "pants"
            pants.menu()
        elif Rect(rect["clothes"]["shoes"]).collidepoint(mx, my) and mb[0]==1:
            anchor = "shoes"
            shoes.menu()



class shirt():
    def menu():
        screen.fill((255,255,255))
        screen.blit(bar,rect["clothes"]["bar"][:2])
        screen.blit(options["back"],rect["shirt"]["back"][:2])
        temp = img["shirt"].copy()
        temp.fill(Color(255, 255, 255) - colour["shirt"], special_flags=BLEND_SUB)
        default.shirt = temp
        current.draw(screen,default, (530, 65))

    def check():
        global anchor
        if Rect(rect["shirt"]["back"]).collidepoint(mx,my) and mb[0]==1:
            anchor="clothes"
            clothes.menu()
        elif Rect(rect["clothes"]["bar"]).collidepoint(mx,my) and mb[0]==1:
            colour["shirt"]=screen.get_at((mx,my))
            shirt.menu()
class undershirt():
    def menu():
        screen.fill((255, 255, 255))
        screen.blit(bar, rect["clothes"]["bar"][:2])
        screen.blit(options["back"], rect["undershirt"]["back"][:2])
        temp = img["undershirt"].copy()
        temp.fill(Color(255, 255, 255) - colour["undershirt"], special_flags=BLEND_SUB)
        default.undershirt = temp
        current.draw(screen,default, (530, 65))
    def check():
        global colour,anchor
        if Rect(rect["clothes"]["bar"]).collidepoint(mx,my) and mb[0]==1:
            colour["undershirt"]=screen.get_at((mx,my))
            undershirt.menu()
        elif Rect(rect["undershirt"]["back"]).collidepoint(mx,my) and mb[0]==1:
            anchor="clothes"
            clothes.menu()

class pants():
    def menu():
        screen.fill((255,255,255))
        screen.blit(bar, rect["clothes"]["bar"][:2])
        screen.blit(options["back"], rect["pants"]["back"][:2])
        temp = img["pants"].copy()
        temp.fill(Color(255, 255, 255) - colour["pants"], special_flags=BLEND_SUB)
        default.pants = temp
        current.draw(screen,default, (530, 65))
    def check():
        global colour,anchor
        if Rect(rect["clothes"]["bar"]).collidepoint(mx,my) and mb[0]==1:
            # print("YA")
            colour["pants"]=screen.get_at((mx,my))
            pants.menu()
        elif Rect(rect["pants"]["back"]).collidepoint(mx,my) and mb[0]==1:
            anchor="clothes"
            clothes.menu()
class shoes():
    def menu():
        screen.fill((255, 255, 255))
        screen.blit(bar, rect["clothes"]["bar"][:2])
        screen.blit(options["back"], rect["shoes"]["back"][:2])
        temp = img["shoes"].copy()
        temp.fill(Color(255, 255, 255) - colour["shoes"], special_flags=BLEND_SUB)
        default.shoes = temp
        current.draw(screen,default, (530, 65))
    def check():
        global colour,anchor
        if Rect(rect["clothes"]["bar"]).collidepoint(mx,my) and mb[0]==1:
            colour["shoes"]=screen.get_at((mx,my))
            shoes.menu()
        elif Rect(rect["pants"]["back"]).collidepoint(mx,my) and mb[0]==1:
            anchor="clothes"
            clothes.menu()
def create():
    bg=Surface((40,1120))
    for i in range(0,1121,56):
        current.draw(bg,default,(0,i))
    image.save(bg,"Sprite.png")

running= True

# screen.blit(bar,(478,298))
# screen.blit(andy.render(names[counter],1,(0,0,0)),(499,208))
# screen.blit(h,(530,65))
intro()
# screen.blit()
while running:
    leftClick=False
    rightClick=False
    mx, my = mouse.get_pos()
    mb = mouse.get_pressed()
    print(mx,my)
    if anchor=="intro":
        intro.menu()
        intro.check()
    elif anchor=="hair":
        hair.check()
    elif anchor=="skin":
        skin.check()
    elif anchor=="clothes":
        clothes.check()
    elif anchor=="shirt":
        shirt.check()
    elif anchor=="undershirt":
        undershirt.check()
    elif anchor=="pants":
        pants.check()
    elif anchor=="shoes":
        shoes.check()
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


