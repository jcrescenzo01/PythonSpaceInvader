import pygame

# Creating game window

# Initializing Pygame
pygame.init()   # needed otherwise pygame code wont work!

# Creating the Screen
screen = pygame.display.set_mode((800, 600))    # created our screen
    # need second set of parenthesis because it takes a tuple!
    # 800Wx600H screen size
    # 0,0 is actually at the TOP RIGHT CORNER! not the middle like in turtle

# Caption and Icon
pygame.display.set_caption("Space Invaders")    # sets the caption for the display to Space Invaders
icon = pygame.image.load('ufo.png')     # taking ufo.png and making a variable representing it
pygame.display.set_icon(icon)       # sets the icon of the display to variable icon's png

# Player
playerImg = pygame.image.load('spaceship.png')
playerX = 370       # half of the width just about - considering image size is why its not 400 exactly!
playerY = 480       # trying to be close to bottem

def player():
    screen.blit(playerImg,(playerX, playerY))   # blit means "to draw", essentially, take image of player to screen


# Game Loop
# events are anything happening inside of the game window, pressing arrow keys, moving mouse, close button, etc etc
running = True      # made so we can manipulate the while loop
while running:     # infinite loop so it stays open, but it will hang if theres no quit functionality!

    screen.fill((0, 0, 0))  # fills the screen bg with an RGB value, but it doesnt work until update
                            # should be before everything

    for event in pygame.event.get():     # for every event in all of the events happening in the game window
        if event.type == pygame.QUIT:     # if we have quit, running equals false and the loop ends
            running = False                 # now we have quit functionality

    # anything you want to appear continuously goes inside while loop!


    player()    # called after screen.fill since we want player on top of screen, opposite would draw it underneath
    pygame.display.update()     # updates the display with the new code, this lets it change - leaving it black for now though

