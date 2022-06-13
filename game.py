from tkinter import N
import pygame, os, sys
from objects import *

# constants
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
SEC = 1000 # 1000 milliseconds

pygame.init() # start pygame

# Window setup
WIDTH, HEIGHT = 900, 500 #subject to change
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
WIN.fill(WHITE)
pygame.display.set_caption("Power Outage")

#---------Home Screen Startup control logic and night passing logic---------- Temporarily commented out
# def night_select():
#     f = open("night.txt", mode = 'r')
#     night = f.read(1)
#     if(night == '1'): 
#         return 'PO_night1.PNG'
#     if(night == '2'):
#         return 'PO_night2.PNG'
#     if(night == '3'):
#         return 'PO_night3.PNG'
#     if(night == '4'):
#         return 'PO_night4.PNG'
#     if(night == '5'):
#         return 'PO_night5.PNG'
#     if(night == '6'):
#         return 'PO_night6.PNG'
#     if(night == '7'):
#         return 'PO_night7.PNG'
#     f.close()
#------------Night getter(as a char)----------------
# def get_night():
#     f = open("night.txt", mode = 'r')
#     night = f.read(1)
#     f.close()
#     return night
#------------Night setter(as a char)----------------
# def set_night(newnight):
#     f = open("night.txt", mode = 'r+')
#     f.truncate(0)
#     f.write(newnight)
#     f.close()

# calculates the window's jiggletime based on the inputed night
def get_jiggletime():
    if(night == '1'): return 90 + random.randrange(0,30,1) #attacked once but only once
    elif(night == '2'): return 70 + random.randrange(0,30,1) #attacked once or twice but more likely once
    elif(night == '3'): return 55 + random.randrange(0,20,1) #attacked twice but only twice
    elif(night == '4'): return 45 + random.randrange(0,15,1) #attacked twice or 3 times but likely twice
    elif(night == '5'): return 35 + random.randrange(0,10,1) #attacked three or four times
    elif(night == '6'): return 25 + random.randrange(0,5,1) #attacked four or five times
    elif(night == '7'): return 15 + random.randrange(0,5,1) #attacked seven to nine times

# function that ensures all of the game's state variables are set to their default values, called at the start of every night
def initialize_night():
    # Fireplace vars
    global fire
    global damper

    # Window vars
    global window_phase
    global jiggle_time
    global jiggle_timer

    # Door vars
    global door_phase

    # Bunker vars
    global holding

    # Time vars
    global next_second
    global num_seconds

    # time
    next_second = SEC # next upcoming second in the night (starts at 1)
    num_seconds = 0 # number of seconds that have passed since the current night started

    # Fireplace
    fire = False
    damper = False #False is open damper, True is closed

    # Window
    window_phase = 1
    jiggle_time = get_jiggletime() # the window's jiggle time for this night
    jiggle_timer = jiggle_time

    # Door
    door_phase = 1

    # Bunker
    holding = False 

# --------initialization nation--------
# Objects and backgrounds
# home_night = night_select() # - commented out for now
HOME_image = pygame.image.load(os.path.join('assets', 'PO_night1.PNG')).convert() #adding image ****this line will be changed, PO_night1.PNG will actually be night_select()****
HOME = pygame.transform.scale(HOME_image, (WIDTH, HEIGHT)) #image resizing

LOAD_image = pygame.image.load(os.path.join('assets', 'dummy.jpg')).convert() #adding temp loading image
LOAD = pygame.transform.scale(LOAD_image, (WIDTH, HEIGHT)) # resizing temp load image

PAUSE_MENU = pygame.image.load(os.path.join('assets', 'Pause_Menu.png')).convert_alpha()

FIREPLACE_unlit_open_image = pygame.image.load(os.path.join('assets', 'PO_Fireplace_unlit_open_beta.PNG')).convert() #adding image
FIREPLACE_unlit_open = pygame.transform.scale(FIREPLACE_unlit_open_image, (WIDTH, HEIGHT)) #image resizing
FIREPLACE_unlit_closed_image = pygame.image.load(os.path.join('assets', 'PO_Fireplace_unlit_closed_beta.PNG')).convert() #adding image
FIREPLACE_unlit_closed = pygame.transform.scale(FIREPLACE_unlit_closed_image, (WIDTH, HEIGHT)) #image resizing
FIREPLACE_lit_open_image = pygame.image.load(os.path.join('assets', 'PO_Fireplace_lit_open_beta.PNG')).convert() #adding image
FIREPLACE_lit_open = pygame.transform.scale(FIREPLACE_lit_open_image, (WIDTH, HEIGHT)) #image resizing-----------------------------------------------------------

BUNKER_image = pygame.image.load(os.path.join('assets', 'PO_bunker_beta.PNG')).convert() #adding image
BUNKER = pygame.transform.scale(BUNKER_image, (WIDTH, HEIGHT)) #image resizing
BUNKER_held_image = pygame.image.load(os.path.join('assets', 'PO_bunker_held_beta.PNG')).convert() #adding image
BUNKER_held = pygame.transform.scale(BUNKER_held_image, (WIDTH, HEIGHT)) #image resizing

DOOR_image = pygame.image.load(os.path.join('assets', 'PO_door_beta.PNG')).convert() #adding image
DOOR = pygame.transform.scale(DOOR_image, (WIDTH, HEIGHT)) #image resizing
DOOR_locked1_image = pygame.image.load(os.path.join('assets', 'PO_door_locked1_beta.PNG')).convert() #adding image
DOOR_locked1 = pygame.transform.scale(DOOR_locked1_image, (WIDTH, HEIGHT)) #image resizing
DOOR_locked2_image = pygame.image.load(os.path.join('assets', 'PO_door_locked2_beta.PNG')).convert() #adding image
DOOR_locked2 = pygame.transform.scale(DOOR_locked2_image, (WIDTH, HEIGHT)) #image resizing
DOOR_locked3_image = pygame.image.load(os.path.join('assets', 'PO_door_locked3_beta.PNG')).convert() #adding image
DOOR_locked3 = pygame.transform.scale(DOOR_locked3_image, (WIDTH, HEIGHT)) #image resizing
DOOR_locked4_image = pygame.image.load(os.path.join('assets', 'PO_door_locked4_beta.PNG')).convert() #adding image
DOOR_locked4 = pygame.transform.scale(DOOR_locked4_image, (WIDTH, HEIGHT)) #image resizing
DOOR_unlocked_image = pygame.image.load(os.path.join('assets', 'PO_door_unlocked_beta.PNG')).convert() #adding image
DOOR_unlocked = pygame.transform.scale(DOOR_unlocked_image, (WIDTH, HEIGHT)) #image resizing

WINDOW_locked1_image = pygame.image.load(os.path.join('assets', 'PO_window_locked1_beta.PNG')).convert() #adding image
WINDOW_locked1 = pygame.transform.scale(WINDOW_locked1_image, (WIDTH, HEIGHT)) #image resizing
WINDOW_locked2_image = pygame.image.load(os.path.join('assets', 'PO_window_locked2_beta.PNG')).convert() #adding image
WINDOW_locked2 = pygame.transform.scale(WINDOW_locked2_image, (WIDTH, HEIGHT)) #image resizing
WINDOW_locked3_image = pygame.image.load(os.path.join('assets', 'PO_window_locked3_beta.PNG')).convert() #adding image
WINDOW_locked3 = pygame.transform.scale(WINDOW_locked3_image, (WIDTH, HEIGHT)) #image resizing
WINDOW_unlocked_image = pygame.image.load(os.path.join('assets', 'PO_window_unlocked_beta.PNG')).convert() #adding image
WINDOW_unlocked = pygame.transform.scale(WINDOW_unlocked_image, (WIDTH, HEIGHT)) #image resizing

# Pygame stuff
view = "Home"
FPS = 60

# initialize first night
night = '1' # ****night_select() when code is adjusted for night control/progress saving****
initialize_night()

playing = False
paused = False
# -------------------------------------

#----------------Image Drawing/View control-----------------
def draw_image():
    if(view == "Home"):
        WIN.blit(HOME, (0, 0)) #display home image
    
    elif(view == "Game-load"):
        # here we add an if statement that checks what night we are loading into
        WIN.blit(LOAD, (0, 0)) # temporary

    elif view == "Fireplace":
        # if statements that look at the fireplace's state and determine what image to show
        if damper and not fire: WIN.blit(FIREPLACE_unlit_closed, (0,0)) #display unlit closed damper fireplace
        elif not damper and not fire: WIN.blit(FIREPLACE_unlit_open, (0,0)) #display unlit open damper fireplace
        else: WIN.blit(FIREPLACE_lit_open, (0,0)) #display lit open damper fireplace
        
    elif(view == "Window"):
        # here we add if statements that looks at the window's state and determines what image to show
        if window_phase == 1: WIN.blit(WINDOW_locked1, (0, 0)) #display fully locked window phase (phase = 1)
        elif window_phase == 2: WIN.blit(WINDOW_locked2, (0,0)) #display second phase locked window (phase = 2)
        elif window_phase == 3: WIN.blit(WINDOW_locked3, (0,0)) #display third phase locked window (phase = 3)
        elif window_phase == 4: WIN.blit(WINDOW_unlocked, (0,0)) #display window unlocked (phase = 4)

    elif view == "Door": WIN.blit(DOOR, (0,0)) #display Frontdoor image

    elif view == 'Door-lock': 
        if door_phase == 1:  WIN.blit(DOOR_locked1, (0,0)) #display fully locked door phase (phase = 1)
        elif door_phase == 2: WIN.blit(DOOR_locked2, (0,0)) #display second phase locked door (phase = 2)
        elif door_phase == 3: WIN.blit(DOOR_locked3, (0,0)) #display third phase locked door (phase = 3)
        elif door_phase == 4: WIN.blit(DOOR_locked4, (0,0)) #display Fourth phase locked door (phase = 4)
        elif door_phase == 5: WIN.blit(DOOR_unlocked, (0,0)) #display unlocked door (phase = 5)
    
    elif(view == "Bunker"):
        if not holding: WIN.blit(BUNKER, (0,0)) #display Bunker image
        else: WIN.blit(BUNKER_held, (0,0)) #display bunker held closed image

    if paused:
        WIN.blit(PAUSE_MENU, (325, 125))
    
    pygame.display.update()

def main():
    global view

    global playing
    global paused

    # Fireplace vars
    global fire
    global damper

    # Window vars
    global window_phase
    global jiggle_time
    global jiggle_timer

    # Door vars
    global door_phase

    # Bunker vars
    global holding

    # Time vars
    global next_second
    global num_seconds
    
    clock = pygame.time.Clock()

    # clicking initialization
    clicking = False
    right_clicking = False
    
    #Rect object initialization
    START_BUTTON = pygame.Rect((378, 46), (402, 414))
    LOG = pygame.Rect((343, 157), (92, 18))
    DAMPER = pygame.Rect((325, 125), (10, 24))
    FP_RIGHT = pygame.Rect((831, 33), (44, 404))
    FP_LEFT = pygame.Rect((17, 31), (40, 408))
    FP_DOWN = pygame.Rect((113, 435), (674, 48))
    WI_LEFT = pygame.Rect((19,27), (62,460))
    WI_LOCK = pygame.Rect((489, 207), (68, 22))
    DOOR = pygame.Rect((166, 28), (352, 454))
    DO_RIGHT = pygame.Rect((786, 28), (80, 458))
    BUNKER = pygame.Rect((112,34), (642, 312))
    BU_DOWN = pygame.Rect((112,422), (644,43))

    # stuff that happens while the game is running
    while True:
        clock.tick(FPS)

        mx, my = pygame.mouse.get_pos() # gets mouse's x and y coordinates
        loc = [mx, my] # mouse location

        # ----------View/Click Controls------------
        if view == "Home" and clicking and START_BUTTON.collidepoint(loc[0],loc[1]):
            view = "Game-load"

        elif view == "Game-load":
            pygame.time.delay(3000)

            # -----timing stuff-----
            start_time = pygame.time.get_ticks() # number of ms since pygame.init() was called

            sec_timer = pygame.USEREVENT + 0 # event that appears on the event queue once per second, used for timing
            pygame.time.set_timer(sec_timer, 1000)
            # ----------------------

            playing = True
            view = 'Fireplace'
        
        elif view == "Fireplace" and clicking:
            if(LOG.collidepoint(loc[0],loc[1])):
                if fire: fire = False
                elif not damper == False:  #must add message to let the player know the damper must be open to turn on fire
                    fire = True
            elif (DAMPER.collidepoint(loc[0],loc[1])):
                if not fire:
                    if damper: damper = False
                    else: damper = True
            elif(FP_RIGHT.collidepoint(loc[0], loc[1])): #these next three sections need lots of control logic once the game functionality begins getting coded, this is just for movement control
                view = 'Window'
            elif(FP_LEFT.collidepoint(loc[0], loc[1])): view = "Door"
            elif(FP_DOWN.collidepoint(loc[0], loc[1])): view = "Bunker"

        elif view == "Window" and clicking:
            if(WI_LEFT.collidepoint(loc[0], loc[1])): #this section needs control logic based on what view the fireplace screen should be
                view = "Fireplace"
            elif(WI_LOCK.collidepoint(loc[0], loc[1])):
                if(window_phase == 2): window_phase = 1
                elif(window_phase == 3): window_phase = 2
                elif(window_phase == 4): #unlocked
                    print('you\'re fucked, buddy')
                    #play error audiobite, as in you're already fucking and will be jumpscared within 5 seconds
        
        elif view == "Door" and clicking:
            if(DOOR.collidepoint(loc[0], loc[1])): view = 'Door-lock'
            elif(DO_RIGHT.collidepoint(loc[0], loc[1])):
                view = "Fireplace" #Again needs control logic based on what the fireplace state is ******good example********

        elif view == "Door-lock":
            if right_clicking: view = "Door"
            elif(clicking and not(door_phase == 5)): #can relock door fully with click unless fully unlocked
                door_phase = 1

        elif view == "Bunker" and clicking:
            if(BUNKER.collidepoint(loc[0], loc[1])):
                if holding: holding = False
                else: holding = True
            elif(BU_DOWN.collidepoint(loc[0], loc[1])):
                if not holding: view = "Fireplace"
        # -----------------------------------------

        # -----------Timing System/Game------------
        if playing:
            # ticks = pygame.time.get_ticks() # number of ticks since pygame.init()

            # if ticks - start_time > next_second:
            #     print(jiggle_timer)
            #     next_second += SEC
            #     num_seconds += 1
            #     # print(num_seconds) # **temp commented out to test for hitbox barriers**

            #     jiggle_timer -= 1

            #     if(jiggle_timer == 0):
            #         window_phase += 1
            #         jiggle_timer = jiggle_time
            pass
            
        # -----------------------------------------

        # ---------------Pause---------------------
        if paused:
            print('paused')
        # -----------------------------------------

        clicking = False # one click allowed per frame - probably a temporary solution
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # left clicking
                    clicking = True
                if event.button == 3: # right clicking
                    right_clicking = True
            
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    clicking = False
                if event.button == 3:
                    right_clicking = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if playing != paused: # can only pause/unpause game after entering
                        playing = not playing
                        paused = not paused

            if playing: # all events that we only want to process while the game is being played (aka not paused)
                if event.type == sec_timer: 
                    # anything in here will occur once for every second of playtime
                    print('jiggle_timer:', jiggle_timer)
                    num_seconds += 1
                    jiggle_timer -= 1
            
        draw_image() # update image every every event has been iterated through

if __name__ == "__main__":
    main()
