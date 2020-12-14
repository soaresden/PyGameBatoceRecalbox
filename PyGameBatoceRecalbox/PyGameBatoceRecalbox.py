# 1 - Import library
import pygame
from pygame.locals import *

# 2 - Initialize the game
pygame.init()
width, height = 1280, 720
screen=pygame.display.set_mode((width, height))
#set the keys
keys = [False, False, False, False]
playerpos=[100,100]

# 3 - Load images
background = pygame.image.load("images/background/back720.png")
pad1 = pygame.image.load("images/icons/pad.png")

# 4 - keep looping through
while 1:
    # 5 - clear the screen before drawing it again
    screen.fill(0)
    # 6 - draw the screen elements
    # drawing the background
    screen.blit(background, (0,0))
    screen.blit(pad1, playerpos)
    # 7 - update the screen
    pygame.display.flip()
    # 8 - loop through the events
    for event in pygame.event.get():
        # check if the event is the X button 
        if event.type == pygame.KEYDOWN:
            if event.key==K_z:
                keys[0]=True
            elif event.key==K_q:
                keys[1]=True
            elif event.key==K_s:
                keys[2]=True
            elif event.key==K_d:
                keys[3]=True
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_z:
                keys[0]=False
            elif event.key==pygame.K_q:
                keys[1]=False
            elif event.key==pygame.K_s:
                keys[2]=False
            elif event.key==pygame.K_d:
                keys[3]=False

        if event.type==pygame.QUIT:
            # if it is quit the game
            pygame.quit() 
            exit(0)

    # 9 - Move player
    if keys[0]:
        playerpos[1]-=5
    elif keys[2]:
        playerpos[1]+=5
    if keys[1]:
        playerpos[0]-=5
    elif keys[3]:
        playerpos[0]+=5