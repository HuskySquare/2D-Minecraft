"""
sprite3.py
~~~~~~~~~~
This example demonstrates simple sprite animation without using any "fancy" techniques.

"""
from pygame import *

screen = display.set_mode((800,600))

def moveMario():
    ''' moveMario controls the location of Mario as well as adjusts the move and frame
        variables to ensure the right picture is drawn.
    '''
    global move, frame, marioX, marioY
    keys = key.get_pressed()

    newMove = -1        
    if keys[K_RIGHT]:
        newMove = RIGHT
        marioX += 2
    elif keys[K_DOWN]:
        newMove = DOWN
        marioY += 2
    elif keys[K_UP]:
        newMove = UP
        marioY -= 2
    elif keys[K_LEFT]:
        newMove = LEFT
        marioX -= 2
    else:
        frame = 0

    if move == newMove:     # 0 is a standing pose, so we want to skip over it when we are moving
        frame = frame + 0.2 # adding 0.2 allows us to slow down the animation
        if frame >= len(pics[move]):
            frame = 1
    elif newMove != -1:     # a move was selected
        move = newMove      # make that our current move
        frame = 1

def makeMove(name,start,end):
    ''' This returns a list of pictures. They must be in the folder "name"
        and start with the name "name".
        start, end - The range of picture numbers 
    '''
    move = []
    for i in range(start,end+1):
        move.append(image.load("%s/%s%03d.png" % (name,name,i)))
    return move


def drawScene():
    screen.fill((200,222,255))
    pic = pics[move][int(frame)]
    screen.blit(pic,(marioX-pic.get_width()//2,marioY-pic.get_height()//2))            
    display.flip()


RIGHT = 0 # These are just the indicies of the moves
DOWN = 1  
UP = 2
LEFT = 3

pics = []
pics.append(makeMove("Mario",1,6))      # RIGHT
pics.append(makeMove("Mario",7,12))     # DOWN
pics.append(makeMove("Mario",13,18))    # UP
pics.append(makeMove("Mario",19,24))    # LEFT

frame=0     # current frame within the move
move=0      # current move being performed
marioX, marioY = 400,300

running = True
myClock = time.Clock()

while running:
    for evnt in event.get():
        if evnt.type == QUIT:
            running = False
        
    moveMario()          
    drawScene()
    myClock.tick(50)
    
quit()
