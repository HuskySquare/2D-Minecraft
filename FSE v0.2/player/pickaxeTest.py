from pygame import *

surface = Surface((80, 1140), SRCALPHA, 32)

item_1 = image.load("Item_5.png")

posList = [(4, 16), (-25, 55), (0, 104), (9, 169), (18, 239)]
rotList = [-40, 140, 85, 30, 0]

for i in range(5):
    surface.blit(transform.rotate(item_1, rotList[i]), (20 + posList[i][0], posList[i][1]))

image.save(surface, "item_0.png")
