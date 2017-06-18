from pygame import *

init()

screen = display.set_mode((100, 100),DOUBLEBUF)

h = image.load("Item_23.png")
screen.fill((255,255,255))

h.fill((255, 255, 0), special_flags=BLEND_SUB)
screen.blit(h, (0, 0))
# ,(40,56,40,784)
display.flip()

time.wait(5000)

quit()
