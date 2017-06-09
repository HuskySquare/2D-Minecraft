from pygame import *

init()

screen = display.set_mode((40, 1140), DOUBLEBUF)

h = image.load("Player_Hair_15.png")
screen.fill((255,255,255))

h.fill((0, 150, 150), special_flags=BLEND_SUB)

screen.blit(h, (0, 0))

display.flip()

time.wait(10000)

quit()
