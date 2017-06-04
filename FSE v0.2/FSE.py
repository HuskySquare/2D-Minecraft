from random import *
import numpy as np
import pickle
from time import time as tm
from pygame import *

with open("blockspickle.pickle", "rb") as f:
    blockList = pickle.load(f)

screen = display.set_mode((1280, 720))

clock = time.Clock()

worldSize = (780, 85)

blocksSurface = Surface((worldSize[0] * 16, worldSize[1] * 16), SRCALPHA)
blocksSurface.fill((0, 0, 0, 0))
playerSurface = Surface((worldSize[0] * 16, worldSize[1] * 16), SRCALPHA)
playerSurface.fill((0, 0, 0, 0))
mainSurface = Surface((1280, 720), SRCALPHA)

background = image.load("background.png").convert(32, SRCALPHA)
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
        pics.append(transform.flip(sprite.subsurface((0, i, 40, 56)), False, True))
    except:
        pass

pics = [pics[0:5], pics[5], pics[6:21], pics[21:26], pics[26], pics[27:]]

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

block3 = [block3_0, block3_1, block3_2, block3_3, block3_4, block3_5, block3_6, block3_7, block3_8, block3_9, block3_10, block3_11, block3_12, block3_13, block3_14, block3_15]
blockImg = [False, block1, block2, block3]

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

    def movePlayer(self):
        keys = key.get_pressed()

        self.newMove = -1

        if keys[K_RIGHT] and keys[K_LEFT]:
            self.frame = 0

        else:
            if keys[K_RIGHT] and self.rect.x < worldSize[0] * 16 - 629:
                self.newMove = 2
                self.vx = 3
            elif keys[K_LEFT] and self.rect.x > 629:
                self.newMove = 5
                self.vx = -3
            else:
                self.frame = 0

        if keys[K_UP] and not self.jumping:
            self.vy = -15
            self.jumping = True
            self.newMove = 1

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

        self.rect.x += self.vx
        for x in range(self.rect.centerx // 16 - 1, self.rect.centerx // 16 + 2):
            for y in range(self.rect.centery // 16 - 2, self.rect.centery // 16 + 3):
                if blocks[y][x].id != 0 and self.rect.colliderect(blocks[y][x].rect):
                    if self.vx > 0:
                        self.rect.right = blocks[y][x].rect.left
                    elif self.vx < 0:
                        self.rect.left = blocks[y][x].rect.right

        if self.jumping and self.vy < 30:
            self.vy += 2
        elif not self.jumping:
            self.vy = 5
        self.vx = 0

    def draw(self):
        pic = pics[self.move][int(self.frame)]
        draw.rect(playerSurface, (0, 0, 0, 0), (self.blitPos[0], self.blitPos[1], 80, 56))
        playerSurface.blit(pic, self.blitPos)

class Block:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        self.rect = Rect(x * 16, y * 16, 16, 16)
        self.condition = 6
        top = True
        down = True
        left = True
        right = True
        if y != 0 and blockList[y-1][x] == 0:
            top = False
        if y != worldSize[1] - 1 and blockList[y+1][x] == 0:
            down = False
        if x != 0 and blockList[y][x-1] == 0:
            left = False
        if x != worldSize[0] - 1 and blockList[y][x+1] == 0:
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

drawBlocks(0, len(blocks[0]) - 1, 0, len(blocks) - 1)

player = Player(629, 339, 24, 42)

running = True

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

    if mb[0] == 1:
        blocks[(player.rect.y - 339 + my)//16][(player.rect.x - 629 + mx)//16].id = 0
        for x in range((player.rect.x - 629 + mx)//16 - 1, (player.rect.x - 629 + mx)//16 + 2):
            for y in range((player.rect.y - 339 + my) // 16 - 1, (player.rect.y - 339 + my)//16 + 2):
                blocks[y][x].update()
        for x in range((player.rect.x - 629 + mx) // 16 - 1, (player.rect.x - 629 + mx) // 16 + 2):
            for y in range((player.rect.y - 339 + my) // 16 - 1, (player.rect.y - 339 + my) // 16 + 2):
                blocks[y][x].draw()

    if mb[2] == 1:
        blocks[(player.rect.y - 339 + my)//16][(player.rect.x - 629 + mx)//16].id = 1
        for x in range((player.rect.x - 629 + mx)//16 - 1, (player.rect.x - 629 + mx)//16 + 2):
            for y in range((player.rect.y - 339 + my) // 16 - 1, (player.rect.y - 339 + my)//16 + 2):
                blocks[y][x].update()
        for x in range((player.rect.x - 629 + mx) // 16 - 1, (player.rect.x - 629 + mx) // 16 + 2):
            for y in range((player.rect.y - 339 + my) // 16 - 1, (player.rect.y - 339 + my) // 16 + 2):
                blocks[y][x].draw()

    player.movePlayer()
    player.collide()
    player.draw()
    screen.blit(background, (0, 0))
    if player.rect.y >= 283:
        screen.blit(blocksSurface.subsurface(player.rect.x - 629, player.rect.y - 339, 1280, 720), (0, 0))
        screen.blit(playerSurface.subsurface(player.rect.x - 629, player.rect.y - 339, 1280, 720), (0, 0))
        #screen.blit(playerSurface.subsurface(player.blitPos[0], player.blitPos[1], 650, 320), (621, 339))
    else:
        screen.blit(blocksSurface.subsurface(player.rect.x - 629, 0, 1248, 704), (0, abs(player.rect.y - 283)))
        #screen.blit(playerSurface.subsurface(player.rect.x, 0, 650, 320), (612, abs(player.rect.y - 283)))

    display.flip()
    clock.tick(60)
    display.set_caption("FSE FPS = {0:.0f}".format(clock.get_fps()))

with open('blockspickle.pickle', 'wb') as f:
    pickle.dump(blockList, f)

quit()
