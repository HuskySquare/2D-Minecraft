from pygame import *

dirt_blocks = image.load("Tiles_6.png")
c = 0

##for x in range(dirt_blocks.get_width()):
##    print(dirt_blocks.get_at((x, 50)))
for y in range(0, 270, 18):
    for x in range(0, 288, 18):
        image.save(dirt_blocks.subsurface((x, y, 16, 16)), "ironore/ironore_block_%i.png" %(c))
        c += 1
