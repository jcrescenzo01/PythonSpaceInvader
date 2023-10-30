import pygame  # game creation import
import random  # for enemy placement
import math  # for collision and other stuff
from pygame import mixer    # for handling music / sounds

# Creating game window

# Initializing Pygame
pygame.init()  # needed otherwise pygame code wont work!

# Creating the Screen
screen = pygame.display.set_mode((800, 600))  # created our screen
# need second set of parenthesis because it takes a tuple for screen size
# 800Wx600H screen size
# 0,0 is actually at the TOP RIGHT CORNER! not the middle like in turtle

# Background
background = pygame.image.load('background1.png')  # loads the background but doesnt make it stay
# till we put it in the loop (below screen.fill)

# Background Sound
mixer.music.load('background.wav')  # loads the background music, .music is for longform sound, ie music
mixer.music.play(-1)  # plays music in the mixer, (-1) makes it play on loop rather than just once

# Caption and Icon
pygame.display.set_caption("Space Invaders")  # sets the caption for the display to Space Invaders
icon = pygame.image.load('ufo.png')  # taking ufo.png and making a variable representing it
pygame.display.set_icon(icon)  # sets the icon of the display to variable icon's png

# Player
playerImg = pygame.image.load('spaceship.png')
playerX = 370  # half of the width just about - considering image size is why its not 400 exactly!
playerY = 480  # trying to be close to bottem
playerX_change = 0  # for keyboard input interaction

# Movement Explaination:
# adding / removing pixils is moving an image, related to pixil size of screen
# while loop for continuous movement

# Enemy
## Multiple Enemies
enemyImg = []       # making lists so we can store multiple enemies
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6  # number of enemies we want

for i in range(num_of_enemies):     # want to be able to loop through them
    enemyImg.append(pygame.image.load('enemy1.png'))    # .append because its a list now, was '=' originally
    # enemyX = 370
    # enemyY = 50         # note that 50 is higher on the screen than 480!
    # However, we want the enemy to show up randomly!:
    enemyX.append(random.randint(0, 735))  # will 800 work poorly? Yes, so 735
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(0.3)  # for moving enemy left and right, etc
    enemyY_change.append(40)  # for y axis enemy movment, set to 40 so we can move it down in the loop later

# random note: Ctrl Alt L will format python code in pycharm to a proper style

# Bullet (player)
bulletImg = pygame.image.load('bullet.png')  # don't forget to change the png!
bulletX = 0
bulletY = 480  # since the player is there
bulletX_change = 0  # may not use it, but might as well keep it
bulletY_change = 3  # bullet has a different speed too
bullet_state = "ready"  # ready: You cant see the bullet on the screen

# fire: the bullet is currently moving


# Collision
# we will be calculating the distance between coordinates - bullet-enemy, stuff like that
# calculating coordinate distance is like so:
# D = <SQUARE ROOT OF>|(x_1^2 - x_2^2) + (y_1^2 - y_2^2)|
# distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))


# Score
# score = 0     # originally this, but removed due to needing a different, more functional scoring system, below:
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)     # defining font, access pygame font function,
                                                    # .ttf being the extension for the font, 32 is size
                                                    # freesansbold is a font that comes with pygame, but you can download other fonts
                                                        #extract the zip, put the ttf in your folder, than replace the .ttf above
textX = 10  # x coordinate of where the text will appear, a bit away from the top left
textY = 10  # y coordinate

def show_score(x,y):    # function for displaying the score
    score = font.render("Score: " + str(score_value), True, (255,255,255))   # rendering rather than bliting,
                # render(textToPrint with score type casted to string, True, color of font)
    screen.blit(score,(x,y))    # blit the score to the screen after rendering it

def player(x, y):  # added x,y during movement tutorial
    screen.blit(playerImg, (x, y))  # blit means "to draw", essentially, take image of player to screen


def enemy(x, y, i):  # player remade into an enemy
                    # added i value for multi-enemy for loop
    screen.blit(enemyImg[i], (x, y))    # added [i] for which enemy image we want


def fire_bullet(x, y):  # function for shooting the bullet out of the player
    global bullet_state  # now we can access bullet state from inside function
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))  # draw bullet on screen,
    # the +16 and +10 make sure it appears in the center of the spaceship rather than the left


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:   # trial and testing untill finding propper distance between enemy and bullet to call it a collision
        return True
    else:
        return False


# Game Loop
# events are anything happening inside of the game window, pressing arrow keys, moving mouse, close button, etc etc

running = True  # made so we can manipulate the while loop

while running:  # infinite loop so it stays open, but it will hang if theres no quit functionality!
    # anything you want to appear continuously goes inside while loop!
    screen.fill((0, 0, 0))  # fills the screen bg with an RGB value, but it doesnt work until update
    # should be before everything

    # Background Image
    screen.blit(background, (0, 0))  # draw the background image at these coordinates
    # the while loop now runs slower though, because it needs to load this heavy background over and over
    # each iteration becoming more and more slow, increasing the speed of entities (player, enemy) will
    # deal with this as long as you get every movement type accounted for
    # I actually didnt have this problem, maybe its based on cpu power?

    # playerX+=0.05     # would move the player right, -= would do left. Continuous since its in a loop
    # print(playerX)    # continually increasing in the terminal
    # We want this to be in response to keyboard input though:
    # Any keystroke press is an Event, anything happening in the game window, called a Keystroke Event
    # stored inside pygame.event.get(), see below

    for event in pygame.event.get():  # for every event in all of the events happening in the game window
        if event.type == pygame.QUIT:  # if we have quit, running equals false and the loop ends
            running = False  # now we have quit functionality

        # if keystroke is pressed check whether its right or left:
        if event.type == pygame.KEYDOWN:  # checks if the key is being pressed down, KEYUP would check if its up / releasing
            print("Keystroke Pressed")
            if event.key == pygame.K_LEFT:  # checks if key being pressed is left arrow
                playerX_change = -0.3  # ship goes left, decreasing via playerX_change
                # print("Left arrow is pressed")
            if event.key == pygame.K_RIGHT:  # checks if key being pressed is right arrow
                playerX_change = 0.3  # ship goes right, increasing by playerX_change
                # print("Right arrow is pressed")
            if event.key == pygame.K_SPACE:  # checks if key being pressed is the Space Bar
                if bullet_state == "ready":  # makes sure bullet doesnt teleport to us by requiring the ready state
                    bullet_sound = mixer.Sound(mixer.Sound('laser.wav'))    # loads bullet sound when firing
                    bullet_sound.play()     # plays the bullet sound
                    bulletX = playerX  # to counter bullet following player x coord
                    fire_bullet(bulletX, bulletY)  # calling fire bullet funct when space is pressed
                    # originally playerX but that gets the bullet stuck on our current x location

        if event.type == pygame.KEYUP:
            print("Keystroke Released")
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0  # ship stops on release
                # print("Keystroke has been released")

    # Enemy Movement
    # Left and Right Wall Border Control for Enemy
    # when it hits the border, we want it to go the opposite direction like in space invaders
    # we also want it to go down a bit each time, getting closer
    for i in range(num_of_enemies):     # for multiple enemies, added [i] brackets below to make this function correctly
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.3  # when it hits the left side start increasing the x value and
            # go the other way, note it doesnt set it to 0 since no one is
            # controlling this things movement but the compiler
            enemyY[i] += enemyY_change[i]  # increment ychange to move it down when border is hit
        elif enemyX[i] >= 736:  # 800 would stop at the left edge of the ship, which would look bad
            enemyX_change[i] = -0.3  # same as above
            enemyY[i] += enemyY_change[i]

        # Collision
        # Now moved to multiple enemy for loop for functionality, also [i]'s added!!!
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)  # stores value of true and false in collision
        # now what do we want when collision occurs?
        if collision:  # if collision is true
            explosion_sound = mixer.Sound(mixer.Sound('explosion.wav')) # loads explosion sound on collision with enemy
            explosion_sound.play()  # plays that sound
            bulletY = 480  # reset bullet to its starting point
            bullet_state = "ready"  # change the state since the bullet isn't shown anymore
            score_value += 1  # increase score by 1 each time we hit, score_value change for scoring system
            # now we need to get the enemy to respawn upon being hit, up to the enemy block to take stuff!
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)  # now the enemy will respawn as it should
        enemy(enemyX[i], enemyY[i], i)  # moved to multi enemy for loop, needed i's and also to specify enemy image

    # Bullet Movement
    if bulletY <= 0:  # this if loop will fix the multiple bullet issue (though its still the
        # only bullet on screen at a time)
        bulletY = 480
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)  # playerX changed to bulletX to fix the bullet following
        # player's x coordinate issue
        bulletY -= bulletY_change
        # at this point (there were) 2 problems: bullet follows our x movement, and bullet can only fire once
        # we want the bullet to stay on its original x coord and allow for multiple bullets
        # x coord problem is because of us setting it to the everchanging playerX value originally
        # multiple bullets problem is because the bullet still exists once fired
        # note that, when the bullet goes offscreen, its still there going further negative
        # after fixing all that, now when we press the spacebar and move the bullet teleports
        # to our current x coord
        # we will make it so we can only press SPACE when the bullet_state is in ready condition



    playerX += playerX_change  # applies keyboard input to the ship
    # Left and Right Wall Border Control for Player
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:  # 800 would stop at the left edge of the ship, which would look bad
        playerX = 736

    player(playerX, playerY)  # called after screen.fill since we want player on top of screen,
    # opposite would draw it underneath

    show_score(textX, textY)    # showing the score on the screen added to while loop

    pygame.display.update()  # updates the display with the new code, this lets it change


""" 
    Things I want to add to this
when score increases, at some point, the enemy numbers should increase to make it harder
larger bullets that hit more enemies, spread out, etc
levels? like, maybe a screen transition with a new background, then maybe obstacles to block bullets
    a lot of this will probably revolve around the score of the player I think
Double-tap dodge function, store and switch bullets function
scrolling screen?
"""