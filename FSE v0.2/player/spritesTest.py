from pygame import *
init()

#screen = display.set_mode((40, 1140))

##spriteS = Surface((40, 1120), SRCALPHA, 32)
#spriteS = spriteS.convert_alpha()

##player0 = []
##playerHair = []
##
##for i in range(13):
##    player0.append(image.load("Contents/Images/Player_0_" + str(i) + ".png"))
##
##for i in range(1, 135):
##    playerHair.append(image.load("Contents/Images/Player_Hair_" + str(i) + ".png"))    

##for sprite in player0:
##    spriteS.blit(sprite, (0, 0))
##
##image.save(spriteS, "Sprite.png")
##
##print("done")
##quit()

##time.wait(1000)

##for hair in playerHair:
##    for sprite in player0:
##        screen.blit(sprite, (0, 0))
##    screen.blit(hair, (0, 0))
##    display.flip()
##    time.wait(200)
##    screen.fill((0, 0, 0))

surface = Surface((80, 1120), SRCALPHA, 32)
screen = display.set_mode((80, 1120))
#surface = surface.convert_alpha()
playerFileList = ["Player_Head", "Player_Hair_15", "Player_Undershirt", "Player_Shirt", "Player_Hands", "Player_Pants", "Player_Shoes"]

player_hands2 = image.load("Player_Hands2.png")

playerList = []

for player in playerFileList:
    playerList.append(image.load(player + ".png"))

item_1 = image.load("Item_0.png")
rot = 0
pos = [0, 0]
sprite = image.load("Sprite0.png")

running = True

while running:
    for evt in event.get():
        if evt.type == QUIT:
            running = False
        if evt.type == KEYDOWN:
            if evt.key == K_RIGHT:
                pos[0] += 1
            if evt.key == K_LEFT:
                pos[0] -= 1
            if evt.key == K_DOWN:
                pos[1] += 1
            if evt.key == K_UP:
                pos[1] -= 1
            if evt.key == K_q:
                rot += 5
            if evt.key == K_w:
                rot -= 5
            if evt.key == 13:
                print(pos, rot)

    screen.fill((0, 0 , 0))

    for player in playerList:
        screen.blit(player, (20, 0))

    screen.blit(transform.rotate(item_1, rot), pos)
    #screen.blit(item_1, (0, 0))

    screen.blit(player_hands2, (20, 0))

    display.flip()
            
"""for i in range(6, 1126, 56):
    image.save(sprite.subsurface((0, i, 40, 56)), "sprite_" + str(i) + ".png")

surface.blit(sprite, (0, 0))
for y in range(1140):
    print(surface.get_at((20, y)))"""
