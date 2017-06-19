#Terraria/2D Minecraft
#Leo Chen, Tailai Wang, Hamza Saqib
#ICS 3U FSE 2017

"""2/D Minecraft is an open world game where there is no objective whatsorver.
Walk around and experience the world by slaying mobs, building stuff, or
just listening to the ambient music. This program involves classes. Most of our
entities inside the game belong to a class, so take note of the varaible names
for more clarity"""


from random import * #who needs timers??
import numpy as np #numpy arrays
import pickle #very important
from time import time as tm #clocks 
from pygame import * 
import math
import pygame

pygame.init() #sound imports
pygame.mixer.init()
pygame.mixer.pre_init(22050,-16,2,2048)
init() #start the enginessss....
######################################################################
"""Pickle files preserve data in the directory:
these are essential in our program, as everything involves reading
these files"""
with open("world/blockspickle.pickle", "rb") as f:
    blockList = pickle.load(f)

with open("inventory.pickle", "rb") as f:
    inventoryPickleList = pickle.load(f)

with open("world/trees.pickle", "rb") as f:
    treesList = pickle.load(f)

screen = display.set_mode((1280, 720))

andy18 = font.Font("fonts/HW ANDY.ttf", 18) #Terraria fonts
andy16 = font.Font("fonts/HW ANDY.ttf", 16)
andy22 = font.Font("fonts/HW ANDY.ttf", 22)
andy44 = font.Font("fonts/HW ANDY.ttf", 44)
andy58 = font.Font("fonts/HW ANDY.ttf", 58)

clock = time.Clock()

worldSize = (780, 85) #(700x 85 blocks is default)
 
blocksSurface = Surface((worldSize[0] * 16, worldSize[1] * 16), SRCALPHA)
blocksSurface.fill((0, 0, 0, 0)) #transparent
treesSurface = Surface((worldSize[0] * 16, worldSize[1] * 16), SRCALPHA)
treesSurface.fill((0, 0, 0, 0)) #transparent
playerSurface = Surface((worldSize[0] * 16, worldSize[1] * 16), SRCALPHA)
playerSurface.fill((0, 0, 0, 0))#transparent
uiSurface = Surface((1280, 720), SRCALPHA)
mainSurface = Surface((1280, 720), SRCALPHA)
###########################################################################
"""For some weird reason loading images as SRCALPHA makes stuff faster.
We loaded as many images as possible in SRC ALPHA form to economize"""
background1 = transform.scale(image.load("images/Background_1.png").convert(32, SRCALPHA), (1280, 720))
background2 = transform.scale(image.load("images/Background_2.png").convert(32, SRCALPHA), (1280, 720))
background3 = transform.scale(image.load("images/Background_3.png").convert(32, SRCALPHA), (1280, 720))

pics = []
sprite = image.load("player/Characters/everything1.png")

for i in range(0, 1120, 56): #player sprites
    pics.append(sprite.subsurface((0, i, 40, 56)))

for i in range(0, 1120, 56):
    pics.append(transform.flip(sprite.subsurface((0, i, 40, 56)), True, False))

pics = [pics[0:5], [pics[5], pics[5]], pics[6:20], pics[20:25], [pics[25], pics[25]], pics[26:]]

slimePics=[]
for i in range(4): #slime sprites
    name="slime/slime_"+str(i)+".png"
    slimePics.append(image.load(name))

purpleSlimePics = []
for i in range(4): #purple slime sprites
    name="slime/slime2_"+str(i)+".png"
    purpleSlimePics.append(image.load(name))

wizardPics = [[],[],[]] #wizard sprite
for i in range(2):
    name = "wizard/skeleton_"+str(i)+".png"
    wizardPics[0].append(image.load(name))

for i in range(2):
    name = "wizard/skeleton_B_"+str(i)+".png"
    wizardPics[1].append(image.load(name))

wizardPics[2].append(image.load("wizard/fire.png")) #wizard fire 
wizardPics[2].append(image.load("wizard/fire2.png"))

""" Bunch of boring block sprites below here, very boring to set up, even more
boring to read. Each block has 12 different states, dependig on how many
blocks are next to them, and whether theyre breaking or not"""
#/////////////////////////////////////////////////////////////////////////    
tile_crack_1 = image.load("tile_cracks/tile_crack_2.png").convert(32, SRCALPHA)
tile_crack_2 = image.load("tile_cracks/tile_crack_8.png").convert(32, SRCALPHA)
tile_crack_3 = image.load("tile_cracks/tile_crack_14.png").convert(32, SRCALPHA)
tile_crack_4 = image.load("tile_cracks/tile_crack_20.png").convert(32, SRCALPHA)
tile_cracks = [tile_crack_4, tile_crack_3, tile_crack_2, tile_crack_1]
#/////////////////////////////////////////////////////////////////////////
block1_0 = image.load("dirt/dirt_block_19.png").convert(32, SRCALPHA)
block1_1 = image.load("dirt/dirt_block_1.png").convert(32, SRCALPHA)
block1_2 = image.load("dirt/dirt_block_0.png").convert(32, SRCALPHA)
block1_3 = image.load("dirt/dirt_block_4.png").convert(32, SRCALPHA)
block1_4 = image.load("dirt/dirt_block_33.png").convert(32, SRCALPHA)
block1_5 = image.load("dirt/dirt_block_69.png").convert(32, SRCALPHA)
block1_6 = image.load("dirt/dirt_block_68.png").convert(32, SRCALPHA)
block1_7 = image.load("dirt/dirt_block_37.png").convert(32, SRCALPHA)
block1_8 = image.load("dirt/dirt_block_51.png").convert(32, SRCALPHA)
block1_9 = image.load("dirt/dirt_block_50.png").convert(32, SRCALPHA)
block1_10 = image.load("dirt/dirt_block_70.png").convert(32, SRCALPHA)
block1_11 = image.load("dirt/dirt_block_59.png").convert(32, SRCALPHA)
block1_12 = image.load("dirt/dirt_block_56.png").convert(32, SRCALPHA)
block1_13 = image.load("dirt/dirt_block_8.png").convert(32, SRCALPHA)
block1_14 = image.load("dirt/dirt_block_12.png").convert(32, SRCALPHA)
block1_15 = image.load("dirt/dirt_block_9.png").convert(32, SRCALPHA)
block1 = [block1_0, block1_1, block1_2, block1_3, block1_4, block1_5, block1_6, block1_7, block1_8, block1_9, block1_10,
          block1_11, block1_12, block1_13, block1_14, block1_15]
#///////////////////////////////////////////////////////////////////////////
block2_0 = image.load("stone/stone_block_19.png").convert(32, SRCALPHA)
block2_1 = image.load("stone/stone_block_1.png").convert(32, SRCALPHA)
block2_2 = image.load("stone/stone_block_0.png").convert(32, SRCALPHA)
block2_3 = image.load("stone/stone_block_4.png").convert(32, SRCALPHA)
block2_4 = image.load("stone/stone_block_33.png").convert(32, SRCALPHA)
block2_5 = image.load("stone/stone_block_69.png").convert(32, SRCALPHA)
block2_6 = image.load("stone/stone_block_68.png").convert(32, SRCALPHA)
block2_7 = image.load("stone/stone_block_37.png").convert(32, SRCALPHA)
block2_8 = image.load("stone/stone_block_51.png").convert(32, SRCALPHA)
block2_9 = image.load("stone/stone_block_50.png").convert(32, SRCALPHA)
block2_10 = image.load("stone/stone_block_70.png").convert(32, SRCALPHA)
block2_11 = image.load("stone/stone_block_59.png").convert(32, SRCALPHA)
block2_12 = image.load("stone/stone_block_56.png").convert(32, SRCALPHA)
block2_13 = image.load("stone/stone_block_8.png").convert(32, SRCALPHA)
block2_14 = image.load("stone/stone_block_12.png").convert(32, SRCALPHA)
block2_15 = image.load("stone/stone_block_9.png").convert(32, SRCALPHA)

block2 = [block2_0, block2_1, block2_2, block2_3, block2_4, block2_5, block2_6, block2_7, block2_8, block2_9, block2_10,
          block2_11, block2_12, block2_13, block2_14, block2_15]

block3_0 = image.load("grass/grass_block_19.png").convert(32, SRCALPHA)
block3_1 = image.load("grass/grass_block_1.png").convert(32, SRCALPHA)
block3_2 = image.load("grass/grass_block_0.png").convert(32, SRCALPHA)
block3_3 = image.load("grass/grass_block_4.png").convert(32, SRCALPHA)
block3_4 = image.load("grass/grass_block_33.png").convert(32, SRCALPHA)
block3_5 = image.load("grass/grass_block_69.png").convert(32, SRCALPHA)
block3_6 = image.load("grass/grass_block_68.png").convert(32, SRCALPHA)
block3_7 = image.load("grass/grass_block_37.png").convert(32, SRCALPHA)
block3_8 = image.load("grass/grass_block_51.png").convert(32, SRCALPHA)
block3_9 = image.load("grass/grass_block_50.png").convert(32, SRCALPHA)
block3_10 = image.load("grass/grass_block_70.png").convert(32, SRCALPHA)
block3_11 = image.load("grass/grass_block_59.png").convert(32, SRCALPHA)
block3_12 = image.load("grass/grass_block_56.png").convert(32, SRCALPHA)
block3_13 = image.load("grass/grass_block_8.png").convert(32, SRCALPHA)
block3_14 = image.load("grass/grass_block_12.png").convert(32, SRCALPHA)
block3_15 = image.load("grass/grass_block_9.png").convert(32, SRCALPHA)

block6_0 = image.load("ironore/ironore_block_19.png").convert(32, SRCALPHA)
block6_1 = image.load("ironore/ironore_block_1.png").convert(32, SRCALPHA)
block6_2 = image.load("ironore/ironore_block_0.png").convert(32, SRCALPHA)
block6_3 = image.load("ironore/ironore_block_4.png").convert(32, SRCALPHA)
block6_4 = image.load("ironore/ironore_block_33.png").convert(32, SRCALPHA)
block6_5 = image.load("ironore/ironore_block_69.png").convert(32, SRCALPHA)
block6_6 = image.load("ironore/ironore_block_68.png").convert(32, SRCALPHA)
block6_7 = image.load("ironore/ironore_block_37.png").convert(32, SRCALPHA)
block6_8 = image.load("ironore/ironore_block_51.png").convert(32, SRCALPHA)
block6_9 = image.load("ironore/ironore_block_50.png").convert(32, SRCALPHA)
block6_10 = image.load("ironore/ironore_block_70.png").convert(32, SRCALPHA)
block6_11 = image.load("ironore/ironore_block_59.png").convert(32, SRCALPHA)
block6_12 = image.load("ironore/ironore_block_56.png").convert(32, SRCALPHA)
block6_13 = image.load("ironore/ironore_block_8.png").convert(32, SRCALPHA)
block6_14 = image.load("ironore/ironore_block_12.png").convert(32, SRCALPHA)
block6_15 = image.load("ironore/ironore_block_9.png").convert(32, SRCALPHA)

block6 = [block6_0, block6_1, block6_2, block6_3, block6_4, block6_5, block6_6, block6_7, block6_8, block6_9, block6_10,
          block6_11, block6_12, block6_13, block6_14, block6_15]

block7_0 = image.load("tree/trunks/tree_trunk_0.png").convert(32, SRCALPHA)
block7_1 = image.load("tree/trunks/tree_trunk_49.png").convert(32, SRCALPHA)
block7_2 = image.load("tree/trunks/tree_trunk_50.png").convert(32, SRCALPHA)
block7_3 = image.load("tree/trunks/tree_trunk_60.png").convert(32, SRCALPHA)

block8_0 = image.load("tree/tree_branch_3.png").convert(32, SRCALPHA)
block8_1 = image.load("tree/tree_branch_4.png").convert(32, SRCALPHA)

tree_top = image.load("tree/tree_top_0.png").convert(32, SRCALPHA)

block7 = [block7_0, block7_1, block7_2, block7_3]
block8 = [block8_0, block8_1]

#//////////////////////////////////////////////////////////////////////
block3 = [block3_0, block3_1, block3_2, block3_3, block3_4, block3_5, block3_6, block3_7, block3_8, block3_9, block3_10,
          block3_11, block3_12, block3_13, block3_14, block3_15]
blockImg = [False, block1, block2, block3, False, False, block6, block7, block8]
blockConditions = [False, 150, 500, 150, False, False, 575, 450, 450]
#/////////////////////////////////////////////////////////////////////
""" Inventory sprite load in. All of these were found on the Terraria wiki.
Again, we used SRCALPHA to speed things up. We have two lists in action here.
Inventory.pickle keeps track of the player's inventory, and drops list
keeps track of items on the ground"""

item1 = image.load("items/item_1.png").convert(32, SRCALPHA)
item2 = image.load("items/item_2.png").convert(32, SRCALPHA)
item4 = image.load("items/item_4.png").convert(32, SRCALPHA)
item5 = image.load("items/item_5.png").convert(32, SRCALPHA)
item6 = image.load("items/item_6.png").convert(32, SRCALPHA)
item9 = image.load("items/item_9.png").convert(32, SRCALPHA)
inventoryBack = image.load("images/Inventory_Back.png")
inventoryBackSelected = image.load("images/Inventory_Back14.png")
heart = image.load("images/Heart.png").convert(32, SRCALPHA)
items = [False, item1, item2, item1, item4, item5, item6, False, False, item9]
item4_sprite = image.load("player/item_4.png").convert(32, SRCALPHA)
item5_sprite = image.load("player/item_5.png").convert(32, SRCALPHA)
item4_sprites = [[], False, False, []]
for i in range(0, 280, 56):
    item4_sprites[0].append(item4_sprite.subsurface((0, i, 80, 56)))
for i in range(0, 280, 56):
    item4_sprites[3].append(transform.flip(item4_sprite.subsurface((0, i, 80, 56)), True, False))
item5_sprites = [[], False, False, []]
for i in range(0, 280, 56):
    item5_sprites[0].append(item5_sprite.subsurface((0, i, 80, 56)))
for i in range(0, 280, 56):
    item5_sprites[3].append(transform.flip(item5_sprite.subsurface((0, i, 80, 56)), True, False))
itemSprites = [False, False, False, False, item4_sprites, item5_sprites, False, False, False, False]

toolSpeeds = [5, 5, 5, 5, 15, 5, 5, 5, 5, 5]
effTools = [0.5, 0.5, 4, 0.5, 0.5, 0.5, 4]
dropsList = []
############################MUSIC LOADING###############################
"""Endless ambient music from the Terraria Wiki. We used the pygame wiki
to learn how to use pygame.mixer"""
file1="Audio/02-Day.mp3"
file2="Audio/03-Night.mp3"

player_hit_sound = mixer.Sound("sounds/player_hit_0.wav")

music = []
music.append(file1)
music.append(file2)

shuffle(music)


END_MUSIC_EVENT=pygame.USEREVENT+0
pygame.mixer.music.set_endevent(END_MUSIC_EVENT)
#########################################################################
"""Variable names explain themselves. Each entity in the game has it's on class.
We simply declare a variable inside the event loop to call the classes and
their functions. Each mob has a class, along with the player, blocks inventory,
and items"""
class Wizard:
    def __init__(self,x,y,w,h):
        self.rect = Rect(x,y,w,h)
        self.blitPos = [x - 8, y - 7]
        self.vx = 0
        self.vy = 0
        self.frame = 0
        self.attack = 0
        self.fire = False #attack variables
        self.health = 100
        self.fireRect = Rect(x,y,w,h) #for collisions
        self.stuck = False
        self.move = 0
        self.newMove = -1 #not moving
        self.firePos = 0 #fireball x value
        self.delete = False
#/////////////////////////////////////////////////////////////////////////////
    def moveWizard(self):
        x = randint(1,40) #random intengers slow things down, allowing for timing
        y = randint(1,2) #dictates left or right
        if x==40 and not self.fire: 
            if y==1: #Right movement
                self.stuck = False
                self.vx = 5 
                self.newMove = 1
            if y==2: #Left movement
                self.stuck = False 
                self.vx = -5
                self.newMove = 0

        if self.move == self.newMove and not self.stuck:  # 0 is a standing pose, so we want to skip over it when we are moving
            self.frame = self.frame + 0.2  # adding 0.2 allows us to slow down the animation
            if self.frame >= len(wizardPics[self.move]):
                self.frame = 0

        elif self.newMove != -1 and not self.stuck:  # a move was selected
            self.move = self.newMove  # make that our current move
            self.frame = 0
        if self.stuck: #moves back to standing frame
            self.frame = 0
#/////////////////////////////////////////////////////////////////////////////            
    def collide(self):
        self.rect.x += self.vx #scans through blocks and checks for collisions
        for x in range(self.rect.centerx // 16 - 1, self.rect.centerx // 16 + 2):
            for y in range(self.rect.centery // 16 - 2, self.rect.centery // 16 + 3):
                if blocks[y][x].id != 0 and self.rect.colliderect(blocks[y][x].rect):
                    if self.vx > 0:
                        self.rect.right = blocks[y][x].rect.left
                        vx = 0 #stop movment if collides with blocks
                        self.stuck = True
                    elif self.vx < 0:
                        self.rect.left = blocks[y][x].rect.right
                        vx = 0
                        self.stuck = True
                        
        self.rect.y += self.vy #scans through blocks and checks for collisions
        for x in range(self.rect.centerx // 16 - 1, self.rect.centerx // 16 + 2):
            for y in range(self.rect.centery // 16 - 2, self.rect.centery // 16 + 3):
                if blocks[y][x].id != 0 and self.rect.colliderect(blocks[y][x].rect):
                    if self.vy > 0: #stop movmeent if collides with blocks
                        self.rect.bottom = blocks[y][x].rect.top
                    elif self.vy < 0:
                        self.rect.top = blocks[y][x].rect.bottom
                self.vy = 5
                    
        self.blitPos = [self.rect.x - 8, self.rect.y - 7] #chaging blit position
        #we did -8, -7 since sprites are weird

    def attackFunc(self):
        if self.fireRect.colliderect(player.rect) and player.health >= 3 and self.fire and not player.hit:
            player.hit = 500 #counter that delays damage
            player.health -= 3 #subtracting damage
            player_hit_sound.play(0)
        elif self.fireRect.colliderect(player.rect) and self.fire and not player.hit:
            player.hit = 500
            player.health = 0
            player_hit_sound.play(0)

#/////////////////////////////////////////////////////////////////////////
    def clear(self): #draws tramsparent rect to clear space
        draw.rect(playerSurface, (0, 0, 0, 0), (self.blitPos[0] - 300, self.blitPos[1] - 50, 550, 150))
#/////////////////////////////////////////////////////////////////////////        
    def draw(self): #actual drawing function
        self.attack = randint(1,50) #draws fireball
        if player.hit:
            self.fire = False
        if self.fire:
            if self.move == 1:
                playerSurface.blit(wizardPics[2][0],(self.rect.x -4 + self.firePos, self.rect.y - 7))
                self.firePos += 5
                self.fireRect = Rect (self.rect.x - 4 + self.firePos, self.rect.y - 7, wizardPics[2][0].get_width(),wizardPics[2][0].get_height())
            elif self.move == 0: #making hitbox, dictation of movement
                playerSurface.blit(wizardPics[2][1],(self.rect.x - 60 + self.firePos, self.rect.y - 7))
                self.firePos -= 5 #moving x value
                self.fireRect = Rect (self.rect.x - 60 + self.firePos, self.rect.y - 7, wizardPics[2][1].get_width(),wizardPics[2][1].get_height())
            if abs(self.firePos) > 150: #if it moves out of range
                self.fire = False
        if self.attack == 50:
            if not self.fire:
                if self.move == 1: #choosing fire direction
                    playerSurface.blit(wizardPics[2][0],(self.rect.x -4, self.rect.y - 7))
                    self.fire = True
                if self.move == 0:
                    playerSurface.blit(wizardPics[2][1],(self.rect.x - 60, self.rect.y - 7))
                    self.fire = True
                self.firePos = 0
            elif self.firePos > 50:
                self.fire = False
        pic = wizardPics[self.move][int(self.frame)] #from mario example
        playerSurface.blit(pic,self.blitPos) #blitting
        self.healthRect = Rect(self.rect.x-20,self.rect.y-20,int(self.health/2),10)
        draw.rect(playerSurface,(255,0,0),self.healthRect) #wizard health bar
#############################################################################
class PurpleSlime: 
    def __init__(self,x,y,w,h):
        self.rect = Rect(x,y,w,h)
        self.blitPos = [x - 8, y - 7]
        self.vx = 0
        self.vy = 0
        self.jumping = False
        self.right = False #directional boolean
        self.left = False
        self.frame = 0
        self.attack = 0
        self.health = 100
        self.delete = False #if it dies, it gets deleted
#////////////////////////////////////////////////////////////////////////////
    def moveSlime(self):
        distance = abs(player.rect.x - slime.rect.x)
        x = randint(1,60)
        if x == 60: #chooses direction
            if distance <400:
                if self.rect.x <player.rect.x and not self.jumping:
                    self.vx = 10
                    self.vy = -10
                    self.jumping = True
                    self.right = True
                if self.rect.x >player.rect.x and not self.jumping:
                    self.vx = -10
                    self.vy= -10
                    self.jumping = True
                    self.left = True
#//////////////////////////////////////////////////////////////////////////
    def collide(self):
        self.rect.x += self.vx #adding x 
        for x in range(self.rect.centerx // 16 - 1, self.rect.centerx // 16 + 2):
            for y in range(self.rect.centery // 16 - 2, self.rect.centery // 16 + 3):
                if blocks[y][x].id != 0 and self.rect.colliderect(blocks[y][x].rect):
                    if self.vx > 0: #cancelling if collision
                        self.rect.right = blocks[y][x].rect.left
                    elif self.vx < 0:
                        self.rect.left = blocks[y][x].rect.right
        self.rect.y += self.vy #adding y
        for x in range(self.rect.centerx // 16 - 1, self.rect.centerx // 16 + 2):
            for y in range(self.rect.centery // 16 - 2, self.rect.centery // 16 + 3):
                if blocks[y][x].id != 0 and self.rect.colliderect(blocks[y][x].rect):
                    self.vy = 5
                    if self.vy > 0: #cancelling if collision
                        self.rect.bottom = blocks[y][x].rect.top
                        self.jumping = False
                    elif self.vy < 0:
                        self.rect.top = blocks[y][x].rect.bottom

        if self.right and self.vx > 0: #makes things smoother
            self.vx -= 0.7
        else:
            self.vx = 0
            self.jumping = False
            self.right = False

        if self.left and self.vx <0: #makes motion smoother
            self.vx += 0.7
        else:
            self.vx = 0
            self.jumping = False
            self.left = False
        if self.vy < 30: #terminal velocity
            self.vy += 0.7
        if self.vy == 0:
            self.jumping = False
        

        self.blitPos = [self.rect.x - 8, self.rect.y - 7]
        self.attack = randint(1,100) 

    def attackFunc(self):
        if self.rect.colliderect(player.rect) and player.health >= 2 and self.attack==25 and not player.hit:
            player.health -= 2
            player.hit = 500
            player_hit_sound.play(0)
        elif slime.rect.colliderect(player.rect) and not player.hit:
            player.health = 0
            player.hit = 500
            player_hit_sound.play(0)
#////////////////////////////////////////////////////////////////////////////
    def clear(self): #drawing rectangle to clear surroundings
        draw.rect(playerSurface, (0, 0, 0, 0), (self.blitPos[0] - 50, self.blitPos[1] - 50, 150, 150))
#///////////////////////////////////////////////////////////////////////////
    def draw(self): #drawing
        x=randint(1,5)
        if x==5:
            if self.frame<3:
                self.frame+=1
            else:
                self.frame=0
        pic = purpleSlimePics[int(self.frame)]
        playerSurface.blit(pic,self.blitPos)
        self.healthRect = Rect(self.rect.x-20,self.rect.y-20,int(self.health/2),10)
        draw.rect(playerSurface,(255,0,0),self.healthRect) #health bar
############################################################################          
class Slime: #same as regular slime
    def __init__(self, x, y, w, h):
        self.rect = Rect(x, y, w, h)
        self.blitPos = [ x - 8, y - 7]
        self.vx = 0 #velocity
        self.vy = 0
        self.jumping = False
        self.right = False #directional boolean
        self.left = False
        self.frame = 0
        self.attack = 0
        self.health = 100
        self.delete= False #deletes after dead
    def moveSlime(self):
        distance = abs(player.rect.x - slime.rect.x) #distance between slime and player
        x = randint(1,60) #distance variable
        if x==60: 
            if distance < 500:  #stops after above 500
                if self.rect.x  <  player.rect.x and not self.jumping:
                    self.vx = 7
                    self.vy = -7
                    self.jumping = True
                    self.right = True
                if self.rect.x > player.rect.x and not self.jumping:
                    self.vx = -7
                    self.vy= -7
                    self.jumping = True
                    self.left = True
    def collide(self): #checks collisions
        self.rect.x += self.vx #adding x
        for x in range(self.rect.centerx // 16 - 1, self.rect.centerx // 16 + 2):
            for y in range(self.rect.centery // 16 - 2, self.rect.centery // 16 + 3):
                if blocks[y][x].id != 0 and self.rect.colliderect(blocks[y][x].rect):
                    if self.vx > 0: #cancelling if collision
                        self.rect.right = blocks[y][x].rect.left
                    elif self.vx < 0:
                        self.rect.left = blocks[y][x].rect.right
        self.rect.y += self.vy #adding y  
        for x in range(self.rect.centerx // 16 - 1, self.rect.centerx // 16 + 2):
            for y in range(self.rect.centery // 16 - 2, self.rect.centery // 16 + 3):
                if blocks[y][x].id != 0 and self.rect.colliderect(blocks[y][x].rect):
                    self.vy = 5
                    if self.vy > 0:
                        self.rect.bottom = blocks[y][x].rect.top
                        self.jumping = False
                    elif self.vy < 0:
                        self.rect.top = blocks[y][x].rect.bottom

        if self.right and self.vx > 0: #smoothens out bounce
            self.vx -= 0.7
        else:
            self.vx = 0
            self.jumping = False
            self.right = False

        if self.left and self.vx <0: #smoothes out bounce
            self.vx += 0.7
        else:
            self.vx = 0
            self.jumping = False
            self.left = False
        if self.vy < 30: #terminal velocity
            self.vy += 0.7
        if self.vy == 0:
            self.jumping = False
        

        self.blitPos = [self.rect.x - 8, self.rect.y - 7]
        self.attack = randint(1,120)
    def attackFunc(self): #attacks with 1 damage 
        if self.rect.colliderect(player.rect) and player.health >= 1 and self.attack==25 and not player.hit:
            player.health -= 1
            player.hit = 500
            player_hit_sound.play(0)
        elif self.rect.colliderect(player.rect) and self.attack==25 and not player.hit:
            player.health = 0
            player.hit = 500
            player_hit_sound.play(0)

    def clear(self): #clears area
        draw.rect(playerSurface, (0, 0, 0, 0), (self.blitPos[0] - 50, self.blitPos[1] - 50, 150, 150))
        
    def draw(self): #draws images
        x=randint(1,5)
        if x==5:
            if self.frame<3:
                self.frame+=1
            else:
                self.frame=0
        pic = slimePics[int(self.frame)]
        playerSurface.blit(pic,self.blitPos)
        self.healthRect = Rect(self.rect.x-20,self.rect.y-20,int(self.health/2),10)
        draw.rect(playerSurface,(255,0,0),self.healthRect) #health bar
#########################################################################
class Player:
    def __init__(self, x, y, w, h):
        self.rect = Rect(x, y, w, h)
        self.blitPos = [x - 8, y - 7]
        self.vx = 0
        self.vy = 0
        self.jumping = False 
        self.move = 1
        self.newMove = -1 #not moving
        self.frame = 0
        self.health = 100 #player health
        self.breaking = False
        self.hit = 0 #not hit

    def movePlayer(self):
        keys = key.get_pressed() #we use keys here b/c user input

        self.newMove = -1 #newmove always -1 until key pessed

        if self.breaking: #if breaking or hitting an object
            if self.move == 2 or self.move == 0:
                self.newMove = 0
            else:
                self.newMove = 3
        else: #if henning tries to spam keys
            if keys[K_d] and keys[K_a]:
                self.frame = 0

            else: 
                if keys[K_d] and self.rect.x < worldSize[0] * 16 - 625:
                    if not self.jumping: #right movement
                        self.newMove = 2
                    self.vx = 3
                elif keys[K_a] and self.rect.x > 633:
                    if not self.jumping: #left movement
                        self.newMove = 5
                    self.vx = -3
                else: #returns to standing position
                    self.frame = 0

            if keys[K_w] and not self.jumping:
                self.vy = -15 #jumps up
                self.jumping = True
                if self.move == 2 or self.move == 1: #jumping animation
                    self.newMove = 1
                else:
                    self.newMove = 4

            elif self.jumping: #doesnt return to walking sprite, stays jumping
                if keys[K_d]:
                    self.newMove = 1
                elif keys[K_a]:
                    self.newMove = 4

            if not self.jumping and self.move == 1:
                self.move = 2

        if self.move == self.newMove:  # 0 is a standing pose, so we want to skip over it when we are moving
            if self.move == 0 or self.move == 3:
                self.frame = self.frame + 0.15
            else:
                self.frame = self.frame + 0.6  # adding 0.2 allows us to slow down the animation
            if self.frame >= len(pics[self.move]):
                self.frame = 1
        elif self.newMove != -1:  # a move was selected
            self.move = self.newMove  # make that our current move
            self.frame = 1

    def collide(self):
        self.rect.y += self.vy #adding y first 
        for x in range(self.rect.centerx // 16 - 1, self.rect.centerx // 16 + 2):
            for y in range(self.rect.centery // 16 - 2, self.rect.centery // 16 + 3):
                if blocks[y][x].id != 0 and self.rect.colliderect(blocks[y][x].rect):
                    if self.vy > 0: #canceling if theres a collision
                        self.rect.bottom = blocks[y][x].rect.top
                        self.jumping = False
                    elif self.vy < 0:
                        self.rect.top = blocks[y][x].rect.bottom
                    self.vy = 5

        self.rect.x += self.vx #adding x 
        for x in range(self.rect.centerx // 16 - 1, self.rect.centerx // 16 + 2):
            for y in range(self.rect.centery // 16 - 2, self.rect.centery // 16 + 3):
                if blocks[y][x].id != 0 and self.rect.colliderect(blocks[y][x].rect):
                    if self.vx > 0: #cancelling if theres a collision
                        self.rect.right = blocks[y][x].rect.left
                    elif self.vx < 0:
                        self.rect.left = blocks[y][x].rect.right

                    ##        if self.jumping and self.vy < 30:
                    ##            self.vy += 2
                    ##        elif not self.jumping:
                    ##            self.vy = 5
        if self.vy < 30: #adding until terminal velocity
            self.vy += 2

        self.vx = 0 #stays zero once its addded

        self.blitPos = [self.rect.x - 8, self.rect.y - 7]
        for slime in slimeList: #slime damage thing too lazy to move
            if slime.rect.colliderect(self.rect) and self.health>=10 and slime.attack==25:
                self.health -= 10
            elif slime.rect.colliderect(self.rect) and slime.attack==25:
                self.heatlh = 0

    def attack(self): #player attacks
        """In this function we utilized a lot of colliderect. If the player was holding a weapon, swinging
        and colliding with an enemy the appropriate damage was dealth. Mobs drop gel when killed"""
        for slime in slimeList: #if player breaks on slime
            if slime.rect.colliderect(self.rect):
                if inventoryList[inventory.selected].id == 5:
                    if slime.health >= 4:
                        slime.health -= 4
                        self.breaking = True
                    elif slime.rect.colliderect(self.rect): #if collision
                        slime.heatlh = 0
                        slime.delete = True #deleting and dropping gell
                        dropsList.append(Drop(slime.rect.x//16, slime.rect.y//16, 9))
                        self.breaking = False
                else:
                    if slime.health >= 1:
                        slime.health -= 1 #taking one away
                        self.breaking = True
                    elif slime.rect.colliderect(self.rect):
                        slime.heatlh = 0
                        slime.delete = True #dropping gel and deleting slime
                        dropsList.append(Drop(slime.rect.x//16, slime.rect.y//16, 9))
                        self.breaking = False

        for purpSlime in purpleSlimeList: #if we attack or hit purple slime
            if purpSlime.rect.colliderect(self.rect):
                if inventoryList[inventory.selected].id == 5:
                    if purpSlime.health >= 3: #hitting with sword or whatever
                        purpSlime.health -= 3
                        self.breaking = True
                    elif purpSlime.rect.colliderect(self.rect):
                        purpSlime.heatlh = 0
                        purpSlime.delete = True #deleted to oblivionnn
                        dropsList.append(Drop(purpSlime.rect.x//16, purpSlime.rect.y//16, 9))
                        self.breaking = False
                else:
                    if purpSlime.health >= 1:
                        purpSlime.health -= 1
                        self.breaking = True
                    elif purpSlime.rect.colliderect(self.rect): #collisions
                        purpSlime.heatlh = 0 #dropping gel and deleted
                        purpSlime.delete = True
                        dropsList.append(Drop(purpSlime.rect.x//16, purpSlime.rect.y//16, 9))
                        self.breaking = False
        for wizard in wizardList:
            if wizard.rect.colliderect(self.rect):
                if inventoryList[inventory.selected].id == 5:
                    if wizard.health >= 3: #same thing for wizard
                        wizard.health -= 3
                        self.breaking = True
                    elif wizard.rect.colliderect(self.rect):
                        wizard.heatlh = 0 #checking for collision and killing it
                        wizard.delete = True
                        dropsList.append(Drop(wizard.rect.x // 16, wizard.rect.y // 16, 9))
                        self.breaking = False
                else:
                    if wizard.health >= 1:
                        wizard.health -= 1 #deleting to oblivion after
                        self.breaking = True
                    elif wizard.rect.colliderect(self.rect):
                        wizard.heatlh = 0
                        wizard.delete = True
                        dropsList.append(Drop(wizard.rect.x // 16, wizard.rect.y // 16, 9))
                        self.breaking = False


    def clear(self): #draws transparent rect to clear room
        draw.rect(playerSurface, (0, 0, 0, 0), (self.blitPos[0] - 50, self.blitPos[1] - 50, 150, 150))

    def draw(self): #blits image
        pic = pics[self.move][int(self.frame)]
        playerSurface.blit(pic, self.blitPos)
        if (self.move == 0 or self.move == 3) and inventoryList[inventory.selected].type == TOOL: #draws current tool being held by player
            playerSurface.blit(itemSprites[inventoryList[inventory.selected].id][self.move][int(self.frame)], (self.blitPos[0] - 20, self.blitPos[1]))
        uiSurface.fill((0, 0, 0, 0)) #health bar stuff, andy22 is the font. 
        uiSurface.blit(andy22.render(str(self.health) + " / " + "100", 1, (255, 255, 255)), (1120, 10))
        for i in range(0, self.health, 20): #drawing hearts
            uiSurface.blit(heart, (1095 + 27 * i/20, 40))


#############################################################################
class Block:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        self.rect = Rect(x * 16, y * 16, 16, 16)
        self.condition = blockConditions[self.id]
        top = True
        down = True
        left = True
        right = True
        if y != 0 and blockList[y - 1][x] == 0:
            top = False
        if y != worldSize[1] - 1 and blockList[y + 1][x] == 0:
            down = False
        if x != 0 and blockList[y][x - 1] == 0:
            left = False
        if x != worldSize[0] - 1 and blockList[y][x + 1] == 0:
            right = False

        if top and down and left and right:
            self.surround = 0

        elif not top and not down and not left and not right:
            self.surround = 11

        else:
            if top and down and right:
                self.surround = 2

            elif down and left and right:
                self.surround = 1

            elif top and down and left:
                self.surround = 3

            elif top and left and right:
                self.surround = 4

            else:
                if top:
                    if left:
                        self.surround = 5
                    elif right:
                        self.surround = 6
                    elif down:
                        self.surround = 7
                    else:
                        self.surround = 12
                elif down:
                    if left:
                        self.surround = 8
                    elif right:
                        self.surround = 9
                    else:
                        self.surround = 13
                elif left:
                    if right:
                        self.surround = 10
                    else:
                        self.surround = 14
                else:
                    self.surround = 15

    def draw(self):
        draw.rect(blocksSurface, (0, 0, 0, 0), self.rect)
        if self.id != 0:
            blocksSurface.blit(blockImg[self.id][self.surround], (self.x * 16, self.y * 16))
            if self.condition < blockConditions[self.id] * 4 / 5:
                blocksSurface.blit(tile_cracks[self.condition // int(blockConditions[self.id] / 5)],
                                   (self.x * 16, self.y * 16))

    def update(self):
        top = True
        down = True
        left = True
        right = True
        if y != 0 and blocks[y - 1][x].id == 0:
            top = False
        if y != worldSize[1] and blocks[y + 1][x].id == 0:
            down = False
        if x != 0 and blocks[y][x - 1].id == 0:
            left = False
        if x != worldSize[0] and blocks[y][x + 1].id == 0:
            right = False

        if top and down and left and right:
            self.surround = 0

        elif not top and not down and not left and not right:
            self.surround = 11

        else:
            if top and down and right:
                self.surround = 2

            elif down and left and right:
                self.surround = 1

            elif top and down and left:
                self.surround = 3

            elif top and left and right:
                self.surround = 4

            else:
                if top:
                    if left:
                        self.surround = 5
                    elif right:
                        self.surround = 6
                    elif down:
                        self.surround = 7
                    else:
                        self.surround = 12
                elif down:
                    if left:
                        self.surround = 8
                    elif right:
                        self.surround = 9
                    else:
                        self.surround = 13
                elif left:
                    if right:
                        self.surround = 10
                    else:
                        self.surround = 14
                else:
                    self.surround = 15

    def breakBlock(self):
        if self.id != 0:
            player.breaking = True
            if inventoryList[inventory.selected].id == effTools[self.id]:
                if self.condition - inventoryList[inventory.selected].speed <= 0:
                    dropsList.append(Drop(self.x, self.y, self.id))
                    self.id = 0
                    self.condition = 0
                else:
                    self.condition -= inventoryList[inventory.selected].speed
            else:
                if self.condition - 5 <= 0:
                    if self.id == 3:
                        dropsList.append(Drop(self.x, self.y, 1))
                    else:
                        dropsList.append(Drop(self.x, self.y, self.id))
                    self.id = 0
                    self.condition = 0
                else:
                    self.condition -= 5

class treesBlock:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        self.rect = Rect(x * 16, y * 16, 16, 16)
        self.condition = blockConditions[self.id]
        top = True
        down = True
        left = True
        right = True
        if y != 0 and treesList[y - 1][x] == 0:
            top = False
        if y != worldSize[1] - 1 and treesList[y + 1][x] == 0:
            down = False
        if x != 0 and treesList[y][x - 1] == 0:
            left = False
        if x != worldSize[0] - 1 and treesList[y][x + 1] == 0:
            right = False

        if id == 7:
            if top and left and right:
                self.surround = 3
            elif top and left and down:
                self.surround = 0
            elif top and right and down:
                self.surround = 0
            elif right:
                self.surround = 2
            elif left:
                self.surround = 1
            elif down and not top and not left and not right:
                self.surround = 0
                treesSurface.blit(tree_top, (self.x * 16 - 30, self.y * 16 - 80))
            else:
                self.surround = 0

        elif id == 8:
            if left:
                self.surround = 0
            else:
                self.id = 0

    def draw(self):
        if self.id != 0:
            draw.rect(treesSurface, (0, 0, 0, 0), self.rect)
            treesSurface.blit(blockImg[self.id][self.surround], (self.x * 16, self.y * 16))
            if self.condition < blockConditions[self.id] * 4 / 5 and self.id != 8:
                treesSurface.blit(tile_cracks[self.condition // int(blockConditions[self.id] / 5)],(self.x * 16, self.y * 16))

    def breakBlock(self):
        player.breaking = True
        """if inventoryList[inventory.selected].id == effTools[self.id]:
            if self.condition - inventoryList[inventory.selected].speed <= 0:
                dropsList.append(Drop(self.x, self.y, self.id))
                self.id = 0
                self.condition = 0
            else:
                self.condition -= inventoryList[inventory.selected].speed
        else:
            if self.condition - 5 <= 0:
                if self.id == 3:
                    dropsList.append(Drop(self.x, self.y, 1))
                else:
                    dropsList.append(Drop(self.x, self.y, self.id))
                self.id = 0
                self.condition = 0
            else:
                self.condition -= 5"""
        if self.condition - 20 <= 0:
            self.id = 0
            self.condition = 0
        else:
            self.condition -= 20
##############################################################################
class inventory:
    selected = 0
    def __init__(self, pos, id, quantity, type):
        self.id = id
        self.quantity = quantity
        self.type = type
        self.pos = pos
        self.speed = toolSpeeds[self.id]

    def draw(self):
        if self.pos == inventory.selected:
            uiSurface.blit(inventoryBackSelected, (20 + 56 * self.pos, 20))
        else:
            uiSurface.blit(inventoryBack, (20 + 56 * self.pos, 20))
        if items[self.id] != EMPTY:
            uiSurface.blit(items[self.id], (20 + 56 * self.pos + int((52 - items[self.id].get_width())/2), 20 + int((52 - items[self.id].get_height())/2)))
        if self.pos == 9:
            uiSurface.blit(andy18.render("0", 1, (255, 255, 255)), (28 + 56 * self.pos, 22))
        else:
            uiSurface.blit(andy18.render(str(self.pos + 1), 1, (255, 255, 255)), (28 + 56 * self.pos, 22))
        if self.quantity > 1:
            uiSurface.blit(andy16.render(str(self.quantity), 1, (255, 255, 255)), (32 + 56 * self.pos, 47))

class Drop:
    def __init__(self, x, y, id):
        self.rect = Rect(x * 16, y * 16, 16, 16)
        self.id = id
        self.delete = False
        self.dist = False

    def collidePlayer1(self):
        self.dist = False

        for item in inventoryList:
            if item.id == self.id and item.quantity < 64:
                if 5 < math.hypot(player.rect.centerx - self.rect.centerx, player.rect.centery - self.rect.centery) < 35:
                    self.rect.x += (player.rect.centerx - self.rect.centerx) / 2
                    self.rect.y += (player.rect.centery - self.rect.centery) / 2
                    self.dist = True
                    break
                elif 5 > math.hypot(player.rect.centerx - self.rect.centerx, player.rect.centery - self.rect.centery):
                    item.quantity += 1
                    self.delete = True
                    self.dist = True
                    break

    def collidePlayer2(self):
        for item in inventoryList:
            if item.id == 0:
                if 5 < math.hypot(player.rect.centerx - self.rect.centerx, player.rect.centery - self.rect.centery) < 35:
                    self.rect.x += (player.rect.centerx - self.rect.centerx) / 2
                    self.rect.y += (player.rect.centery - self.rect.centery) / 2
                    self.dist = True
                    break
                elif 5 > math.hypot(player.rect.centerx - self.rect.centerx, player.rect.centery - self.rect.centery):
                    item.id = self.id
                    item.type = BLOCK
                    item.quantity = 1
                    self.delete = True
                    self.dist = True
                    break

    def collide(self):
        self.dist = False
        self.rect.y += 15
        for x in range(self.rect.centerx // 16 - 1, self.rect.centerx // 16 + 2):
            for y in range(self.rect.centery // 16 - 2, self.rect.centery // 16 + 3):
                if blocks[y][x].id != 0 and self.rect.colliderect(blocks[y][x].rect):
                    self.rect.bottom = blocks[y][x].rect.top
                    self.falling = False

    def clear(self):
        draw.rect(playerSurface, (0, 0, 0, 0), (self.rect.x, self.rect.y - 20, 20, 20))

    def draw(self):
        playerSurface.blit(items[self.id], (self.rect.x, self.rect.y))
###########################################################################

def drawBlocks(x1, x2, y1, y2):
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            blocks[y][x].draw()
            trees[y][x].draw()

def drawBackground():
    screen.fill((15, 80, 220))
    screen.blit(background1, (int(player.rect.x - 629) / -15, -50))
    screen.blit(background1, (1280 - int(player.rect.x - 629) / 15, -50))
    screen.blit(background2, (int(player.rect.x - 629) / -10, 150))
    screen.blit(background2, (1280 - int(player.rect.x - 629) / 10, 150))
    screen.blit(background3, (int(player.rect.x - 629)/-5, 225))
    screen.blit(background3, (1280 - int(player.rect.x - 629) / 5, 225))

blocks = []
for y in range(len(blockList)):
    row = []
    for x in range(len(blockList[0])):
        row.append(Block(blockList[y][x], x, y))
    blocks.append(row)

trees = []
for y in range(len(treesList)):
    row = []
    for x in range(len(treesList[0])):
        row.append(treesBlock(treesList[y][x], x, y))
    trees.append(row)

inventoryList = []
for i in range(10):
    inventoryList.append(inventory(i, inventoryPickleList[i][0], 1, inventoryPickleList[i][1]))

drawBlocks(0, len(blocks[0]) - 1, 0, len(blocks) - 1)
###########################################################################
player = Player(1000, 339, 24, 45)
wizardList = []
for i in range(3):
    wizard = Wizard(randint(700,1800),319,20,37)
    wizardList.append(wizard)


slimeList=[]
for i in range(5):
    slime= Slime(randint(900,1800),339,14,14)
    slimeList.append(slime)

purpleSlimeList=[]
for i in range(3):
    purpleSlime = PurpleSlime(randint(900,1800),339,28,28)
    purpleSlimeList.append(purpleSlime)


EMPTY = 0
BLOCK = 1
TOOL = 2
deleteList = []
##########################################################################

pygame.mixer.music.load(music[0])
pygame.mixer.music.play()
paused = False
running = True
positive = True
dead =False
time = 0
while running:
    leftClick = False
    rightClick = False
    mx, my = mouse.get_pos()
    mb = mouse.get_pressed()

    for evt in event.get():
        if evt.type == QUIT:
            running = False
        if evt.type == MOUSEBUTTONDOWN:
            if evt.button == 1:
                leftClick = True
            if evt.button == 3:
                rightClick = True
            if evt.button == 5:
                if inventory.selected == 9:
                    inventory.selected = 0
                else:
                    inventory.selected += 1
            if evt.button == 4:
                if inventory.selected == 0:
                    inventory.selected = 9
                else:
                    inventory.selected -= 1
        if evt.type == KEYDOWN:
            if evt.key == K_1:
                inventory.selected = 0
            elif evt.key == K_2:
                inventory.selected = 1
            elif evt.key == K_3:
                inventory.selected = 2
            elif evt.key == K_4:
                inventory.selected = 3
            elif evt.key == K_5:
                inventory.selected = 4
            elif evt.key == K_6:
                inventory.selected = 5
            elif evt.key == K_7:
                inventory.selected = 6
            elif evt.key == K_8:
                inventory.selected = 7
            elif evt.key == K_9:
                inventory.selected = 8
            elif evt.key == K_0:
                inventory.selected = 9
            elif evt.key == K_ESCAPE:
                if paused:
                    paused =False
                elif not paused:
                    paused = True
#///////////////////////////////////////////////////////////////////////////
    if not paused and not dead:
        if time <= 5184000 and positive:
            time+=5000
        else:
            positive = False
        if time >= 0 and not positive:
            time-=5000
        else:
            positive = True

        alphaCount=time//20330

        if player.hit > 0:
            player.hit -= 0.1
    #///////////////////////////////////////////////////////////////////////////
        if mb[0] == 1:
            if abs((player.rect.y - 339 + my) // 16 - player.rect.y // 16) < 5 and abs((player.rect.x - 629 + mx) // 16 - player.rect.x // 16) < 5:
                trees[(player.rect.y - 339 + my) // 16][(player.rect.x - 629 + mx) // 16].breakBlock()
                blocks[(player.rect.y - 339 + my) // 16][(player.rect.x - 629 + mx) // 16].breakBlock()
                player.attack()
                for x in range((player.rect.x - 629 + mx) // 16 - 1, (player.rect.x - 629 + mx) // 16 + 2):
                    for y in range((player.rect.y - 339 + my) // 16 - 1, (player.rect.y - 339 + my) // 16 + 2):
                        blocks[y][x].update()
                for x in range((player.rect.x - 629 + mx) // 16 - 1, (player.rect.x - 629 + mx) // 16 + 2):
                    for y in range((player.rect.y - 339 + my) // 16 - 1, (player.rect.y - 339 + my) // 16 + 2):
                        blocks[y][x].draw()
                        trees[y][x].draw()

        elif player.breaking == True:
            player.breaking = False
            if player.move == 0:
                player.move = 1
            elif player.move == 3:
                player.move = 4

        if mb[2] == 1:
            if inventoryList[inventory.selected].type == BLOCK and blocks[(player.rect.y - 339 + my) // 16][(player.rect.x - 629 + mx) // 16].id == 0:
                blocks[(player.rect.y - 339 + my) // 16][(player.rect.x - 629 + mx) // 16].id = inventoryList[inventory.selected].id
                blocks[(player.rect.y - 339 + my) // 16][(player.rect.x - 629 + mx) // 16].condition = blockConditions[inventoryList[inventory.selected].id]
                for x in range((player.rect.x - 629 + mx) // 16 - 1, (player.rect.x - 629 + mx) // 16 + 2):
                    for y in range((player.rect.y - 339 + my) // 16 - 1, (player.rect.y - 339 + my) // 16 + 2):
                        blocks[y][x].update()
                for x in range((player.rect.x - 629 + mx) // 16 - 1, (player.rect.x - 629 + mx) // 16 + 2):
                    for y in range((player.rect.y - 339 + my) // 16 - 1, (player.rect.y - 339 + my) // 16 + 2):
                        blocks[y][x].draw()
                        trees[y][x].draw()
                if inventoryList[inventory.selected].quantity > 1:
                    inventoryList[inventory.selected].quantity -= 1
                else:
                    inventoryList[inventory.selected].id = 0
                    inventoryList[inventory.selected].type = EMPTY
                    inventoryList[inventory.selected].quantity = 0
        for wizard in wizardList: #calling the class functions
            wizard.attackFunc()

        for purpSlime in purpleSlimeList: #calling the class functions
            purpSlime.attackFunc()

        for slime in slimeList: #calling the class functions
            slime.attackFunc()

        if len(dropsList) != 0:
            for drop in dropsList:
                drop.collidePlayer1() 
            dropsList = [drop for drop in dropsList if not drop.delete]
        if len(dropsList) != 0:
            for drop in dropsList: #checking collision
                if not drop.dist:
                    drop.collidePlayer2()
            dropsList = [drop for drop in dropsList if not drop.delete] #if its gone, delete from list
        if len(dropsList) != 0:
            for drop in dropsList:
                if not drop.dist: #calling the class functions
                    drop.collide()
                drop.clear()

        for slime in slimeList: #calling the class functions
            slime.moveSlime()
            slime.collide()
            slime.clear()

        slimeList = [slime for slime in slimeList if not slime.delete]

        for purpSlime in purpleSlimeList: #calling the class functions
            purpSlime.moveSlime()
            purpSlime.collide()
            purpSlime.clear()

        purpleSlimeList = [purpSlime for purpSlime in purpleSlimeList if not purpSlime.delete]
        #deleting dead ones
        for wizard in wizardList: #calling the class functions
            wizard.moveWizard()
            wizard.collide()
            wizard.clear()

        wizardList = [wizard for wizard in wizardList if not wizard.delete]
        #deleting dead ones
        player.movePlayer() #calling the class functions
        player.collide()
        player.clear()

        drawBackground()

        if len(dropsList) != 0:
            for drop in dropsList:
                drop.draw()

        for slime in slimeList: #calling the class functions
            slime.draw()

        for purpSlime in purpleSlimeList:#calling the class functions
            purpSlime.draw()

        for wizard in wizardList:#calling the class functions
            wizard.draw()

        player.draw()
        for item in inventoryList:#calling the class functions
            item.draw()


        if player.rect.y >= 339:
            screen.blit(treesSurface.subsurface(player.rect.x - 629, player.rect.y - 339, 1280, 720), (0, 0))
            screen.blit(blocksSurface.subsurface(player.rect.x - 629, player.rect.y - 339, 1280, 720), (0, 0))
            screen.blit(playerSurface.subsurface(player.rect.x - 629, player.rect.y - 339, 1280, 720), (0, 0))
            # screen.blit(playerSurface.subsurface(player.blitPos[0], player.blitPos[1], 650, 320), (621, 339))
        else:
            screen.blit(treesSurface.subsurface(player.rect.x - 629, 0, 1280, 720), (0, abs(player.rect.y - 339)))
            screen.blit(blocksSurface.subsurface(player.rect.x - 629, 0, 1280, 720), (0, abs(player.rect.y - 339)))
            screen.blit(playerSurface.subsurface(player.rect.x - 629, 0, 1280, 720), (0, abs(player.rect.y - 339)))
            # screen.blit(playerSurface.subsurface(player.rect.x, 0, 650, 320), (612, abs(player.rect.y - 283)))

        screen.blit(uiSurface, (0, 0))

        display.flip()
        clock.tick(60)
        display.set_caption("FSE FPS = {0:.0f}".format(clock.get_fps()))

        if player.health == 0:
            dead = True

    if dead: #pauses game, resets health
        screenRect = Rect(0,0,1280,720)  #UI stuff
        draw.rect(screen,(0,0,0,250),screenRect)
        restart = andy44.render("Restart", True, (200,200,200))
        restart2 = andy58.render("Restart", True, (255,255,0))
        close = andy44.render("Exit",True,(200,200,200))
        close2 = andy58.render("Exit", True,(255,255,0))
        deadText = andy44.render("You have been slain",True,(255,0,0))
        screen.blit(deadText, (480,300))
        closeRect = Rect(600,600,90,50)
        restartRect = Rect(570,500,160,50)
        
        if closeRect.collidepoint(mx,my): #yellow highlight
            screen.blit(close2,(600,590))
            if leftClick:
                quit()
        else:
            screen.blit(close,(610,600))

        if restartRect.collidepoint(mx,my):
            screen.blit(restart2,(570,490))
            if leftClick:
                dead = False
                player = Player(629, 339, 24, 45)
                player.health = 100
        else:
            screen.blit(restart,(590,500))

        display.flip() #update screen
        
    if paused: #press ESC to pause
        screenRect = Rect(0,0,1280,720) #UI stuff
        draw.rect(screen,(0,0,0,250),screenRect)
        close = andy44.render("Exit",True,(200,200,200))
        close2 = andy58.render("Exit", True,(255,255,0))
        infoText = andy44.render("Press Esc. to Resume",True,(200,200,200))
        screen.blit(infoText,(480,300))
        closeRect = Rect(630,600,60,50)
        if closeRect.collidepoint(mx,my): #yellow highlights
            screen.blit(close2,(620,590))
            if leftClick: #closes game
                quit()
        else:
            screen.blit(close,(630,600))

        display.flip()
with open('blockspickle.pickle', 'wb') as f:
    pickle.dump(blockList, f) #updating pickle file

with open("inventory.pickle", "wb") as f:
    pickle.dump(inventoryPickleList, f) #updating pickle file

with open("trees.pickle", "wb") as f:
    pickle.dump(treesList, f)
out=open("flag.txt","w")
out.write("0")
out.close()
quit()
