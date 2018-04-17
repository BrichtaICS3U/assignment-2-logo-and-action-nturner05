            # ICS3U
# Assignment 2: Logo
# <Noah Turner>

# adapted from http://www.101computing.net/getting-started-with-pygame/

# Import the pygame library and initialise the game engine
import pygame
pygame.init()
import math
# Define some colours
# Colours are defined using RGB values
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (43, 114, 229)

class Logo(pygame.sprite.Sprite):

    def __init__(self, width, height, speed):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.width=width
        self.height=height
        self.speed = speed
    def __init__(self, width, height, speed):
        super().__init__()
# Set the screen size (please don't change this)
SCREENWIDTH = 400
SCREENHEIGHT = 400

# Open a new window
# The window is defined as (width, height), measured in pixels
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Logo")

# This loop will continue until the user exits the game
carryOn = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

#---------Main Program Loop----------
while carryOn:
    # --- Main event loop ---
    for event in pygame.event.get(): # Player did something
        if event.type == pygame.QUIT: # Player clicked close button
            carryOn = False

    # --- Game logic goes here
    # There should be none for a static image
    
    # --- Draw code goes here

    # Clear the screen to white
    screen.fill(WHITE)

    # Queue different shapes and lines to be drawn
    pygame.draw.ellipse(screen, BLACK, [80, 80, 250, 250], 2)
    pygame.draw.ellipse(screen, BLACK, [90, 90, 230, 230], 0)
    pygame.draw.ellipse(screen, WHITE, [130, 130, 150, 150], 0)
    pygame.draw.arc(screen, BLUE, [130, 130, 150, 150], math.radians(90), math.radians(180), 75)
    pygame.draw.arc(screen, BLUE, [130, 130, 150, 150], math.radians(270), math.radians(0), 75)

    # Update the screen with queued shapes
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Once the main program loop is exited, stop the game engine
pygame.quit()
