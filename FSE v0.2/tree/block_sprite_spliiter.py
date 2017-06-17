from pygame import *

dirt_blocks = image.load("Tiles_5.png")
c = 0

##for x in range(dirt_blocks.get_width()):
##    print(dirt_blocks.get_at((x, 0)))
for y in range(0, 264, 22):
    for x in range(0, 176, 22):
        image.save(dirt_blocks.subsurface((x, y, 20, 20)), "tree_trunk_%i.png" %(c))
        c += 1
