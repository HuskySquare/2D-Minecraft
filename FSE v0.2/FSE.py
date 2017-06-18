from random import *
import numpy as np
import pickle
from time import time as tm
from pygame import *
import math
import pygame

pygame.init()
pygame.mixer.init()
pygame.mixer.pre_init(22050,-16,2,2048)
init()
######################################################################
with open("blockspickle.pickle", "rb") as f:
    blockList = pickle.load(f)

with open("inventory.pickle", "rb") as f:
    inventoryPickleList = pickle.load(f)

screen = display.set_mode((1280, 720))

andy18 = font.Font("fonts/HW ANDY.ttf", 18)
andy16 = font.Font("fonts/HW ANDY.ttf", 16)

clock = time.Clock()

worldSize = (780, 85)

blocksSurface = Surface((worldSize[0] * 16, worldSize[1] * 16), SRCALPHA)
blocksSurface.fill((0, 0, 0, 0))
playerSurface = Surface((worldSize[0] * 16, worldSize[1] * 16), SRCALPHA)
playerSurface.fill((0, 0, 0, 0))
uiSurface = Surface((1280, 720), SRCALPHA)
mainSurface = Surface((1280, 720), SRCALPHA)
###########################################################################
background = image.load("background.png").convert()
background = transform.scale(background, (1280, 720))

pics = []
sprite = image.load("player\Sprite0.png")

for i in range(6, 1126, 56):
    try:
        pics.append(sprite.subsurface((0, i, 40, 56)))
    except:
        pass

for i in range(6, 1126, 56):
    try:
        pics.append(transform.flip(sprite.subsurface((0, i, 40, 56)), True, False))
    except:
        pass

pics = [pics[0:5], [pics[5], pics[5]], pics[6:19], pics[19:24], [pics[24], pics[24]], pics[25:]]

slimePics=[]
for i in range(4):
    name="slime/slime_"+str(i)+".png"
    slimePics.append(image.load(name))

purpleSlimePics = []
for i in range(4):
    name="slime/slime2_"+str(i)+".png"
    purpleSlimePics.append(image.load(name))

wizardPics = [[],[],[]] #wizard sprite
for i in range(2):
    name = "wizard/skeleton_"+str(i)+".png"
    wizardPics[0].append(image.load(name))

for i in range(2):
    name = "wizard/skeleton_B_"+str(i)+".png"
    wizardPics[1].append(image.load(name))

wizardPics[2].append(image.load("wizard/fire.png"))
wizardPics[2].append(image.load("wizard/fire2.png"))
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
#//////////////////////////////////////////////////////////////////////
block3 = [block3_0, block3_1, block3_2, block3_3, block3_4, block3_5, block3_6, block3_7, block3_8, block3_9, block3_10,
          block3_11, block3_12, block3_13, block3_14, block3_15]
blockImg = [False, block1, block2, block3]
blockConditions = [False, 150, 500, 150]
#/////////////////////////////////////////////////////////////////////
item1 = image.load("items/item_1.png").convert(32, SRCALPHA)
item2 = image.load("items/item_2.png").convert(32, SRCALPHA)
item4 = image.load("items/item_4.png").convert(32, SRCALPHA)
inventoryBack = image.load("images/Inventory_Back.png")
inventoryBackSelected = image.load("images/Inventory_Back14.png")
items = [False, item1, item2, item1, item4]
toolSpeeds = [5, 5, 5, 5, 15]
effTools = [0.5, 0.5, 4, 0.5]
dropsList = []
############################MUSIC LOADING###############################
file1="Audio/02-Day.mp3"
file2="Audio/03-Night.mp3"

music = []
music.append(file1)
music.append(file2)

shuffle(music)


END_MUSIC_EVENT=pygame.USEREVENT+0
pygame.mixer.music.set_endevent(END_MUSIC_EVENT)
#########################################################################
"""Variable names explain themselves. Each entity in the game has it's on class.
We simply declare a variable inside the event loop to call the classes and
their functions"""
class Wizard:
    def __init__(self,x,y,w,h):
        self.rect = Rect(x,y,w,h)
        self.blitPos = [x - 8, y - 7]
        self.vx = 0
        self.vy = 0
        self.frame = 0
        self.attack = 0
        self.fire = False
        self.health = 100
        self.stuck = False
        self.move = 0
        self.newMove = -1
        self.firePos = 0
#/////////////////////////////////////////////////////////////////////////////       
    def moveWizard(self):
        x = randint(1,40)
        y = randint(1,2)
        if x==40 and not self.fire:
            if y==1:
                self.stuck = False
                self.vx = 5
                self.newMove = 1
            if y==2:
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
        if self.stuck:
            self.frame = 0
#/////////////////////////////////////////////////////////////////////////////            
    def collide(self):
        self.rect.x += self.vx #scans through blocks and checks for collisions
        for x in range(self.rect.centerx // 16 - 1, self.rect.centerx // 16 + 2):
            for y in range(self.rect.centery // 16 - 2, self.rect.centery // 16 + 3):
                if blocks[y][x].id != 0 and self.rect.colliderect(blocks[y][x].rect):
                    if self.vx > 0:
                        self.rect.right = blocks[y][x].rect.left
                        vx = 0
                        self.stuck = True
                    elif self.vx < 0:
                        self.rect.left = blocks[y][x].rect.right
                        vx = 0
                        self.stuck = True
                        
        self.rect.y += self.vy #scans through blocks and checks for collisions
        for x in range(self.rect.centerx // 16 - 1, self.rect.centerx // 16 + 2):
            for y in range(self.rect.centery // 16 - 2, self.rect.centery // 16 + 3):
                if blocks[y][x].id != 0 and self.rect.colliderect(blocks[y][x].rect):
                    if self.vy > 0:
                        self.rect.bottom = blocks[y][x].rect.top
                    elif self.vy < 0:
                        self.rect.top = blocks[y][x].rect.bottom
                    self.vy = 5
                    
        self.blitPos = [self.rect.x - 8, self.rect.y - 7]

                     
            
#/////////////////////////////////////////////////////////////////////////
    def clear(self):
        draw.rect(playerSurface, (0, 0, 0, 0), (self.blitPos[0] - 300, self.blitPos[1] - 50, 550, 150))
#/////////////////////////////////////////////////////////////////////////        
    def draw(self):
        self.attack = randint(1,50)
        if self.fire:
            if self.move == 1:
                playerSurface.blit(wizardPics[2][0],(self.rect.x -4 + self.firePos, self.rect.y - 7))
                self.firePos += 5
            elif self.move == 0:
                playerSurface.blit(wizardPics[2][1],(self.rect.x - 60 + self.firePos, self.rect.y - 7))
                self.firePos -= 5
            if abs(self.firePos) > 150:
                self.fire = False
        if self.attack == 50:
            if not self.fire:
                if self.move == 1:
                    playerSurface.blit(wizardPics[2][0],(self.rect.x -4, self.rect.y - 7))
                    self.fire = True
                if self.move == 0:
                    playerSurface.blit(wizardPics[2][1],(self.rect.x - 60, self.rect.y - 7))
                    self.fire = True
                self.firePos = 0
            elif self.firePos > 50:
                self.fire = False
        pic = wizardPics[self.move][int(self.frame)]
        playerSurface.blit(pic,self.blitPos)
#############################################################################
class PurpleSlime:
    def __init__(self,x,y,w,h):
        self.rect = Rect(x,y,w,h)
        self.blitPos = [x - 8, y - 7]
        self.vx = 0
        self.vy = 0
        self.jumping = False
        self.right = False
        self.left = False
        self.frame = 0
        self.attack = 0
        self.health = 500
        self.status = "Alive"
#////////////////////////////////////////////////////////////////////////////
    def moveSlime(self):
        distance = abs(player.rect.x - slime.rect.x)
        x = randint(1,60)
        if x == 60:
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
        self.rect.x += self.vx
        for x in range(self.rect.centerx // 16 - 1, self.rect.centerx // 16 + 2):
            for y in range(self.rect.centery // 16 - 2, self.rect.centery // 16 + 3):
                if blocks[y][x].id != 0 and self.rect.colliderect(blocks[y][x].rect):
                    if self.vx > 0:
                        self.rect.right = blocks[y][x].rect.left
                    elif self.vx < 0:
                        self.rect.left = blocks[y][x].rect.right
        self.rect.y += self.vy            
        for x in range(self.rect.centerx // 16 - 1, self.rect.centerx // 16 + 2):
            for y in range(self.rect.centery // 16 - 2, self.rect.centery // 16 + 3):
                if blocks[y][x].id != 0 and self.rect.colliderect(blocks[y][x].rect):
                    self.vy = 5
                    if self.vy > 0:
                        self.rect.bottom = blocks[y][x].rect.top
                        self.jumping = False
                    elif self.vy < 0:
                        self.rect.top = blocks[y][x].rect.bottom

        if self.right and self.vx > 0:
            self.vx -= 0.7
        else:
            self.vx = 0
            self.jumping = False
            self.right = False

        if self.left and self.vx <0:
            self.vx += 0.7
        else:
            self.vx = 0
            self.jumping = False
            self.left = False
        if self.vy < 30:
            self.vy += 0.7
        if self.vy == 0:
            self.jumping = False
        

        self.blitPos = [self.rect.x - 8, self.rect.y - 7]
        self.attack = randint(1,25)
#////////////////////////////////////////////////////////////////////////////
    def clear(self):
        draw.rect(playerSurface, (0, 0, 0, 0), (self.blitPos[0] - 50, self.blitPos[1] - 50, 150, 150))
#///////////////////////////////////////////////////////////////////////////
    def draw(self):
        x=randint(1,5)
        if x==5:
            if self.frame<3:
                self.frame+=1
            else:
                self.frame=0
        pic = purpleSlimePics[int(self.frame)]
        playerSurface.blit(pic,self.blitPos)
############################################################################          
class Slime:
    def __init__(self, x, y, w, h):
        self.rect = Rect(x, y, w, h)
        self.blitPos = [ x - 8, y - 7]
        self.vx = 0
        self.vy = 0
        self.jumping = False
        self.right = False
        self.left = False
        self.frame = 0
        self.attack = 0
        self.health = 100
        self.status = "Alive"
    def moveSlime(self):
        distance = abs(player.rect.x - slime.rect.x)
        x = randint(1,60)
        if x==60:
            if distance < 500: 
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
    def collide(self):
        self.rect.x += self.vx
        for x in range(self.rect.centerx // 16 - 1, self.rect.centerx // 16 + 2):
            for y in range(self.rect.centery // 16 - 2, self.rect.centery // 16 + 3):
                if blocks[y][x].id != 0 and self.rect.colliderect(blocks[y][x].rect):
                    if self.vx > 0:
                        self.rect.right = blocks[y][x].rect.left
                    elif self.vx < 0:
                        self.rect.left = blocks[y][x].rect.right
        self.rect.y += self.vy            
        for x in range(self.rect.centerx // 16 - 1, self.rect.centerx // 16 + 2):
            for y in range(self.rect.centery // 16 - 2, self.rect.centery // 16 + 3):
                if blocks[y][x].id != 0 and self.rect.colliderect(blocks[y][x].rect):
                    self.vy = 5
                    if self.vy > 0:
                        self.rect.bottom = blocks[y][x].rect.top
                        self.jumping = False
                    elif self.vy < 0:
                        self.rect.top = blocks[y][x].rect.bottom

        if self.right and self.vx > 0:
            self.vx -= 0.7
        else:
            self.vx = 0
            self.jumping = False
            self.right = False

        if self.left and self.vx <0:
            self.vx += 0.7
        else:
            self.vx = 0
            self.jumping = False
            self.left = False
        if self.vy < 30:
            self.vy += 0.7
        if self.vy == 0:
            self.jumping = False
        

        self.blitPos = [self.rect.x - 8, self.rect.y - 7]
        self.attack = randint(1,25)
        
    def clear(self):
        draw.rect(playerSurface, (0, 0, 0, 0), (self.blitPos[0] - 50, self.blitPos[1] - 50, 150, 150))
        
    def draw(self):
        x=randint(1,5)
        if x==5:
            if self.frame<3:
                self.frame+=1
            else:
                self.frame=0
        pic = slimePics[int(self.frame)]
        playerSurface.blit(pic,self.blitPos)
#########################################################################
class Player:
    def __init__(self, x, y, w, h):
        self.rect = Rect(x, y, w, h)
        self.blitPos = [x - 8, y - 7]
        self.vx = 0
        self.vy = 0
        self.jumping = False
        self.move = 0
        self.newMove = -1
        self.frame = 0
        self.health = 100
        self.status = "Alive"

    def movePlayer(self):
        keys = key.get_pressed()

        self.newMove = -1

        if keys[K_RIGHT] and keys[K_LEFT]:
            self.frame = 0

        else:
            if keys[K_RIGHT] and self.rect.x < worldSize[0] * 16 - 629:
                if not self.jumping:
                    self.newMove = 2
                self.vx = 3
            elif keys[K_LEFT] and self.rect.x > 629:
                if not self.jumping:
                    self.newMove = 5
                self.vx = -3
            else:
                self.frame = 0

        if keys[K_UP] and not self.jumping:
            self.vy = -15
            self.jumping = True
            if self.move == 2 or self.move == 1:
                self.newMove = 1
            else:
                self.newMove = 4

        elif self.jumping:
            if keys[K_RIGHT]:
                self.newMove = 1
            elif keys[K_LEFT]:
                self.newMove = 4

        if not self.jumping and self.move == 1:
            self.move = 2

        if self.move == self.newMove:  # 0 is a standing pose, so we want to skip over it when we are moving
            self.frame = self.frame + 0.6  # adding 0.2 allows us to slow down the animation
            if self.frame >= len(pics[self.move]):
                self.frame = 1
        elif self.newMove != -1:  # a move was selected
            self.move = self.newMove  # make that our current move
            self.frame = 1

    def collide(self):
        self.rect.y += self.vy
        for x in range(self.rect.centerx // 16 - 1, self.rect.centerx // 16 + 2):
            for y in range(self.rect.centery // 16 - 2, self.rect.centery // 16 + 3):
                if blocks[y][x].id != 0 and self.rect.colliderect(blocks[y][x].rect):
                    if self.vy > 0:
                        self.rect.bottom = blocks[y][x].rect.top
                        self.jumping = False
                    elif self.vy < 0:
                        self.rect.top = blocks[y][x].rect.bottom
                    self.vy = 5

        self.rect.x += self.vx
        for x in range(self.rect.centerx // 16 - 1, self.rect.centerx // 16 + 2):
            for y in range(self.rect.centery // 16 - 2, self.rect.centery // 16 + 3):
                if blocks[y][x].id != 0 and self.rect.colliderect(blocks[y][x].rect):
                    if self.vx > 0:
                        self.rect.right = blocks[y][x].rect.left
                    elif self.vx < 0:
                        self.rect.left = blocks[y][x].rect.right

                    ##        if self.jumping and self.vy < 30:
                    ##            self.vy += 2
                    ##        elif not self.jumping:
                    ##            self.vy = 5
        if self.vy < 30:
            self.vy += 2

        self.vx = 0

        self.blitPos = [self.rect.x - 8, self.rect.y - 7]

        for slime in slimeList:
            if slime.rect.colliderect(self.rect) and self.health>=10 and slime.attack==25:
                self.health -= 10
            else:
                self.heatlh = 0
                self.status = "Dead"
    def clear(self):
        draw.rect(playerSurface, (0, 0, 0, 0), (self.blitPos[0] - 50, self.blitPos[1] - 50, 150, 150))

    def draw(self):
        pic = pics[self.move][int(self.frame)]
        playerSurface.blit(pic, self.blitPos)

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


blocks = []
for y in range(len(blockList)):
    row = []
    for x in range(len(blockList[0])):
        row.append(Block(blockList[y][x], x, y))
    blocks.append(row)

inventoryList = []
for i in range(10):
    inventoryList.append(inventory(i, inventoryPickleList[i][0], 1, inventoryPickleList[i][1]))

drawBlocks(0, len(blocks[0]) - 1, 0, len(blocks) - 1)
###########################################################################
player = Player(629, 339, 24, 40)

wizard = Wizard(780,319,20,37)

slimeList=[]
for i in range(5):
    slime= Slime(randint(700,1100),339,14,14)
    slimeList.append(slime)

purpleSlimeList=[]
for i in range(3):
    purpleSlime = PurpleSlime(randint(700,1000),339,28,28)
    purpleSlimeList.append(purpleSlime)


EMPTY = 0
BLOCK = 1
TOOL = 2
deleteList = []
##########################################################################
import menu

pygame.mixer.music.load(music[0])
pygame.mixer.music.play()

running = True
positive = True
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
            if evt.button == 4:
                if inventory.selected == 9:
                    inventory.selected = 0
                else:
                    inventory.selected += 1
            if evt.button == 5:
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
#///////////////////////////////////////////////////////////////////////////
    if time <= 5184000 and positive:
        time+=5000
    else:
        positive = False
    if time >= 0 and not positive:
        time-=5000
    else:
        positive = True

    alphaCount=time//20330
    screen.fill((0, 0, 0))
    background.set_alpha(alphaCount)
    screen.blit(background,(0,0))
#///////////////////////////////////////////////////////////////////////////
    if mb[0] == 1:
        blocks[(player.rect.y - 339 + my) // 16][(player.rect.x - 629 + mx) // 16].breakBlock()
        for x in range((player.rect.x - 629 + mx) // 16 - 1, (player.rect.x - 629 + mx) // 16 + 2):
            for y in range((player.rect.y - 339 + my) // 16 - 1, (player.rect.y - 339 + my) // 16 + 2):
                blocks[y][x].update()
        for x in range((player.rect.x - 629 + mx) // 16 - 1, (player.rect.x - 629 + mx) // 16 + 2):
            for y in range((player.rect.y - 339 + my) // 16 - 1, (player.rect.y - 339 + my) // 16 + 2):
                blocks[y][x].draw()

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
            if inventoryList[inventory.selected].quantity > 1:
                inventoryList[inventory.selected].quantity -= 1
            else:
                inventoryList[inventory.selected].id = 0
                inventoryList[inventory.selected].type = EMPTY
                inventoryList[inventory.selected].quantity = 0

    if len(dropsList) != 0:
        for drop in dropsList:
            drop.collidePlayer1()
        dropsList = [drop for drop in dropsList if not drop.delete]
        for drop in dropsList:
            if not drop.dist:
                drop.collidePlayer2()
        dropsList = [drop for drop in dropsList if not drop.delete]
        for drop in dropsList:
            if not drop.dist:
                drop.collide()
            drop.clear()

    for slime in slimeList:
        slime.moveSlime()
        slime.collide()
        slime.clear()

    for purpSlime in purpleSlimeList:
        purpSlime.moveSlime()
        purpSlime.collide()
        purpSlime.clear()

    wizard.moveWizard()
    wizard.collide()
    wizard.clear()
        
    player.movePlayer()
    player.collide()
    player.clear()

    if len(dropsList) != 0:
        for drop in dropsList:
            drop.draw()

    for slime in slimeList:
        slime.draw()

    for purpSlime in purpleSlimeList:
        purpSlime.draw()
        
    wizard.draw()
    player.draw()

    for item in inventoryList:
        item.draw()


    if player.rect.y >= 339:
        screen.blit(blocksSurface.subsurface(player.rect.x - 629, player.rect.y - 339, 1280, 720), (0, 0))
        screen.blit(playerSurface.subsurface(player.rect.x - 629, player.rect.y - 339, 1280, 720), (0, 0))
        # screen.blit(playerSurface.subsurface(player.blitPos[0], player.blitPos[1], 650, 320), (621, 339))
    else:
        screen.blit(blocksSurface.subsurface(player.rect.x - 629, 0, 1280, 720), (0, abs(player.rect.y - 339)))
        screen.blit(playerSurface.subsurface(player.rect.x - 629, 0, 1280, 720), (0, abs(player.rect.y - 339)))
        # screen.blit(playerSurface.subsurface(player.rect.x, 0, 650, 320), (612, abs(player.rect.y - 283)))

    screen.blit(uiSurface, (0, 0))

    display.flip()
    clock.tick(60)
    display.set_caption("FSE FPS = {0:.0f}".format(clock.get_fps()))

with open('blockspickle.pickle', 'wb') as f:
    pickle.dump(blockList, f)

with open("inventory.pickle", "wb") as f:
    pickle.dump(inventoryPickleList, f)

quit()
