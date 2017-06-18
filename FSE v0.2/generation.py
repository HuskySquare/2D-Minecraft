#{0:"Air, 1:"Dirt",2:"Stone",3:"Grass",5:"Pickaxe",6:"Iron",7:"Tree Trunk".8:"Tree Main Branch",9:"Gel"}
import numpy as np
from random import *
import pickle
pieces=[]
anchor=20
length=0

for i in range(780):
    x=randint(-3,3)
    anchor+=x
    if anchor<=6:
        anchor+=3
    if anchor>=79:
        anchor-=3

    temp=np.zeros((85,1),dtype="int")
    temp[anchor:].fill(1)
    temp[anchor]=3

    if i!=0:
        if not length:

            length = randint(0, 10)
            #weighted_choice=[(1,)
            x=choice([84,0])
            temp=np.delete(pieces[i-1],[x])
            if x:
                temp = np.insert(temp, 0, 0).reshape((85, 1))
                anchor+=1

            else:
                temp = np.append(temp, 0).reshape((85, 1))


            # temp=np.insert(temp,x,0).reshape((85,1))
        else:
            temp=pieces[i-1]
            length-=1
        # else:
        #     temp=pieces[i-1]
        #     x=randint(-1,0)
        #     if x==-1:
        #         temp=np.delete(temp,[84])
        #     else:
        #         temp=np.delete(temp,[0])
        #
        #
        #     if x:
        #         temp = np.insert(temp,0,0).reshape(85,1)
        #     else:
        #         temp=np.append(temp,0).reshape((85,1))

        # temp.reshape((85,1))



    pieces.append(temp)

blocks=np.concatenate(pieces,axis=1)

blocks[60:,:]=2
for i in range(780):
    if randint(0,1):
        blocks[:,i][randint(30,84)]=6
    temp=blocks[:,i]

    anchor=np.where(temp==3)[0][0]


    for j in range(randint(5,10)):
        try:
            temp[anchor+randint(5,35)]=2
        except IndexError:
            continue

#Making caves-----------------------------------------
for i in range(randint(15,30)):

    width, height = randint(5, 20), randint(5, 20)
    temp = np.random.normal(size=(width, height))
    temp = np.fabs(temp)
    temp = temp.astype(int)
    x,y=randint(30,84-width),randint(0,780-height)
    blocks[x:x+width,y:y+height]=temp

with open('blockspickle.pickle', 'wb') as f:
    pickle.dump(blocks, f)



# for i in blocks():

def genTree(x,y,h):
    blocks[x-1,y]=7
    blocks[x+1,y]=7
    blocks[:,x][y-h:y+1]=8