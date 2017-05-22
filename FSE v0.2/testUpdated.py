from random import *
import numpy as np
import pickle
from time import time as tm
from pygame import *

with open("blockspickle.pickle", "rb") as f:
    blocks = pickle.load(f)

#with open("blockspickle.pickle", "rb") as f:
#    blocks_default = pickle.load(f)

screen = display.set_mode((1248, 704))

clock = time.Clock()

#780 x 45
##blocks=np.zeros((20,780))
##blocks=np.vstack((blocks,np.ones((5,780))))
##blocks=np.vstack((blocks,np.random.randint(1,3,size=(20,780))))
blocksSurface = Surface((12480, 1360), SRCALPHA)
blocksSurface.fill((0, 0, 0, 0))
playerSurface = Surface((12480, 1360), SRCALPHA)

blocks = [[0 for i in range(780)] for j in range(20)]
for i in range(5):
    blocks.append([1 for j in range(780)])
for i in range(20):
    blocks.append([randint(1,2) for j in range(780)])
for i in range(40):
    blocks.append([2 for j in range(780)])

blocks = np.array(blocks)

marioRect = Rect(612, 286, 24, 37)
pos = 624
vx = 0
vy = 0
jumping = False
xCollide = False

background = image.load("background.png").convert(32, SRCALPHA)
background = transform.scale(background, (1280, 720))
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
block1 = [block1_0, block1_1, block1_2, block1_3, block1_4, block1_5, block1_6, block1_7, block1_8, block1_9, block1_10, block1_11, block1_12, block1_13, block1_14, block1_15]
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

block2 = [block2_0, block2_1, block2_2, block2_3, block2_4, block2_5, block2_6, block2_7, block2_8, block2_9, block2_10, block2_11, block2_12, block2_13, block2_14, block2_15]
blockImg = [False, block1, block2]
class player():
    def __init__(self,name):
        self.name=name
        self.health=100
    
def moveMario():
    ''' moveMario controls the location of Mario as well as adjusts the move and frame
        variables to ensure the right picture is drawn.
    '''
    global move, frame, marioX, marioY, pos, vx, vy, jumping
    keys = key.get_pressed()

    newMove = -1
    if  keys[K_RIGHT] and keys[K_LEFT]:
        frame=0
        pass
    else:
        if keys[K_RIGHT] and pos < 11368:
            newMove = RIGHT
            marioX += 2
            vx = 2
            pos+=5
        elif keys[K_LEFT] and pos > 649:
            newMove = LEFT
            marioX -= 2
            pos-=5
            vx = -2
        else:
            frame = 0

    if keys[K_UP] and not jumping:
        vy = -20
        jumping = True

    if move == newMove:     # 0 is a standing pose, so we want to skip over it when we are moving
        frame = frame + 0.6 # adding 0.2 allows us to slow down the animation
        if frame >= len(pics[move]):
            frame = 1
    elif newMove != -1:     # a move was selected
        move = newMove      # make that our current move
        frame = 1

    screen.blit(background, (0, 0))
    #blocksSurface.fill((0, 0, 0, 0))
    screen.blit(blocksSurface, (624 - pos, 0))
    drawPlayer()

def marioCollide():
    global vx, vy, jumping, xCollide
    marioRect.y += vy

    for x in range(marioRect.centerx // 16 - 1, marioRect.centerx // 16 + 2):
        for y in range(marioRect.centery // 16 - 2, marioRect.centery // 16 + 3):
            if blocks[y][x] != 0 and marioRect.colliderect(Rect(x * 16, y * 16, 16, 16)):
                if vy > 0:
                    marioRect.bottom = Rect(x * 16, y * 16, 16, 16).top
                    jumping = False
                elif vy < 0:
                    marioRect.top = Rect(x * 16, y * 16, 16, 16).bottom
    vy = 0

    marioRect.x += vx
    
    for x in range(marioRect.centerx // 16 - 1, marioRect.centerx // 16 + 2):
        for y in range(marioRect.centery // 16 - 2, marioRect.centery // 16 + 3):
            if blocks[y][x] != 0 and marioRect.colliderect(Rect(x * 16, y * 16, 16, 16)):
                if vx > 0:
                    marioRect.right = Rect(x * 16, y * 16, 16, 16).left
                    xCollide = True
                elif vx < 0:
                    marioRect.left = Rect(x * 16, y * 16, 16, 16).right
                    xCollide = True
    vx = 0
    vy = 5
    drawPlayer()

def makeMove(name,start,end):
    ''' This returns a list of pictures. They must be in the folder "name"
        and start with the name "name".
        start, end - The range of picture numbers 
    '''
    move = []
    for i in range(start,end+1):
        move.append(image.load("%s/%s%03d.png" % (name,name,i)))
    return move

def drawPlayer():
    pic = pics[move][int(frame)]
    screen.blit(background, (0, 0))
    screen.blit(blocksSurface.subsurface(marioRect.x - 612, marioRect.y - 283, 1248, 704), (0, 0))
    draw.rect(playerSurface, (0, 0, 0, 0), (marioRect.x - 2, marioRect. y - 5, 31, 55))
    playerSurface.blit(pic, (marioRect.x, marioRect.y))
    #screen.blit(pic, (624-pic.get_width()//2, 323-pic.get_height()))
    screen.blit(playerSurface.subsurface(marioRect.x - 612, marioRect.y - 283, 1248, 704), (0, 0))
    display.flip()

def drawScene():
    screen.blit(background, (0, 0))
    blocksSurface.fill((0, 0, 0, 0))
    for x in range(pos//16 - 40, pos//16 + 40): #779, pos//16 - 650, pos//16 + 650
        for y in range(44): #44
            if blocks[y][x] != 0:
                top = True
                down = True
                left = True
                right = True
                if y != 0 and blocks[y-1][x] == 0:
                    top = False
                if y != 29 and blocks[y+1][x] == 0:
                    down = False
                if x != 0 and blocks[y][x-1] == 0:
                    left = False
                if x != 51 and blocks[y][x+1] == 0:
                    right = False

                if top and down and left and right:
                    blocksSurface.blit(blockImg[blocks[y][x]][0], (x * 16, y * 16))

                elif not top and not down and not left and not right:
                    blocksSurface.blit(blockImg[blocks[y][x]][11], (x * 16, y * 16))

                else:
                    if top and down and right:
                        blocksSurface.blit(blockImg[blocks[y][x]][2], (x * 16, y * 16))

                    elif down and left and right:
                        blocksSurface.blit(blockImg[blocks[y][x]][1], (x * 16, y * 16))

                    elif top and down and left:
                        blocksSurface.blit(blockImg[blocks[y][x]][3], (x * 16, y * 16))

                    elif top and left and right:
                        blocksSurface.blit(blockImg[blocks[y][x]][4], (x * 16, y * 16))

                    else:
                        if top:
                            if left:
                                blocksSurface.blit(blockImg[blocks[y][x]][5], (x * 16, y * 16))
                            elif right:
                                blocksSurface.blit(blockImg[blocks[y][x]][6], (x * 16, y * 16))
                            elif down:
                                blocksSurface.blit(blockImg[blocks[y][x]][7], (x * 16, y * 16))
                            else:
                                blocksSurface.blit(blockImg[blocks[y][x]][12], (x * 16, y * 16))
                        elif down:
                            if left:
                                blocksSurface.blit(blockImg[blocks[y][x]][8], (x * 16, y * 16))
                            elif right:
                                blocksSurface.blit(blockImg[blocks[y][x]][9], (x * 16, y * 16))
                            else:
                                blocksSurface.blit(blockImg[blocks[y][x]][13], (x * 16, y * 16))
                        elif left:
                            if right:
                                blocksSurface.blit(blockImg[blocks[y][x]][10], (x * 16, y * 16))
                            else:
                                blocksSurface.blit(blockImg[blocks[y][x]][14], (x * 16, y * 16))
                        else:
                            blocksSurface.blit(blockImg[blocks[y][x]][15], (x * 16, y * 16))
    screen.blit(blocksSurface, (624 - pos, 0))

def drawWorld():
    screen.blit(background, (0, 0))
    blocksSurface.fill((0, 0, 0, 0))
    for x in range(779): #779, pos//16 - 650, pos//16 + 650
        for y in range(84): #44
            if blocks[y][x] != 0:
                top = True
                down = True
                left = True
                right = True
                if y != 0 and blocks[y-1][x] == 0:
                    top = False
                if y != 29 and blocks[y+1][x] == 0:
                    down = False
                if x != 0 and blocks[y][x-1] == 0:
                    left = False
                if x != 51 and blocks[y][x+1] == 0:
                    right = False

                if top and down and left and right:
                    blocksSurface.blit(blockImg[blocks[y][x]][0], (x * 16, y * 16))

                elif not top and not down and not left and not right:
                    blocksSurface.blit(blockImg[blocks[y][x]][11], (x * 16, y * 16))

                else:
                    if top and down and right:
                        blocksSurface.blit(blockImg[blocks[y][x]][2], (x * 16, y * 16))

                    elif down and left and right:
                        blocksSurface.blit(blockImg[blocks[y][x]][1], (x * 16, y * 16))

                    elif top and down and left:
                        blocksSurface.blit(blockImg[blocks[y][x]][3], (x * 16, y * 16))

                    elif top and left and right:
                        blocksSurface.blit(blockImg[blocks[y][x]][4], (x * 16, y * 16))

                    else:
                        if top:
                            if left:
                                blocksSurface.blit(blockImg[blocks[y][x]][5], (x * 16, y * 16))
                            elif right:
                                blocksSurface.blit(blockImg[blocks[y][x]][6], (x * 16, y * 16))
                            elif down:
                                blocksSurface.blit(blockImg[blocks[y][x]][7], (x * 16, y * 16))
                            else:
                                blocksSurface.blit(blockImg[blocks[y][x]][12], (x * 16, y * 16))
                        elif down:
                            if left:
                                blocksSurface.blit(blockImg[blocks[y][x]][8], (x * 16, y * 16))
                            elif right:
                                blocksSurface.blit(blockImg[blocks[y][x]][9], (x * 16, y * 16))
                            else:
                                blocksSurface.blit(blockImg[blocks[y][x]][13], (x * 16, y * 16))
                        elif left:
                            if right:
                                blocksSurface.blit(blockImg[blocks[y][x]][10], (x * 16, y * 16))
                            else:
                                blocksSurface.blit(blockImg[blocks[y][x]][14], (x * 16, y * 16))
                        else:
                            blocksSurface.blit(blockImg[blocks[y][x]][15], (x * 16, y * 16))
    screen.blit(blocksSurface, (624 - pos, 0))

def updateBlocks(blockX, blockY):
    screen.blit(background, (0, 0))
    draw.rect(blocksSurface, (0, 0, 0, 0), (blockX * 16 - 16, blockY * 16 - 16, 48, 48))
    for x in range(blockX - 1, blockX + 2):  # 779, pos//16 - 650, pos//16 + 650
        for y in range(blockY - 1, blockY + 2):  # 44
            if blocks[y][x] != 0:
                top = True
                down = True
                left = True
                right = True
                if y != 0 and blocks[y - 1][x] == 0:
                    top = False
                if y != 29 and blocks[y + 1][x] == 0:
                    down = False
                if x != 0 and blocks[y][x - 1] == 0:
                    left = False
                if x != 51 and blocks[y][x + 1] == 0:
                    right = False

                if top and down and left and right:
                    blocksSurface.blit(blockImg[blocks[y][x]][0], (x * 16, y * 16))

                elif not top and not down and not left and not right:
                    blocksSurface.blit(blockImg[blocks[y][x]][11], (x * 16, y * 16))

                else:
                    if top and down and right:
                        blocksSurface.blit(blockImg[blocks[y][x]][2], (x * 16, y * 16))

                    elif down and left and right:
                        blocksSurface.blit(blockImg[blocks[y][x]][1], (x * 16, y * 16))

                    elif top and down and left:
                        blocksSurface.blit(blockImg[blocks[y][x]][3], (x * 16, y * 16))

                    elif top and left and right:
                        blocksSurface.blit(blockImg[blocks[y][x]][4], (x * 16, y * 16))

                    else:
                        if top:
                            if left:
                                blocksSurface.blit(blockImg[blocks[y][x]][5], (x * 16, y * 16))
                            elif right:
                                blocksSurface.blit(blockImg[blocks[y][x]][6], (x * 16, y * 16))
                            elif down:
                                blocksSurface.blit(blockImg[blocks[y][x]][7], (x * 16, y * 16))
                            else:
                                blocksSurface.blit(blockImg[blocks[y][x]][12], (x * 16, y * 16))
                        elif down:
                            if left:
                                blocksSurface.blit(blockImg[blocks[y][x]][8], (x * 16, y * 16))
                            elif right:
                                blocksSurface.blit(blockImg[blocks[y][x]][9], (x * 16, y * 16))
                            else:
                                blocksSurface.blit(blockImg[blocks[y][x]][13], (x * 16, y * 16))
                        elif left:
                            if right:
                                blocksSurface.blit(blockImg[blocks[y][x]][10], (x * 16, y * 16))
                            else:
                                blocksSurface.blit(blockImg[blocks[y][x]][14], (x * 16, y * 16))
                        else:
                            blocksSurface.blit(blockImg[blocks[y][x]][15], (x * 16, y * 16))
    screen.blit(blocksSurface, (624 - pos, 0))

RIGHT = 0 # These are just the indicies of the moves
LEFT = 1
pos = 624

pics = []
pics.append(makeMove("Mario",1,6))      # RIGHT
pics.append(makeMove("Mario",19,24))    # LEFT

frame=0     # current frame within the move
move=0      # current move being performed
marioX, marioY = 400,300

running = True

##logo = image.load("images/logo.png").convert(32, SRCALPHA)
##logoSurface = Surface((1248, 720))
##logoSurface.set_colorkey((0, 0, 0))
##logoSurface.blit(logo, (381, 250))

    
##for i in range(255, 0, -1):
##    screen.blit(background, (0, 0))
##    logoSurface.set_alpha(i)
##    screen.blit(logoSurface, (0, 0))
##    display.flip()

def genMountain(x1, x2, h):
    # for x in range(abs(x2 - x1)):
    #     for y in range():
    for x in range(x1, x2 + 1):
        for y in range(int(((h / ((x1**2)/4 - (x1*x2)/4 + (x2**2)/4)) * (x - (x1 + x2) / 2)**2 + 20 - h)), 20):
            #print(x, y)
            blocks[y][x] = 1

genMountain(2, 20, 20)
drawWorld()
drawPlayer()

# for x in range(52):
#     if 0 <= 1/10 * (x - 35)**2 < 30:
#         blocks[int(1/10 * (x - 35)**2)][x] = 1
#         for y in range(int(1/10 * (x - 35)**2), 30):
#             blocks[y][x] = 1

while running:
    #sTime = tm()
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
        if evt.type==KEYUP:
            moveMario()
    keys = key.get_pressed()
    

    if mb[0] == 1:
        blocks[my // 16][mx // 16 + (marioRect.x - 623) // 16] = 0
        updateBlocks(mx // 16 + (marioRect.x - 623) // 16, my // 16)
        #drawScene()
        #drawPlayer()

    if mb[2] == 1:
        blocks[my // 16][mx // 16 + (marioRect.x - 623) // 16] = 1
        updateBlocks(mx // 16 + (marioRect.x - 623) // 16, my // 16)
        #drawScene()
        #drawPlayer()
    moveMario()
    marioCollide()
    #drawPlayer()
    #print(blocksSurface.get_colorkey())
    #print(pos)
    #print(tm() - sTime)
    clock.tick(60)
    display.set_caption("dank gaem fps = {0:.0f}".format(clock.get_fps()))
    display.flip()

#blocks = blocks_default

with open('blockspickle.pickle', 'wb') as f:
    pickle.dump(blocks, f)

quit()
