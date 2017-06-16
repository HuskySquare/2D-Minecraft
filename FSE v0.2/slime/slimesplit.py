from pygame import *
thing = image.load("Sky_Slime_4.png")
newSurface = Surface((36, 152), SRCALPHA)
newSurface.blit(thing, (0, 0))
c = 0

for i in range(0, 152, 38):
    name = "slime2_" + str(c) + ".png"
    image.save(newSurface.subsurface(0, i, 36, 38), name)
    c += 1
