'''
This program allows user to customize the player in the game.
It allows the player to change the eye colour,skin colour,hair style, hair colour and particular clothes.

'''
from pygame import *

init()  # Initialzie directly after importing to avoid module conflicts
import os #Used as a substitute for glob

img = {"hair": [],
       "head": image.load("player/Player_Head.png").subsurface(0, 0, 40, 56).copy(),
       "undershirt": image.load("player/Player_Undershirt.png").subsurface(0, 0, 40, 56).copy(),
       "shirt": image.load("player/Player_Shirt.png").subsurface(0, 0, 40, 56).copy(),
       "pants": image.load("player/Player_Pants.png").subsurface(0, 0, 40, 56).copy(),
       "shoes": image.load("player/Player_Shoes.png").subsurface(0, 0, 40, 56).copy(),
       "hands": image.load("player/Player_Hands.png").subsurface(0, 0, 40, 56).copy(),
       "eye1": image.load("player/Player_0_1.png").subsurface(0, 0, 40, 56).copy(),
       "eye2": image.load("player/Player_0_2.png").subsurface(0, 0, 40, 56).copy(),
       }
#loading images
colour = {"hair": Color(63, 37, 11),
          "skin": Color(232, 219, 136),
          "pants": Color(40, 40, 40),
          "shoes": Color(25, 38, 114),
          "shirt": Color(201, 26, 34),
          "undershirt": Color(171, 181, 198),
          "eye": Color(65, 136, 160),
          }  #Set default colour for parts of the body
names = []  # Used for hair style since there are many hair styles, this stores the name of the hair style, such as "hair1"

anchor = "intro"         #Anchor is an indicator of which interface the user's in.


x = [file for file in os.listdir("player/hair")]  # x is a temporary variable that stores all the hair file names. os.listdir() is similar to glob.glob()
for i, j in zip(x, range(1, len(x) + 1)):
    names.append("Hair {0}".format(j))
    img["hair"].append(image.load("player/hair/" + i).subsurface(0, 0, 40, 56).copy())

del x
screen = display.set_mode((1248, 704))
screen.fill((255, 255, 255))

background = transform.scale(image.load("images/background.png"), (1248, 704))
background.set_alpha(100)
bar = image.load("player/Hue.png")
andy = font.Font("player/HW ANDY.ttf", 50)
clock = time.Clock()
counter = 0  # Used to control what hair to use

rect = {"intro": {"body": (604, 22, 40, 56), "hair": (585, 121, 78, 61), "eye": (580, 186, 87, 61),
                  "skin": (582.5, 251, 83, 61), "clothes": (555, 316, 138, 61), "create": (563.5, 532, 121, 61)},
        "hair": {"hair": (568, 208, 40, 56), "bar": (535, 298, 178, 16), "back": (577.5, 491, 93, 61)},
        "eye": {"bar": (535, 180, 178, 16), "back": (577.5, 549, 93, 61)},
        "clothes": {"bar": (535, 182, 178, 16), "back": (577.5, 549, 93, 61), "shirt": (577, 140, 94, 61),
                    "undershirt": (522.5, 215, 203, 61), "pants": (572, 290, 104, 61), "shoes": (568, 365, 105, 61)},
        "skin": {"bar": (535, 298, 178, 16), "back": (577.5, 474, 93, 61)},
        "shirt": {"back": (577.5, 491, 93, 61)},
        "undershirt": {"back": (577.5, 491, 93, 61)},
        "pants": {"back": (577.5, 491, 93, 61)},
        "shoes": {"back": (577.5, 491, 93, 61)}
        }  # Two dimensional dictionary to store all the rect for more convenience
options = {"hair": andy.render("Hair", 1, (200,200,200)), "skin": andy.render("Skin", 1, (200,200,200)),
           "clothes": andy.render("Clothes", 1, (200,200,200)),
           "back": andy.render("Back", 1, (200,200,200)), "create": andy.render("Create", 1, (200,200,200)),
           "shirt": andy.render("Shirt", 1, (200,200,200)),
           "undershirt": andy.render("Undershirt", 1, (200,200,200)), "pants": andy.render("Pants", 1, (200,200,200)),
           "shoes": andy.render("Shoes", 1, (200,200,200)), "eye": andy.render("Eyes", 1, (200,200,200))}
# options is a dictionary storing all the text surface



class current():  #current is a class that is dedicated to draw to the person on the screen.
    def __init__(self, head, hair, undershirt, shirt, pants, shoes, hands, eye):
        self.head = head
        self.hair = hair
        self.undershirt = undershirt
        self.shirt = shirt
        self.pants = pants
        self.shoes = shoes
        self.hands = hands
        self.eye1 = img["eye1"].copy()
        self.eye2 = eye

    def draw(bg, self, pos):   #the draw function draws the person at pos in order.
        bg.blit(self.head, pos)
        bg.blit(self.eye1, pos)
        bg.blit(self.eye2, pos)
        bg.blit(self.hair, pos)
        bg.blit(self.undershirt, pos)
        bg.blit(self.shirt, pos)
        bg.blit(self.pants, pos)
        bg.blit(self.shoes, pos)
        bg.blit(self.hands, pos)


# Space for readibility


x = [img["head"].copy(), img["hair"][counter].copy(), img["undershirt"].copy()
    , img["shirt"].copy()
    , img["pants"].copy()
    , img["shoes"].copy()
    , img["hands"].copy(), img["eye2"]]

x[0].fill(Color(255, 255, 255) - colour["skin"], special_flags=BLEND_SUB)
x[1].fill(Color(255, 255, 255) - colour["hair"], special_flags=BLEND_SUB)
x[2].fill(Color(255, 255, 255) - colour["undershirt"], special_flags=BLEND_SUB)
x[3].fill(Color(255, 255, 255) - colour["shirt"], special_flags=BLEND_SUB)
x[4].fill(Color(255, 255, 255) - colour["pants"], special_flags=BLEND_SUB)
x[5].fill(Color(255, 255, 255) - colour["shoes"], special_flags=BLEND_SUB)
x[6].fill(Color(255, 255, 255) - colour["skin"], special_flags=BLEND_SUB)
x[7].fill(Color(255, 255, 255) - colour["eye"], special_flags=BLEND_SUB)
#Setting the default color for each body part or clothes
default = current(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7])  # default is an instance of the class. It is a representation of the person the user is manipulating
'''
The classes used below work similarly.
The menu fucntion draws the interface while the check the function check for mouse collision
'''

class intro():  # The interface

    def menu():      #This draws the menu
        screen.fill((0, 0, 0)) #fills black screen first
        screen.blit(background, (0, 0)) #background is translucent: gives cool effect
        current.draw(screen, default, rect["intro"]["body"][:2])

        screen.blit(options["hair"], rect["intro"]["hair"][:2]) #blitting text options on screen
        screen.blit(options["eye"], rect["intro"]["eye"][:2])
        screen.blit(options["skin"], rect["intro"]["skin"][:2])
        screen.blit(options["clothes"], rect["intro"]["clothes"][:2])
        screen.blit(options["create"], rect["intro"]["create"][:2])


    def check():
        global anchor #the anchor changes based on what you click
        if Rect(rect["intro"]["hair"]).collidepoint(mx, my) and mb[0] == 1:
            anchor = "hair"
            hair.menu()
        elif Rect(rect["intro"]["eye"]).collidepoint(mx, my) and mb[0] == 1:
            anchor = "eye"
            eye.menu()

        elif Rect(rect["intro"]["skin"]).collidepoint(mx, my) and mb[0] == 1:
            anchor = "skin"
            skin.menu()

        elif Rect(rect["intro"]["clothes"]).collidepoint(mx, my) and mb[0] == 1:
            anchor = "clothes"
            clothes.menu()
        elif Rect(rect["intro"]["create"]).collidepoint(mx, my) and mb[0] == 1:
            create()


class eye():
    def menu():
        global colour
        screen.fill((0, 0, 0)) #fills black
        screen.blit(background, (0, 0)) #adjusted alpha on background
        screen.blit(bar, rect["eye"]["bar"][:2]) #blits if eye is selected
        screen.blit(options["back"], rect["eye"]["back"][:2])
        temp = img["eye2"].copy()
        temp.fill(Color(255, 255, 255) - colour["eye"], special_flags=BLEND_SUB)
        default.eye2 = temp
        current.draw(screen, default, (604, 65)) # Calling the drawing function to draw the person at position (604,55)


    def check():
        global anchor, colour
        if Rect(rect["eye"]["bar"]).collidepoint(mx, my) and mb[0] == 1:
            colour["eye"] = screen.get_at((mx, my))
            eye.menu()
        elif Rect(rect["eye"]["back"]).collidepoint(mx, my) and mb[0] == 1:
            anchor = "intro"
            intro.menu()


class skin():
    def menu():
        global colour
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        screen.blit(bar, rect["skin"]["bar"][:2])
        screen.blit(options["back"], rect["skin"]["back"][:2])

        default.head = img["head"].copy()
        default.hands = img["hands"].copy()
        default.hands.fill(Color(255, 255, 255) - colour["skin"], special_flags=BLEND_SUB)
        default.head.fill(Color(255, 255, 255) - colour["skin"], special_flags=BLEND_SUB)

        current.draw(screen, default, (604, 157))

    def check():
        global colour, anchor
        if Rect(rect["skin"]["bar"]).collidepoint(mx, my) and mb[0] == 1:
            colour["skin"] = screen.get_at((mx, my))
            skin.menu()
        elif Rect(rect["skin"]["back"]).collidepoint(mx, my) and mb[0] == 1:
            anchor = "intro"


class hair():
    def menu():
        # global counter
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        screen.blit(bar, rect["hair"]["bar"][:2])
        screen.blit(andy.render(names[counter], 1, (200,200,200)), (568, 208))

        temp = img["hair"][counter].copy()
        temp.fill(Color(255, 255, 255) - colour["hair"], special_flags=BLEND_SUB)
        default.hair = temp
        current.draw(screen, default, (604, 65))
        screen.blit(options["back"], rect["hair"]["back"][:2])

    def check():
        global anchor, colour, counter

        textRect = Rect((499, 208), andy.render(names[counter], 1, (0, 0, 0)).get_size())
        if textRect.collidepoint(mx, my) and mb[0] == 1:
            counter += 1
            hair.menu()
        elif Rect(rect["hair"]["bar"]).collidepoint(mx, my) and mb[0] == 1:
            colour["hair"] = screen.get_at((mx, my))
            hair.menu()

        elif Rect(rect["hair"]["back"]).collidepoint(mx, my) and mb[0] == 1:
            anchor = "intro"
            intro.menu()

    

class clothes():
    def menu():
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        screen.blit(options["shirt"], rect["clothes"]["shirt"][:2])
        screen.blit(options["undershirt"], rect["clothes"]["undershirt"][:2])
        screen.blit(options["pants"], rect["clothes"]["pants"][:2])
        screen.blit(options["shoes"], rect["clothes"]["shoes"][:2])
        # screen.blit(bar,rect["clothes"]["bar"][:2])
        screen.blit(options["back"], rect["clothes"]["back"][:2])
        current.draw(screen, default, (604, 18))
        # screen.blit(bar,)

    def check():
        global anchor

        if Rect(rect["clothes"]["back"]).collidepoint(mx, my) and mb[0] == 1:
            anchor = "intro"
            intro.menu()
        elif Rect(rect["clothes"]["shirt"]).collidepoint(mx, my) and mb[0] == 1:
            anchor = "shirt"
            shirt.menu()
        elif Rect(rect["clothes"]["undershirt"]).collidepoint(mx, my) and mb[0] == 1:
            anchor = "undershirt"
            undershirt.menu()
        elif Rect(rect["clothes"]["pants"]).collidepoint(mx, my) and mb[0] == 1:
            anchor = "pants"
            pants.menu()
        elif Rect(rect["clothes"]["shoes"]).collidepoint(mx, my) and mb[0] == 1:
            anchor = "shoes"
            shoes.menu()


class shirt():
    def menu():
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        screen.blit(bar, rect["clothes"]["bar"][:2])
        screen.blit(options["back"], rect["shirt"]["back"][:2])
        temp = img["shirt"].copy()
        temp.fill(Color(255, 255, 255) - colour["shirt"], special_flags=BLEND_SUB)
        default.shirt = temp
        current.draw(screen, default, (604, 65))

    def check():
        global anchor
        if Rect(rect["shirt"]["back"]).collidepoint(mx, my) and mb[0] == 1:
            anchor = "clothes"
            clothes.menu()
        elif Rect(rect["clothes"]["bar"]).collidepoint(mx, my) and mb[0] == 1:
            colour["shirt"] = screen.get_at((mx, my))
            shirt.menu()


class undershirt():
    def menu():
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        screen.blit(bar, rect["clothes"]["bar"][:2])
        screen.blit(options["back"], rect["undershirt"]["back"][:2])
        temp = img["undershirt"].copy()
        temp.fill(Color(255, 255, 255) - colour["undershirt"], special_flags=BLEND_SUB)
        default.undershirt = temp
        current.draw(screen, default, (604, 65))

    def check():
        global colour, anchor
        if Rect(rect["clothes"]["bar"]).collidepoint(mx, my) and mb[0] == 1:
            colour["undershirt"] = screen.get_at((mx, my))
            undershirt.menu()
        elif Rect(rect["undershirt"]["back"]).collidepoint(mx, my) and mb[0] == 1:
            anchor = "clothes"
            clothes.menu()


class pants():
    def menu():
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        screen.blit(bar, rect["clothes"]["bar"][:2])
        screen.blit(options["back"], rect["pants"]["back"][:2])
        temp = img["pants"].copy()
        temp.fill(Color(255, 255, 255) - colour["pants"], special_flags=BLEND_SUB)
        default.pants = temp
        current.draw(screen, default, (604, 65))

    def check():
        global colour, anchor
        if Rect(rect["clothes"]["bar"]).collidepoint(mx, my) and mb[0] == 1:
            # print("YA")
            colour["pants"] = screen.get_at((mx, my))
            pants.menu()
        elif Rect(rect["pants"]["back"]).collidepoint(mx, my) and mb[0] == 1:
            anchor = "clothes"
            clothes.menu()


class shoes():
    def menu():
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        screen.blit(bar, rect["clothes"]["bar"][:2])
        screen.blit(options["back"], rect["shoes"]["back"][:2])
        temp = img["shoes"].copy()
        temp.fill(Color(255, 255, 255) - colour["shoes"], special_flags=BLEND_SUB)
        default.shoes = temp
        current.draw(screen, default, (604, 65))

    def check():
        global colour, anchor
        if Rect(rect["clothes"]["bar"]).collidepoint(mx, my) and mb[0] == 1:
            colour["shoes"] = screen.get_at((mx, my))
            shoes.menu()
        elif Rect(rect["pants"]["back"]).collidepoint(mx, my) and mb[0] == 1:
            anchor = "clothes"
            clothes.menu()


def create():   #A function made for saving the entire person and used it in the game.
    
    bg = Surface((40, 1120), SRCALPHA)  # A surface used to save with the entire person.
    bg2 = Surface((40, 1120), SRCALPHA)  # A surface used to save with onlt the alternative hands.

    for i in range(0, 1120, 56):
        save = []

        if i != 1064:   #Some images have differnet height. This prevents error from subsurface out of boundary of the original surface.
            save.append(image.load("player/Player_Head.png").subsurface(0, i, 40, 56).copy())
            save.append(img["hair"][counter].copy())

            save.append(image.load("player/Player_Undershirt.png").subsurface(0, i, 40, 56).copy())
            save.append(image.load("player/Player_Shirt.png").subsurface(0, i, 40, 56).copy())
            save.append(image.load("player/Player_Pants.png").subsurface(0, i, 40, 56).copy())
            save.append(image.load("player/Player_Shoes.png").subsurface(0, i, 40, 56).copy())
            save.append(image.load("player/Player_Hands.png").subsurface(0, i, 40, 56).copy())
            save.append(image.load("player/Player_Eye2.png").subsurface(0, i, 40, 56).copy())
            hand2 = image.load("player/Player_Hands2.png").subsurface(0, i, 40, 56).copy()

            save[0].fill(Color(255, 255, 255) - colour["skin"], special_flags=BLEND_SUB)
            save[1].fill(Color(255, 255, 255) - colour["hair"], special_flags=BLEND_SUB)
            save[2].fill(Color(255, 255, 255) - colour["undershirt"], special_flags=BLEND_SUB)
            save[3].fill(Color(255, 255, 255) - colour["shirt"], special_flags=BLEND_SUB)
            save[4].fill(Color(255, 255, 255) - colour["pants"], special_flags=BLEND_SUB)
            save[5].fill(Color(255, 255, 255) - colour["shoes"], special_flags=BLEND_SUB)
            save[6].fill(Color(255, 255, 255) - colour["skin"], special_flags=BLEND_SUB)
            save[7].fill(Color(255, 255, 255) - colour["eye"], special_flags=BLEND_SUB)
            hand2.fill(Color(255, 255, 255) - colour["skin"], special_flags=BLEND_SUB)


        else:
            save.append(image.load("player/Player_Head.png").subsurface(0, i, 40, 54).copy())
            save.append(img["hair"][counter].copy())
            save.append(image.load("player/Player_Undershirt.png").subsurface(0, i, 40, 54).copy())
            save.append(image.load("player/Player_Shirt.png").subsurface(0, i, 40, 54).copy())
            save.append(image.load("player/Player_Pants.png").subsurface(0, i, 40, 56).copy())
            save.append(image.load("player/Player_Shoes.png").subsurface(0, i, 40, 54).copy())
            save.append(image.load("player/Player_Hands.png").subsurface(0, i, 40, 54).copy())
            save.append(image.load("player/Player_Eye2.png").subsurface(0, i, 40, 54).copy())
            hand2 = image.load("player/Player_Hands2.png").subsurface(0, i, 40, 54).copy()

            save[0].fill(Color(255, 255, 255) - colour["skin"], special_flags=BLEND_SUB)
            save[1].fill(Color(255, 255, 255) - colour["hair"], special_flags=BLEND_SUB)
            save[2].fill(Color(255, 255, 255) - colour["undershirt"], special_flags=BLEND_SUB)
            save[3].fill(Color(255, 255, 255) - colour["shirt"], special_flags=BLEND_SUB)
            save[4].fill(Color(255, 255, 255) - colour["pants"], special_flags=BLEND_SUB)
            save[5].fill(Color(255, 255, 255) - colour["shoes"], special_flags=BLEND_SUB)
            save[6].fill(Color(255, 255, 255) - colour["skin"], special_flags=BLEND_SUB)
            save[7].fill(Color(255, 255, 255) - colour["eye"], special_flags=BLEND_SUB)
            hand2.fill(Color(255, 255, 255) - colour["skin"], special_flags=BLEND_SUB)

        temp = current(save[0], save[1], save[2], save[3], save[4], save[5], save[6], save[7])
        current.draw(bg, temp, (0, i))

        bg2.blit(hand2, (0, i))
    image.save(bg, "player/Characters/everything1.png")
    out=open("flag.txt","w")  # flag.txt file serves the purpose as a flag so when the user return the menu, it will return back to the previously opened window.
    out.write("1")
    out.close()
    import menu   #Go back to the menu

running = True
intro() #Initialzie the intro window

while running:

    mx, my = mouse.get_pos()
    mb = mouse.get_pressed()

    if anchor == "intro":
        intro.menu()
        intro.check()
    elif anchor == "eye":
        eye.check()
    elif anchor == "hair":
        hair.check()
    elif anchor == "skin":
        skin.check()
    elif anchor == "clothes":
        clothes.check()
    elif anchor == "shirt":
        shirt.check()
    elif anchor == "undershirt":
        undershirt.check()
    elif anchor == "pants":
        pants.check()
    elif anchor == "shoes":
        shoes.check()


    for evt in event.get():
        if evt.type == QUIT:
            running = False
        if evt.type == MOUSEBUTTONDOWN:
            if evt.button == 1:
                leftClick = True
            if evt.button == 3:
                rightClick = True

    display.flip()
    clock.tick(15)

quit()


