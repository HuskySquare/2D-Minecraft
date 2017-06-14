from pygame import *

init()

screen = display.set_mode((40, 56),DOUBLEBUF)

h = image.load("Player_Hair_15.png").subsurface(0,0,40,56)
screen.fill((255,255,255))

h.fill((220, 141, 50), special_flags=BLEND_SUB)
print(h.get_size())
screen.blit(h, (0, 0))
# ,(40,56,40,784)
display.flip()

time.wait(10000)

quit()
