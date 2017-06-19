#{0:"Air, 1:"Dirt",2:"Stone",3:"Grass",4:"Pickaxe",6:"Iron",7:"Tree Trunk".8:"Tree Main Branch",9:"Gel"}
import numpy as np
from random import *
import pickle
pieces=[]
anchor=20
length=0
trees=np.zeros((85,780),dtype="int")


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

            length = randint(3, 10)
            # weighted_choice=[(1,)
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
dist=6
blocks[60:,:]=2

def genTree(x,y,h):

    global trees
    temp=np.zeros((h,3),dtype='int')

    temp[:,1]=7
    temp[h - 1] = 7
    for i in range(randint(1,3)): #Left branch
        temp[randint(2,h-3),0]=8
    for i in range(randint(1,3)): #Right branch
        temp[randint(2,h-3),2]=8
    # print(temp)
    trees[y-h+1:y+1][:,x:x+3]=temp


for i in range(780):

    temp=blocks[:,i]
    anchor=np.where(temp!=0)[0][0]
    if not dist:
        try:
            genTree(i,anchor - 1,randint(5,10))
        except ValueError:
            pass
        dist=randint(7,15)
    else:
        dist-=1
    for j in range(randint(1,3)):
        if randint(0,1):
            try:
                temp[anchor+randint(30,84)]=6
            except IndexError:
                continue
    for k in range(randint(5,10)):
        try:
            temp[anchor+randint(5,35)]=2
            temp[anchor+randint(30,60)]=6
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

with open('trees.pickle', 'wb') as f:
    pickle.dump(trees, f)




# for i in blocks():

