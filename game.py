from tkinter import N
import pygame, os, sys
from objects import *
from dataclasses import dataclass

# constants
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
SEC = 1000 # 1000 milliseconds
FPS = 60

pygame.init() # start pygame

# Window setup
WIDTH, HEIGHT = 900, 500 #subject to change
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
WIN.fill(WHITE)
pygame.display.set_caption("Power Outage")

# Objects and backgrounds
# home_night = night_select() # - commented out for now
HOME_image = pygame.image.load(os.path.join('assets', 'PO_night1.PNG')).convert() #adding image ****this line will be changed, PO_night1.PNG will actually be night_select()****
HOME = pygame.transform.scale(HOME_image, (WIDTH, HEIGHT)) #image resizing

LOAD_image = pygame.image.load(os.path.join('assets', 'dummy.jpg')).convert() #adding temp loading image
LOAD = pygame.transform.scale(LOAD_image, (WIDTH, HEIGHT)) # resizing temp load image

PAUSE_MENU = pygame.image.load(os.path.join('assets', 'PO_pause_menu_beta.png')).convert_alpha()

FIREPLACE_unlit_open_image = pygame.image.load(os.path.join('assets', 'PO_fireplace_unlit_open_beta.PNG')).convert() #adding image
FIREPLACE_unlit_open = pygame.transform.scale(FIREPLACE_unlit_open_image, (WIDTH, HEIGHT)) #image resizing
FIREPLACE_unlit_closed_image = pygame.image.load(os.path.join('assets', 'PO_fireplace_unlit_closed_beta.PNG')).convert() #adding image
FIREPLACE_unlit_closed = pygame.transform.scale(FIREPLACE_unlit_closed_image, (WIDTH, HEIGHT)) #image resizing
FIREPLACE_lit_open_image = pygame.image.load(os.path.join('assets', 'PO_fireplace_lit_open_beta.PNG')).convert() #adding image
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
WINDOW_unlocked = pygame.transform.scale(WINDOW_unlocked_image, (WIDTH, HEIGHT)) #image resizingg

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

# fucntion that handles clicks based off the current game states and mouse position
def handle_clicks(states: States, rects: dict, clicking: bool, right_clicking: bool, loc: tuple):
    if states.view == "Home" and clicking and rects['START_BUTTON'].collidepoint(loc[0],loc[1]):
            states.view = "Game-load"

    elif states.view == "Game-load":
        pygame.time.delay(3000)

        # -----timing stuff-----
        #start_time = pygame.time.get_ticks() # number of ms since pygame.init() was called
        global sec_timer
        sec_timer = pygame.USEREVENT + 0 # event that appears on the event queue once per second, used for timing
        pygame.time.set_timer(sec_timer, 1000)
        # ----------------------

        states.playing = True
        states.view = 'Fireplace'
        
    if clicking: # handle clicks
        if states.playing: # handle clicks while playing
            if states.view == "Fireplace":
                if rects['LOG'].collidepoint(loc[0],loc[1]):
                    if states.fire: states.fire = False
                    elif not states.damper == False:  #must add message to let the player know the damper must be open to turn on fire
                        states.fire = True
                elif rects['DAMPER'].collidepoint(loc[0],loc[1]):
                    if not states.fire:
                        if states.damper: states.damper = False
                        else: states.damper = True
                elif rects['FP_RIGHT'].collidepoint(loc[0], loc[1]): #these next three sections need lots of control logic once the game functionality begins getting coded, this is just for movement control
                    states.view = 'Window'
                elif rects['FP_LEFT'].collidepoint(loc[0], loc[1]): states.view = "Door"
                elif rects['FP_DOWN'].collidepoint(loc[0], loc[1]): states.view = "Bunker"

            elif states.view == "Window":
                if rects['WI_LEFT'].collidepoint(loc[0], loc[1]): #this section needs control logic based on what view the fireplace screen should be
                    states.view = "Fireplace"
                elif rects['WI_LOCK'].collidepoint(loc[0], loc[1]):
                    if states.window_phase == 2: states.window_phase = 1
                    elif states.window_phase == 3: states.window_phase = 2
                    elif states.window_phase == 4: #unlocked
                        print('you\'re fucked, buddy')
                
            elif states.view == "Door":
                if rects['DOOR'].collidepoint(loc[0], loc[1]): states.view = 'Door-lock'
                elif rects['DO_RIGHT'].collidepoint(loc[0], loc[1]):
                    states.view = "Fireplace" #Again needs control logic based on what the fireplace state is ******good example********

            elif states.view == "Door-lock":
                if not states.door_phase == 5: #can relock door fully with click unless fully unlocked
                    states.door_phase = 1

            elif states.view == "Bunker":
                if rects['BUNKER'].collidepoint(loc[0], loc[1]):
                    if states.holding: states.holding = False
                    else: states.holding = True
                elif rects['BU_DOWN'].collidepoint(loc[0], loc[1]):
                    if not states.holding: states.view = "Fireplace"

        if states.paused: # handle clicks while paused
            pass
        
    if right_clicking: # handle right clicks
        if states.playing: # handle right clicks while playing
            if states.view == "Door-lock": states.view = "Door"
        if states.paused: # handle right clicks while paused
            pass

# function that updates game states as needed
def update_states(states: States):
    if states.jiggle_countdown < 0:
        states.jiggle_countdown = states.jiggle_time
        states.window_phase += 1
    
    if states.window_phase == 4:
        #play error audiobite, as in you're already fucking and will be jumpscared within 5 seconds
        pass

# function that determines which images to display based off current game states
def draw_image(states: States):
    if states.view == "Home":
        WIN.blit(HOME, (0, 0)) #display home image
    
    elif states.view == "Game-load":
        # here we add an if statement that checks what night we are loading into
        WIN.blit(LOAD, (0, 0)) # temporary

    elif states.view == "Fireplace":
        # if statements that look at the fireplace's state and determine what image to show
        if states.damper and not states.fire: WIN.blit(FIREPLACE_unlit_closed, (0,0)) #display unlit closed damper fireplace
        elif not states.damper and not states.fire: WIN.blit(FIREPLACE_unlit_open, (0,0)) #display unlit open damper fireplace
        else: WIN.blit(FIREPLACE_lit_open, (0,0)) #display lit open damper fireplace
        
    elif states.view == "Window":
        # here we add if statements that looks at the window's state and determines what image to show
        if states.window_phase == 1: WIN.blit(WINDOW_locked1, (0, 0)) #display fully locked window phase (phase = 1)
        elif states.window_phase == 2: WIN.blit(WINDOW_locked2, (0,0)) #display second phase locked window (phase = 2)
        elif states.window_phase == 3: WIN.blit(WINDOW_locked3, (0,0)) #display third phase locked window (phase = 3)
        elif states.window_phase == 4: WIN.blit(WINDOW_unlocked, (0,0)) #display window unlocked (phase = 4)

    elif states.view == "Door": WIN.blit(DOOR, (0,0)) #display Frontdoor image

    elif states.view == 'Door-lock': 
        if states.door_phase == 1:  WIN.blit(DOOR_locked1, (0,0)) #display fully locked door phase (phase = 1)
        elif states.door_phase == 2: WIN.blit(DOOR_locked2, (0,0)) #display second phase locked door (phase = 2)
        elif states.door_phase == 3: WIN.blit(DOOR_locked3, (0,0)) #display third phase locked door (phase = 3)
        elif states.door_phase == 4: WIN.blit(DOOR_locked4, (0,0)) #display Fourth phase locked door (phase = 4)
        elif states.door_phase == 5: WIN.blit(DOOR_unlocked, (0,0)) #display unlocked door (phase = 5)
    
    elif states.view == "Bunker":
        if not states.holding: WIN.blit(BUNKER, (0,0)) #display Bunker image
        else: WIN.blit(BUNKER_held, (0,0)) #display bunker held closed image

    if states.paused:
        # note: this part needs to be at the bottom so that the pause menu will overlay everything else
        WIN.blit(PAUSE_MENU, (325, 125))
    
    pygame.display.update()

def main():  
    clock = pygame.time.Clock()

    # clicking initialization
    clicking = False
    right_clicking = False

    states = States() # initialize game states
    
    # Dictionary containing all of the Rect objects to be used in the game
    rects = {
        'START_BUTTON': pygame.Rect((378, 46), (402, 414)),
        'LOG': pygame.Rect((343, 157), (92, 18)),
        'DAMPER': pygame.Rect((325, 125), (10, 24)),
        'FP_RIGHT': pygame.Rect((831, 33), (44, 404)),
        'FP_LEFT': pygame.Rect((17, 31), (40, 408)),
        'FP_DOWN': pygame.Rect((113, 435), (674, 48)),
        'WI_LEFT': pygame.Rect((19,27), (62,460)),
        'WI_LOCK': pygame.Rect((489, 207), (68, 22)),
        'DOOR': pygame.Rect((166, 28), (352, 454)),
        'DO_RIGHT': pygame.Rect((786, 28), (80, 458)),
        'BUNKER': pygame.Rect((112,34), (642, 312)),
        'BU_DOWN': pygame.Rect((112,422), (644,43))
    }

    # stuff that happens while the game is running
    while True:
        clock.tick(FPS)

        loc = pygame.mouse.get_pos() # gets mouse's x and y coordinates

        handle_clicks(states, rects, clicking, right_clicking, loc)
        update_states(states)

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
                    if states.playing != states.paused: # can only pause/unpause game after entering
                        states.playing = not states.playing
                        states.paused = not states.paused

            if states.playing: # all events that we only want to process while the game is being played (aka not paused)
                if event.type == sec_timer: 
                    # anything in here will occur once for every second of playtime
                    print('jiggle_countdown:', states.jiggle_countdown)
                    states.num_seconds += 1
                    states.jiggle_countdown -= 1
            
        draw_image(states) # update image after every event has been iterated through

if __name__ == "__main__":
    main()