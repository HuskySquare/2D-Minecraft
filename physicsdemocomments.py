# ----- Pre-Program Initialization and Imports

# Modules to import:
from pygame import *  # to use graphics
from random import *  # to have random world gen
import numpy as np  # to use numpy arrays

# Initialize pygame to use video system
init()

# Create a clock object to handle framerate
clock = time.Clock()

# ----- Game Objects

# The air block class
class Air:  # standard object, no inheritance

    # Method to initialize the object
    def __init__(self, x, y, w, h):

        """ Initializes the air block object. """

        # Initial attributes
        self.rect = Rect(x, y, w, h)  # rect attribute (collision box)
        self.around = False  # boolean for player detection (read player class)

    # Method to update the object's appearance and other attributes
    def update(self):

        """ Draws the air block onto the screen and updates it attributes. """

        # Draw the block on the screen (white if around player, else blue)
        draw.rect(screen, ((255, 255, 255) if self.around else (25, 25, 185)), self.rect)

        # Reset block's around status to default
        self.around = False

# The normal block class
class Block:

    # Method to initialize the object
    def __init__(self, x, y, w, h):

        """ Initializes the air block object. """

        # Initial attributes
        self.rect = Rect(x, y, w, h)  # rect attribute (collision box)
        self.around = False  # boolean for player detection (read player class)

        # Method to update the object's appearance and other attributes

    # Method to update the object's appearance and other attributes
    def update(self):
        """ Draws the air block onto the screen and updates it attributes. """

        # Draw the block on the screen (white if around player, else blue)
        draw.rect(screen, ((155, 155, 155) if self.around else (50, 255, 150)), self.rect)

        # Reset block's around status to default
        self.around = False

# The player class
class Player:

    # Method to initialize the object
    def __init__(self, x, y, w, h, controls):

        """ Initializes the player. """

        # Collision attributes
        self.rect = Rect(x, y, w, h)  # rect (collision box)

        # Movement attributes
        self.vx = 0  # velocity in x-direction
        self.vy = 0  # velocity in y-direction

        # Controls attribute
        self.controls = controls

        # Boolean to check if player is standing (can jump)
        self.standing = False

        # List to hold surrounding blocks (blocks around player)
        self.surrounding_blocks = []
    
    # Method to control player movement
    def control(self):
        
        """ Handles player control input. """
        
        # Check to see which directions the player wants to go
        if key.get_pressed()[self.controls[0]]:  # if player hit left
            self.vx = -8  # x-velocity is 8px left / frame
        if key.get_pressed()[self.controls[1]]:  # if player hit right
            self.vx = 8  # x-velocity is 8px right / frame
        if key.get_pressed()[self.controls[2]] and self.standing:  # if player hits up and is standing
            self.vy = -23  # y-velocity is 23px up / frame (initially)
        
        # Player is initially not standing every frame (must prove to be standing in later code)
        self.standing = False
    
    # Method to detect collision with surrounding blocks
    def detect(self):

        """ Detects potential blocks in collision path. """

        # List to hold blocks surrounding the player
        self.surrounding_blocks = []  # initially empty, will be filled later

        # For loop to check blocks surrounding the player
        for shift in surrounding_shifts:  # for every shift in  player position towards a block

            # Attempt to add blocks around player into the surround list
            try:  # run code knowing errors are possible

                # Add the current block to the surround list
                self.surrounding_blocks.append(gameWorld[self.rect.centery // self.rect.h + shift[1],
                                                         self.rect.centerx // self.rect.w + shift[0]])
            # Catch any potential IndexErrors (reaching too far out of array)
            except IndexError:  # if IndexError is raised

                # Nothing happens; carry on as normal (don't add the block)
                pass

        # After this, the surround list is now full

        # For loop to update surrounding blocks' around attribute
        for block in self.surrounding_blocks:  # for every block in the surround list

            # Set the block's around attribute to True (block is surrounding player)
            block.around = True

        # Run the collision code with all of these blocks
        self.collide(self.surrounding_blocks)

    # Method to handle collision with blocks
    def collide(self, blocks):

        """ Handles collision with surrounding blocks. """

        # Move the player in the y-direction
        self.rect.y += self.vy

        # For loop to run through blocks in surrounding
        for block in blocks:  # for every block in the block list

            # Check to see if the block is a real block and if the player is touching the block
            if type(block) is Block and self.rect.colliderect(block.rect):

                # If the block is a real block and is touching player, run the following code

                # Check to see if the player was moving downwards
                if self.vy > 0:  # if player was moving downwards

                    # The bottom of the player is now on the top of the block
                    self.rect.bottom = block.rect.top

                    # The player is now standing on a block
                    self.standing = True

                # Check to see if the player was moving upwards
                elif self.vy < 0:  # if player was moving upwards

                    # The top of the player is now aligned with the bottom of the block
                    self.rect.top = block.rect.bottom

                # Player stops moving in the y-direction
                self.vy = 0

        # Move the player in the x-direction
        self.rect.centerx = (self.rect.centerx + self.vx) % screenSize[0]

        # For loop to run through blocks in surrounding
        for block in blocks:  # for every block in the block list

            # Check to see if the block is a real block and if the player is touching the block
            if type(block) is Block and self.rect.colliderect(block.rect):

                # If the block is a real block and is touching player, run the following code

                # Check to see if the player was moving right
                if self.vx > 0:  # if player was moving right

                    # The right side of the player is now aligned with the left of the block
                    self.rect.right = block.rect.left

                # Check to see if the player was moving left
                elif self.vx < 0:  # if player was moving left

                    # The left side of the player is now aligned with the right of the block
                    self.rect.left = block.rect.right

        # Reset velocity variables
        self.vx = 0  # player temporarily stops moving along x-axis
        self.vy += 2 if self.vy + 1 < self.rect.h else 0  # gravity is applied to y-direction

    # Method to update the object's appearance and other attributes
    def update(self):

        # Draw the player onscreen
        draw.rect(screen, (255, 0, 0), self.rect)


# ----- Game Functions

# Make a function that generates the world of blocks for the player
def make_world(rows, columns):  # defined as 'make_world'

    """ Creates the world for the game. """

    # Empty list to hold blocks
    world_list = []

    # Nested for loop to generate the world

    # Outer loop (handles rows)
    for y in range(rows):  # for every row of blocks in the world

        # Empty list to hold blocks in the current row
        row_list = []

        # Inner loop (handles individual blocks)
        for x in range(columns):  # for every column of blocks in the world

            # Check to see what the RNG thinks
            if randrange(rows - len(world_list)):  # if the number generated by the function is not 0 (chance increases over time)

                # Append an Air block to the current row
                row_list.append(Air(b_width * x, b_height * y, b_width, b_height))

            else:  # if the number is 0 (chance increases over time)

                # Append a normal Block to the current row
                row_list.append(Block(b_width * x, b_height * y, b_width, b_height))

        # After the row is filled, append the row to the world list
        world_list.append(row_list)

    # Convert the 2D list world into a numpy 2-axial array
    world_array = np.array(world_list)

    # Return the world array
    return world_array

# ~~~~~ INFO ON NUMPY ARRAYS

# Numpy arrays are similar to 2D Python lists with the following differences:
# - Are fully dimensional, unlike Python lists, which uses lists inside lists to become dimensional
# - Dimensions in arrays are called 'axes' (singular 'axis')
# - Are much faster than python lists
# - Use 'tuples' of information to represent 'coordinates', while lists use 'indices' to represent 'locations'

# Since numpy arrays are so much faster than lists, we use them to store the world

# ----- Program Component Declarations

# Set the window display caption
display.set_caption("New Physics Idea!")

# Make the window for the game
screenSize = 960, 540  # screen size 960px x 540px
screen = display.set_mode(screenSize)  # set the mode for the screen (makes it appear)

# Make values to generate the world list and array
complexity = abs(int(input('Complexity level? (Use a positive integer)\n')))  # complexity of world
rows = 9 * complexity  # number of rows in world
columns = 16 * complexity  # number of columns in world

# Set variables for block dimensions
b_width = screenSize[0] // columns  # width of one block
b_height = screenSize[1] // rows  # height of one block

# Make the game world with the gen function
gameWorld = make_world(rows, columns)  # use the row and column number

# Make a single player
player = Player(b_width, b_height, b_width, b_height, [K_a, K_d, K_w, K_s])

# Shifts to detect blocks around player (added the the player's integral position)
surrounding_shifts = [(-1, -1), (0, -1), (1, -1),  # top row
                      (-1, 0), (0, 0), (1, 0),  # middle row
                      (-1, 1), (0, 1), (1, 1)]  # bottom row

# ----- Gameloop

# While loop to run the game
while True:  # keep running until explicitly broken

    # Event loop (collect user input and events)
    for e in event.get():  # for every event in the event queue

        # Check to see if user wanted to quit
        if e.type == QUIT:  # if user clicked the 'X' button at top-right of window

            # Break out of the event loop
            break

    # This else statement only runs if the event loop was NOT broken out of
    else:

        # Nested for loop to draw the world
        for r in range(rows):  # for every row in the world
            for c in range(columns):  # for every column in the world

                # Draw the block at the current coordinates onto the screen
                gameWorld[r, c].update()

        # Handle the player
        player.control()  # movement
        player.detect()  # collision detection
        player.update()  # drawing onto screen

        # Set max framerate to 60 FPS
        clock.tick(60)

        # Update the window caption to display the current FPS
        display.set_caption("New Physics Idea! // FPS - {0:.0f}".format(clock.get_fps()))

        # Update the whole screen display
        display.update()

        # Go back to the beginning of the loop
        continue

    # This void is only accessed if the else block did not run (broken out of event loop)

    # Break out of the gameloop
    break

# ----- Shutdown

# After game ends, shut down all processes
display.quit()  # close the window
exit()  # Close Python
