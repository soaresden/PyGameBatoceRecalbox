# 1 - Import library
import pygame
from pygame.locals import *

#CONFIG
VERSION = '1.15'
# CONSTANTS
WHITE = 255, 255, 255
BLACK = 0, 0, 0
MATTE_BLACK = 20, 20, 20
GREEN = 40, 175, 99
RED = 255, 0, 0
YELLOW = 250, 237, 39
DARK_GREEN = 0, 128, 0
LIGHT_BLUE = 0, 191, 255
GREY = 204, 204, 204
BLUE = 33, 150, 243
BACKGROUND = 174, 222, 203
WORLD_SHIFT_SPEED_PERCENT = 0.00135

FONT_EQUINOX = "fonts/font-EquinoxRg.ttf"
FONT_VAG = "fonts/font-vagRounded-BT-Normal.ttf"
FONT_LIGHT = "fonts/font-OpenSans-Light.ttf"
FONT_REG= "fonts/OpenSans-Regular.ttf"
FONT_SEMIBOLD = "fonts/OpenSans-SemiBold.ttf"

SFX_BACK = "sounds/sfx/back.wav"
SFX_OK = "sounds/sfx/ok.wav"
SFX_SELECTION = "sounds/sfx/selection.wav"


CONFIG_FILE = 'config.json'
config = {'DEBUG': False, 'menu_sound': True, 'background_music': True, 'show_fps': False, 'show_score': True,
          'high_scores': [0, 0, 0, 0, 0, 0, 0, 0, 0]}
music_playing = False
delta_time = 0


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

# 3.1 - Load audio
pygame.mixer.music.load("sounds/music/001 Video Game Music Mix Session 1.ogg")
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(0.25)

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