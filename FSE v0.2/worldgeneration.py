import numpy as np
from random import *
pieces=[]
anchor=20
for i in range(780):
    x=randint(-3,3)
    anchor+=x
    if anchor<=0:
        anchor+=3
    temp=np.zeros((85,1),dtype="int")
    temp[anchor:].fill(1)
    temp[anchor]=3
    for j in range(randint(5,30)):
        temp[anchor+randint(10,35)]=2

    pieces.append(temp)

    
blocks=np.concatenate(pieces,axis=1)
##print(blocks)

