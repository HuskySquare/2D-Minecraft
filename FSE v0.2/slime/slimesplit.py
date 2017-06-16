from pygame import *
thing = image.load("Sky_Slime_1.png")
newSurface = Surface((14, 96), SRCALPHA)
newSurface.blit(thing, (0, 0))
c = 0

for i in range(0, 96, 24):
    name = "slime_" + str(c) + ".png"
    image.save(newSurface.subsurface(0, i, 14, 24), name)
    c += 1
