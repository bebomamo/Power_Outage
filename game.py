from tkinter import N
import pygame, os, sys
from objects import *
from dataclasses import dataclass
from pygame import mixer

# constants
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
SEC = 1000 # 1000 milliseconds
FPS = 60

pygame.init() # start pygame
pygame.mixer.init() #start mixer 

# Window setup
WIDTH, HEIGHT = 900, 500 #subject to change
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
WIN.fill(WHITE)
pygame.display.set_caption("Power Outage")

# Objects and backgrounds
# home_night = night_select() # - commented out for now
HOME_IMAGE = pygame.image.load(os.path.join('assets', 'PO_home_alpha.PNG')).convert() #adding image ****this line will be changed, PO_night1.PNG will actually be night_select()****
HOME = pygame.transform.scale(HOME_IMAGE, (WIDTH, HEIGHT)) #image resizing

PAUSE_MENU = pygame.image.load(os.path.join('assets', 'PO_pause_menu_beta.png')).convert_alpha()

NIGHT1_LOAD_IMAGE = pygame.image.load(os.path.join('assets','PO_night1.PNG')).convert()
NIGHT1_LOAD = pygame.transform.scale(NIGHT1_LOAD_IMAGE, (WIDTH, HEIGHT))
NIGHT2_LOAD_IMAGE = pygame.image.load(os.path.join('assets','PO_night2.PNG')).convert()
NIGHT2_LOAD = pygame.transform.scale(NIGHT2_LOAD_IMAGE, (WIDTH, HEIGHT))
NIGHT3_LOAD_IMAGE = pygame.image.load(os.path.join('assets','PO_night3.PNG')).convert()
NIGHT3_LOAD = pygame.transform.scale(NIGHT3_LOAD_IMAGE, (WIDTH, HEIGHT))
NIGHT4_LOAD_IMAGE = pygame.image.load(os.path.join('assets','PO_night4.PNG')).convert()
NIGHT4_LOAD = pygame.transform.scale(NIGHT4_LOAD_IMAGE, (WIDTH, HEIGHT))
NIGHT5_LOAD_IMAGE = pygame.image.load(os.path.join('assets','PO_night5.PNG')).convert()
NIGHT5_LOAD = pygame.transform.scale(NIGHT5_LOAD_IMAGE, (WIDTH, HEIGHT))
NIGHT6_LOAD_IMAGE = pygame.image.load(os.path.join('assets','PO_night6.PNG')).convert()
NIGHT6_LOAD = pygame.transform.scale(NIGHT6_LOAD_IMAGE, (WIDTH, HEIGHT))
NIGHT7_LOAD_IMAGE = pygame.image.load(os.path.join('assets','PO_night7.PNG')).convert()
NIGHT7_LOAD = pygame.transform.scale(NIGHT7_LOAD_IMAGE, (WIDTH, HEIGHT))

FIREPLACE_UNLIT_OPEN_IMAGE = pygame.image.load(os.path.join('assets', 'PO_fireplace_unlit_open_beta.PNG')).convert() #adding image
FIREPLACE_UNLIT_OPEN = pygame.transform.scale(FIREPLACE_UNLIT_OPEN_IMAGE, (WIDTH, HEIGHT)) #image resizing
FIREPLACE_UNLIT_CLOSED_IMAGE = pygame.image.load(os.path.join('assets', 'PO_fireplace_unlit_closed_beta.PNG')).convert() #adding image
FIREPLACE_UNLIT_CLOSED = pygame.transform.scale(FIREPLACE_UNLIT_CLOSED_IMAGE, (WIDTH, HEIGHT)) #image resizing
FIREPLACE_LIT_OPEN_IMAGE = pygame.image.load(os.path.join('assets', 'PO_fireplace_lit_open_beta.PNG')).convert() #adding image
FIREPLACE_LIT_OPEN = pygame.transform.scale(FIREPLACE_LIT_OPEN_IMAGE, (WIDTH, HEIGHT)) #image resizing-----------------------------------------------------------

BUNKER_IMAGE = pygame.image.load(os.path.join('assets', 'PO_bunker_beta.PNG')).convert() #adding image
BUNKER = pygame.transform.scale(BUNKER_IMAGE, (WIDTH, HEIGHT)) #image resizing
BUNKER_HELD_IMAGE = pygame.image.load(os.path.join('assets', 'PO_bunker_held_beta.PNG')).convert() #adding image
BUNKER_HELD = pygame.transform.scale(BUNKER_HELD_IMAGE, (WIDTH, HEIGHT)) #image resizing

DOOR_IMAGE = pygame.image.load(os.path.join('assets', 'PO_door_beta.PNG')).convert() #adding image
DOOR = pygame.transform.scale(DOOR_IMAGE, (WIDTH, HEIGHT)) #image resizing
DOOR_LOCKED1_IMAGE = pygame.image.load(os.path.join('assets', 'PO_door_locked1_beta.PNG')).convert() #adding image
DOOR_LOCKED1 = pygame.transform.scale(DOOR_LOCKED1_IMAGE, (WIDTH, HEIGHT)) #image resizing
DOOR_LOCKED2_IMAGE = pygame.image.load(os.path.join('assets', 'PO_door_locked2_beta.PNG')).convert() #adding image
DOOR_LOCKED2 = pygame.transform.scale(DOOR_LOCKED2_IMAGE, (WIDTH, HEIGHT)) #image resizing
DOOR_LOCKED3_IMAGE = pygame.image.load(os.path.join('assets', 'PO_door_locked3_beta.PNG')).convert() #adding image
DOOR_LOCKED3 = pygame.transform.scale(DOOR_LOCKED3_IMAGE, (WIDTH, HEIGHT)) #image resizing
DOOR_LOCKED4_IMAGE = pygame.image.load(os.path.join('assets', 'PO_door_locked4_beta.PNG')).convert() #adding image
DOOR_LOCKED4 = pygame.transform.scale(DOOR_LOCKED4_IMAGE, (WIDTH, HEIGHT)) #image resizing
DOOR_UNLOCKED_IMAGE = pygame.image.load(os.path.join('assets', 'PO_door_unlocked_beta.PNG')).convert() #adding image
DOOR_UNLOCKED = pygame.transform.scale(DOOR_UNLOCKED_IMAGE, (WIDTH, HEIGHT)) #image resizing

WINDOW_LOCKED1_IMAGE = pygame.image.load(os.path.join('assets', 'PO_window_locked1_beta.PNG')).convert() #adding image
WINDOW_LOCKED1 = pygame.transform.scale(WINDOW_LOCKED1_IMAGE, (WIDTH, HEIGHT)) #image resizing
WINDOW_LOCKED2_IMAGE = pygame.image.load(os.path.join('assets', 'PO_window_locked2_beta.PNG')).convert() #adding image
WINDOW_LOCKED2 = pygame.transform.scale(WINDOW_LOCKED2_IMAGE, (WIDTH, HEIGHT)) #image resizing
WINDOW_LOCKED3_IMAGE = pygame.image.load(os.path.join('assets', 'PO_window_locked3_beta.PNG')).convert() #adding image
WINDOW_LOCKED3 = pygame.transform.scale(WINDOW_LOCKED3_IMAGE, (WIDTH, HEIGHT)) #image resizing
WINDOW_UNLOCKED_IMAGE = pygame.image.load(os.path.join('assets', 'PO_window_unlocked_beta.PNG')).convert() #adding image
WINDOW_UNLOCKED = pygame.transform.scale(WINDOW_UNLOCKED_IMAGE, (WIDTH, HEIGHT)) #image resizing

#Audio asset initialization
#for window
JIGGLE_s = mixer.Sound(os.path.join('assets', 'Jiggle.wav')) #
#for door
LOCK_s = mixer.Sound(os.path.join('assets', 'Lock.wav')) #
#for bunker
BUNKER_HOLD_s = mixer.Sound(os.path.join('assets', 'Bunker_hold.wav')) #
BUNKER_RELEASE_s = mixer.Sound(os.path.join('assets', 'Bunker_release.wav')) #
WALK_TOWARDS_s = mixer.Sound(os.path.join('assets', 'Walk_towards.wav'))
WALK_AWAY_s = mixer.Sound(os.path.join('assets', 'Walk_away.wav'))
#for fireplace
CLIMB_DOWN_s = mixer.Sound(os.path.join('assets', 'Climb_down.wav'))
CLIMB_UP_s = mixer.Sound(os.path.join('assets', 'Climb_up.wav'))
CLOSE_DAMPER_s = mixer.Sound(os.path.join('assets', 'Close_damper.wav')) #
OPEN_DAMPER_s = mixer.Sound(os.path.join('assets', 'Open_damper.wav')) #
FIRE_ON_s = mixer.Sound(os.path.join('assets', 'Fire_on.wav')) #
FIRE_RUNNING_s = mixer.Sound(os.path.join('assets', 'Fire_running.wav')) #
FIRE_OFF_s = mixer.Sound(os.path.join('assets', 'Fire_off.wav')) #
#for fear
BEEPS_s = mixer.Sound(os.path.join('assets', 'New_Recording.wav'))
FEAR_s = mixer.Sound(os.path.join('assets', 'Fear.wav'))


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

#function that updates constant background noise
def update_music(states: States):
    if states.fire and states.music_swap == True:
        mixer.music.stop()
        mixer.music.load(os.path.join('assets', 'Fire_running.wav'))
        mixer.music.play(-1)
        states.music_swap = False
    elif states.music_swap == True:
        mixer.music.stop()
        mixer.music.load(os.path.join('assets', 'Ambient.wav'))
        mixer.music.play(-1)
        states.music_swap = False

# fucntion that handles clicks based off the current game states and mouse position
def handle_clicks(states: States, rects: dict, clicking: bool, right_clicking: bool, loc: tuple):
    if states.view == "Home" and clicking:
        if rects['START_BUTTON'].collidepoint(loc[0],loc[1]): states.view = "Game-load"
        elif rects['QUIT_BUTTON'].collidepoint(loc[0],loc[1]):
            pygame.quit()
            sys.exit()

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
                    if states.fire: 
                        FIRE_OFF_s.play()
                        states.fire = False
                        states.music_swap = True
                    elif not states.damper:  #must add message to let the player know the damper must be open to turn on fire
                        FIRE_ON_s.play()
                        states.fire = True
                        states.music_swap = True
                elif rects['DAMPER'].collidepoint(loc[0],loc[1]):
                    if not states.fire:
                        if states.damper: 
                            states.damper = False
                            OPEN_DAMPER_s.play()
                        else: 
                            states.damper = True
                            CLOSE_DAMPER_s.play()
                            if states.FP_attack:
                                states.FP_countdown = states.FP_time
                                states.FP_attack = False
                                CLIMB_UP_s.play()
                elif rects['FP_RIGHT'].collidepoint(loc[0], loc[1]): #these next three sections need lots of control logic once the game functionality begins getting coded, this is just for movement control
                    states.view = 'Window'
                elif rects['FP_LEFT'].collidepoint(loc[0], loc[1]): states.view = "Door"
                elif rects['FP_DOWN'].collidepoint(loc[0], loc[1]): 
                    states.view = "Bunker"
                    if not states.B_firstattack:
                        states.B_checked = True
                        states.B_CTcountdown = states.B_checkedtime
                    
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
                    states.view = "Fireplace" #Again needs control logic based on what the fireplace state is

            elif states.view == "Door-lock":
                if states.door_phase < 5: #can relock door fully with click unless fully unlocked
                    states.door_phase = 1

            elif states.view == "Bunker":
                if rects['BUNKER'].collidepoint(loc[0], loc[1]):
                    if states.holding: 
                        states.holding = False
                        BUNKER_RELEASE_s.play()
                    else: 
                        states.holding = True
                        BUNKER_HOLD_s.play()
                        if states.B_attack:
                                states.B_countdown = states.B_time
                                states.B_attack = False
                                WALK_AWAY_s.play()
                elif rects['BU_DOWN'].collidepoint(loc[0], loc[1]):
                    if not states.holding: states.view = "Fireplace"

        if states.paused: # handle clicks while paused
            if rects['RESUME_BUTTON'].collidepoint(loc[0],loc[1]):
                states.paused = False
                states.playing = True
            elif rects['QUIT_BUTTON_PAUSED'].collidepoint(loc[0],loc[1]):
                # TODO: should ask the player whether or not they want to save most recent night
                pygame.quit()
                sys.exit()
        
    if right_clicking: # handle right clicks
        if states.playing: # handle right clicks while playing
            if states.view == "Door-lock": states.view = "Door"
        if states.paused: # handle right clicks while paused
            pass

# function that updates game states as needed
def update_states(states: States):
    # Window
    if states.jiggle_countdown < 0:
        states.jiggle_countdown = states.jiggle_time
        states.window_phase += 1
        JIGGLE_s.play()
    
    if states.window_phase == 4:
        #play error audiobite, as in you're already fucking and will be jumpscared within 5 seconds
        pass

    # Door
    if states.lock_countdown < 0:
        states.lock_countdown = states.lock_time
        states.door_phase += 1
        LOCK_s.play()

    # Fireplace
    if states.climbdown_countdown < 0:
        states.climbdown_countdown = states.climbdown_time
        if not states.damper:
            CLIMB_DOWN_s.play()
            states.FP_attack = True

    if states.FP_countdown < 0:
        pass

    # Bunker
    if states.bunkerwalk_countdown < 0:
        states.bunkerwalk_countdown = states.bunkerwalk_time / 4
        WALK_TOWARDS_s.play()
        states.B_attack = True
        states.B_firstattack = True

        


# function that determines which images to display based off current game states
def draw_image(states: States):
    if states.view == "Home":
        WIN.blit(HOME, (0, 0)) #display home image
    
    elif states.view == "Game-load":
        if states.night == '1': WIN.blit(NIGHT1_LOAD, (0,0))
        elif states.night == '2': WIN.blit(NIGHT2_LOAD, (0,0))
        elif states.night == '3': WIN.blit(NIGHT3_LOAD, (0,0))
        elif states.night == '4': WIN.blit(NIGHT4_LOAD, (0,0))
        elif states.night == '5': WIN.blit(NIGHT5_LOAD, (0,0))
        elif states.night == '6': WIN.blit(NIGHT6_LOAD, (0,0))
        elif states.night == '7': WIN.blit(NIGHT7_LOAD, (0,0))

    elif states.view == "Fireplace":
        # if statements that look at the fireplace's state and determine what image to show
        if states.damper and not states.fire: WIN.blit(FIREPLACE_UNLIT_CLOSED, (0,0)) #display unlit closed damper fireplace
        elif not states.damper and not states.fire: WIN.blit(FIREPLACE_UNLIT_OPEN, (0,0)) #display unlit open damper fireplace
        else: WIN.blit(FIREPLACE_LIT_OPEN, (0,0)) #display lit open damper fireplace
        
    elif states.view == "Window":
        # here we add if statements that looks at the window's state and determines what image to show
        if states.window_phase == 1: WIN.blit(WINDOW_LOCKED1, (0, 0)) #display fully locked window phase (phase = 1)
        elif states.window_phase == 2: WIN.blit(WINDOW_LOCKED2, (0,0)) #display second phase locked window (phase = 2)
        elif states.window_phase == 3: WIN.blit(WINDOW_LOCKED3, (0,0)) #display third phase locked window (phase = 3)
        elif states.window_phase == 4: WIN.blit(WINDOW_UNLOCKED, (0,0)) #display window unlocked (phase = 4)

    elif states.view == "Door": WIN.blit(DOOR, (0,0)) #display Frontdoor image

    elif states.view == 'Door-lock': 
        if states.door_phase == 1:  WIN.blit(DOOR_LOCKED1, (0,0)) #display fully locked door phase (phase = 1)
        elif states.door_phase == 2: WIN.blit(DOOR_LOCKED2, (0,0)) #display second phase locked door (phase = 2)
        elif states.door_phase == 3: WIN.blit(DOOR_LOCKED3, (0,0)) #display third phase locked door (phase = 3)
        elif states.door_phase == 4: WIN.blit(DOOR_LOCKED4, (0,0)) #display Fourth phase locked door (phase = 4)
        elif states.door_phase == 5: WIN.blit(DOOR_UNLOCKED, (0,0)) #display unlocked door (phase = 5)
    
    elif states.view == "Bunker":
        if not states.holding: WIN.blit(BUNKER, (0,0)) #display Bunker image
        else: WIN.blit(BUNKER_HELD, (0,0)) #display bunker held closed image

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
    HOME_BUTTON_WIDTH = 625
    HOME_BUTTON_HEIGHT = 59
    PAUSE_BUTTON_WIDTH = 85
    PAUSE_BUTTON_HEIGHT = 18
    rects = {
        'START_BUTTON': pygame.Rect((125, 203), (HOME_BUTTON_WIDTH, HOME_BUTTON_HEIGHT)),
        'QUIT_BUTTON': pygame.Rect((125, 407), (HOME_BUTTON_WIDTH, HOME_BUTTON_HEIGHT)),
        'RESUME_BUTTON': pygame.Rect((405,203), (PAUSE_BUTTON_WIDTH, PAUSE_BUTTON_HEIGHT)),
        'QUIT_BUTTON_PAUSED': pygame.Rect((405, 293), (PAUSE_BUTTON_WIDTH, PAUSE_BUTTON_HEIGHT)),
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
        update_music(states)

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
                    states.num_seconds += 1
                    states.jiggle_countdown -= 1
                    states.lock_countdown -= 1
                    states.climbdown_countdown -= 1
                    if states.FP_attack:
                        states.FP_countdown -= 1
                    if not states.B_checked:    
                        states.bunkerwalk_countdown -= 1
                    elif states.B_CTcountdown > 0:
                        states.B_CTcountdown -= 1
                    else:
                        states.B_checked = False
                        states.B_CTcountdown = states.B_checkedtime
                    if states.B_attack:
                        states.B_countdown -= 1
            
        draw_image(states) # update image after every event has been iterated through

if __name__ == "__main__":
    main()