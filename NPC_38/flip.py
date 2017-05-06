import glob as glob
from pygame import *
files=glob.glob("*.png")
for i in files:
    pic=image.load(i)        
    pic=transform.flip(pic,True,False)
    image.save(pic,"{0}{1}.png".format(i[:4],int(i[4:i.find(".")])+17))
