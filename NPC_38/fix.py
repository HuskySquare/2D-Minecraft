import os,glob
files=glob.glob("*.png")
for i in files:
    if "flip" in i:
        os.remove(i)
