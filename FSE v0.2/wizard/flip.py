import glob
from pygame import *
files=glob.glob("*.png")
for i in files:
    pic=image.load(i)        
    pic=transform.flip(pic,True,False)
    image.save(pic,"skeleton_B_"+str(i)+".png")
