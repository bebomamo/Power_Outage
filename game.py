from ast import Num
from sre_constants import JUMP
from tkinter import N
import pygame, os, sys
from objects import *
from dataclasses import dataclass
from pygame import QUIT, mixer

# constants
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
SEC = 1000 # 1000 milliseconds
FPS = 60

pygame.init() # start pygame
pygame.mixer.init() #start mixer
clock = pygame.time.Clock()  

# Window setup
WIDTH, HEIGHT = 900, 500 #subject to change
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
WIN.fill(WHITE)
pygame.display.set_caption("Power Outage")

# Objects and backgrounds
# home_night = night_select() # - commented out for now
HOME_IMAGE = pygame.image.load(os.path.join('assets', 'PO_home_alpha.PNG')).convert() #adding image ****this line will be changed, PO_night1.PNG will actually be night_select()****
HOME = pygame.transform.scale(HOME_IMAGE, (WIDTH, HEIGHT)) #image resizing

NIGHT_WIN_IMAGE = pygame.image.load(os.path.join('assets', 'PO_win_screen_beta.png')).convert()
NIGHT_WIN = pygame.transform.scale(NIGHT_WIN_IMAGE, (WIDTH, HEIGHT)) #image resizing

NIGHT_LOSE_IMAGE = pygame.image.load(os.path.join('assets', 'PO_lose_screen_beta.png')).convert()
NIGHT_LOSE = pygame.transform.scale(NIGHT_LOSE_IMAGE, (WIDTH, HEIGHT))

FINAL_WIN_IMAGE = pygame.image.load(os.path.join('assets', 'PO_final_win_screen_beta.png')).convert()
FINAL_WIN = pygame.transform.scale(FINAL_WIN_IMAGE, (WIDTH, HEIGHT))

JUMPSCARE_IMAGE = pygame.image.load(os.path.join('assets', 'dummy.jpg')).convert_alpha()
JUMPSCARE = pygame.transform.scale(JUMPSCARE_IMAGE, (WIDTH, HEIGHT))

PAUSE_MENU = pygame.image.load(os.path.join('assets', 'PO_pause_menu_beta.png')).convert_alpha()

SAVE_MENU = pygame.image.load(os.path.join('assets', 'PO_save_menu_beta.png')).convert_alpha()

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

#Fear bar section initialization
FEARBAR1_IMAGE = pygame.image.load(os.path.join('assets', 'PO_fear_p1.PNG')).convert() #initializing all fear bar images
FEARBAR1 = pygame.transform.scale(FEARBAR1_IMAGE, (200, 50)) # image resizing 
FEARBAR2_IMAGE = pygame.image.load(os.path.join('assets', 'PO_fear_p2.PNG')).convert()
FEARBAR2 = pygame.transform.scale(FEARBAR2_IMAGE, (200, 50))
FEARBAR3_IMAGE = pygame.image.load(os.path.join('assets', 'PO_fear_p3.PNG')).convert()
FEARBAR3 = pygame.transform.scale(FEARBAR3_IMAGE, (200, 50))
FEARBAR4_IMAGE = pygame.image.load(os.path.join('assets', 'PO_fear_p4.PNG')).convert()
FEARBAR4 = pygame.transform.scale(FEARBAR4_IMAGE, (200, 50))
FEARBAR5_IMAGE = pygame.image.load(os.path.join('assets', 'PO_fear_p5.PNG')).convert()
FEARBAR5 = pygame.transform.scale(FEARBAR5_IMAGE, (200, 50))
FEARBAR6_IMAGE = pygame.image.load(os.path.join('assets', 'PO_fear_p6.PNG')).convert()
FEARBAR6 = pygame.transform.scale(FEARBAR6_IMAGE, (200, 50))
FEARBAR7_IMAGE = pygame.image.load(os.path.join('assets', 'PO_fear_p7.PNG')).convert()
FEARBAR7 = pygame.transform.scale(FEARBAR7_IMAGE, (200, 50))
FEARBAR8_IMAGE = pygame.image.load(os.path.join('assets', 'PO_fear_p8.PNG')).convert()
FEARBAR8 = pygame.transform.scale(FEARBAR8_IMAGE, (200, 50))

#Audio asset initialization
#for window
JIGGLE_S = mixer.Sound(os.path.join('assets', 'Jiggle.wav')) #
#for door
LOCK_S = mixer.Sound(os.path.join('assets', 'Lock.wav')) #
#for bunker
BUNKER_HOLD_S = mixer.Sound(os.path.join('assets', 'Bunker_hold.wav')) #
BUNKER_RELEASE_S = mixer.Sound(os.path.join('assets', 'Bunker_release.wav')) #
WALK_TOWARDS_S = mixer.Sound(os.path.join('assets', 'Walk_towards.wav'))
WALK_AWAY_S = mixer.Sound(os.path.join('assets', 'Walk_away.wav'))
#for fireplace
CLIMB_DOWN_S = mixer.Sound(os.path.join('assets', 'Climb_down.wav'))
CLIMB_UP_S = mixer.Sound(os.path.join('assets', 'Climb_up.wav'))
CLOSE_DAMPER_S = mixer.Sound(os.path.join('assets', 'Close_damper.wav')) #
OPEN_DAMPER_S = mixer.Sound(os.path.join('assets', 'Open_damper.wav')) #
FIRE_ON_S = mixer.Sound(os.path.join('assets', 'Fire_on.wav')) #
FIRE_RUNNING_S = mixer.Sound(os.path.join('assets', 'Fire_running.wav')) #
FIRE_OFF_S = mixer.Sound(os.path.join('assets', 'Fire_off.wav')) #
#for fear
BEEPS_S = mixer.Sound(os.path.join('assets', 'New_Recording.wav'))
FEAR_S = mixer.Sound(os.path.join('assets', 'Fear.wav'))
#for jumpscare
JUMPSCARE_S = mixer.Sound(os.path.join('assets', 'JumpscareOne.wav'))

# function that controls the game's home screen
def home_screen(states: States):
    START_BUTTON = Button('PO_start_button_red_black_beta.png', 'PO_start_button_green_black_beta.png', 'button_pressed.mp3', (125, 203), WIN)
    RESTART_BUTTON = Button('PO_restart_button_red_black_beta.png', 'PO_restart_button_green_black_beta.png', 'button_pressed.mp3', (125, 305), WIN)
    QUIT_BUTTON = Button('PO_quit_button_red_black_beta.png', 'PO_quit_button_green_black_beta.png', 'button_pressed.mp3', (125, 407), WIN)

    advance = False # set to True when the player is ready to move on to the next screen

    while not advance:
        clock.tick(FPS)

        loc = pygame.mouse.get_pos()

        WIN.blit(HOME, (0,0))

        for button in [START_BUTTON, RESTART_BUTTON, QUIT_BUTTON]: button.process()

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if START_BUTTON.rect.collidepoint(loc[0],loc[1]): 
                    states.keep_playing = True # begin game sequence
                    advance = True
                if RESTART_BUTTON.rect.collidepoint(loc[0],loc[1]):
                    states.night = 1 # start at night 1 no matter what 
                    states.keep_playing = True
                    advance = True
                if QUIT_BUTTON.rect.collidepoint(loc[0],loc[1]):
                    pygame.quit()
                    sys.exit()

# function that controls the game's loading screens
def load_screen(states: States):
    sec_timer = pygame.USEREVENT + 0 # event that appears on the event queue once per second, used for timing
    pygame.time.set_timer(sec_timer, 1000)

    advance = False
    num_seconds = 0 # number of seconds passes since screen was entered

    while not advance:
        if states.night == 1: WIN.blit(NIGHT1_LOAD, (0,0))
        elif states.night == 2: WIN.blit(NIGHT2_LOAD, (0,0))
        elif states.night == 3: WIN.blit(NIGHT3_LOAD, (0,0))
        elif states.night == 4: WIN.blit(NIGHT4_LOAD, (0,0))
        elif states.night == 5: WIN.blit(NIGHT5_LOAD, (0,0))
        elif states.night == 6: WIN.blit(NIGHT6_LOAD, (0,0))
        elif states.night == 7: WIN.blit(NIGHT7_LOAD, (0,0))

        if num_seconds > 3: advance = True

        for event in pygame.event.get():
            if event.type == sec_timer:
                num_seconds += 1

        pygame.display.update()

# function that controls the game's win screen
def win_screen(states: States):
    NEXT_NIGHT_BUTTON = Button('PO_next_night_button_red_black_beta.png', 'PO_next_night_button_green_black_beta.png', 'button_pressed.mp3', (125, 305), WIN)
    QUIT_BUTTON = Button('PO_quit_button_red_black_beta.png', 'PO_quit_button_green_black_beta.png', 'button_pressed.mp3', (125, 407), WIN)
    SAVE_BUTTON_YES = Button('PO_save_button_yes_beta.png', 'PO_save_button_yes_hover_beta.png', 'button_pressed.mp3', (405, 203), WIN)
    SAVE_BUTTON_NO = Button('PO_save_button_no_beta.png', 'PO_save_button_no_hover_beta.png', 'button_pressed.mp3', (405, 250), WIN)
    
    advance = False # set to True when the player is ready to move on to the next screen
    save_menu = False # set to True when the save menu is to be displayed

    while not advance:
        clock.tick(FPS)

        loc = pygame.mouse.get_pos()

        WIN.blit(NIGHT_WIN, (0,0))
        NEXT_NIGHT_BUTTON.process()
        QUIT_BUTTON.process()

        if save_menu:
            WIN.blit(SAVE_MENU, (325, 125))
            SAVE_BUTTON_YES.process()
            SAVE_BUTTON_NO.process()
        
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not save_menu:
                    if NEXT_NIGHT_BUTTON.rect.collidepoint(loc[0],loc[1]):
                        advance = True
                    if QUIT_BUTTON.rect.collidepoint(loc[0],loc[1]):
                        save_menu = True
                if save_menu:
                    if SAVE_BUTTON_YES.rect.collidepoint(loc[0],loc[1]):
                        set_night(states.night) # write night to night.txt (it will already have been incremented when this is called)
                        pygame.quit()
                        sys.exit()
                    if SAVE_BUTTON_NO.rect.collidepoint(loc[0],loc[1]):
                        pygame.quit()
                        sys.exit()

# function that controls the game's lose screen
def lose_screen(states: States):
    RESTART_BUTTON = Button('PO_restart_button_red_black_beta.png', 'PO_restart_button_green_black_beta.png', 'button_pressed.mp3', (125, 305), WIN)
    QUIT_BUTTON = Button('PO_quit_button_red_black_beta.png', 'PO_quit_button_green_black_beta.png', 'button_pressed.mp3', (125, 407), WIN)
    SAVE_BUTTON_YES = Button('PO_save_button_yes_beta.png', 'PO_save_button_yes_hover_beta.png', 'button_pressed.mp3', (405, 203), WIN)
    SAVE_BUTTON_NO = Button('PO_save_button_no_beta.png', 'PO_save_button_no_hover_beta.png', 'button_pressed.mp3', (405, 250), WIN)
    
    advance = False # set to True when the player is ready to move on to the next screen
    save_menu = False # set to True when the save menu is to be displayed

    while not advance:
        clock.tick(FPS)

        loc = pygame.mouse.get_pos()

        WIN.blit(NIGHT_LOSE, (0,0))
        RESTART_BUTTON.process()
        QUIT_BUTTON.process()

        if save_menu:
            WIN.blit(SAVE_MENU, (325, 125))
            SAVE_BUTTON_YES.process()
            SAVE_BUTTON_NO.process()
        
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not save_menu:
                    if RESTART_BUTTON.rect.collidepoint(loc[0],loc[1]):
                        advance = True
                    if QUIT_BUTTON.rect.collidepoint(loc[0],loc[1]):
                        save_menu = True
                if save_menu:
                    if SAVE_BUTTON_YES.rect.collidepoint(loc[0],loc[1]):
                        set_night(states.night) # write failed night to night.txt (night will not have been incremented when this is called)
                        pygame.quit()
                        sys.exit()
                    if SAVE_BUTTON_NO.rect.collidepoint(loc[0],loc[1]):
                        pygame.quit()
                        sys.exit()

def final_win_screen():
    QUIT_BUTTON = Button('PO_quit_button_red_black_beta.png', 'PO_quit_button_green_black_beta.png', 'button_pressed.mp3', (125, 407), WIN)

    advance = False # set to True when the player is ready to move on to the next screen

    while not advance:
        clock.tick(FPS)

        loc = pygame.mouse.get_pos()

        WIN.blit(FINAL_WIN, (0,0))
        QUIT_BUTTON.process()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if QUIT_BUTTON.rect.collidepoint(loc[0],loc[1]):
                    set_night(1)
                    pygame.quit()
                    sys.exit()

# Function that controls the game's easter egg screen
def egg_screen():
    sec_timer = pygame.USEREVENT + 0 # event that appears on the event queue once per second, used for timing
    pygame.time.set_timer(sec_timer, 1000)

    advance = False
    num_seconds = 0 # number of seconds that have passed since this screen was entered

    while not advance:
        
        # code for video should go here

        if num_seconds > 5: advance = True

        for event in pygame.event.get():
            if event.type == sec_timer:
                num_seconds += 1

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

# fucntion that handles clicks during the game based off the current game states and mouse position
def handle_clicks(states: States, rects: dict, clicking: bool, right_clicking: bool, loc: tuple):
    if clicking: # handle clicks
        if states.playing: # handle clicks while playing
            if states.view == "Fireplace":
                if rects['LOG'].collidepoint(loc[0],loc[1]):
                    if states.fire: 
                        FIRE_OFF_S.play()
                        states.fire = False
                        states.music_swap = True
                    elif not states.damper:  #must add message to let the player know the damper must be open to turn on fire
                        FIRE_ON_S.play()
                        states.fire = True
                        states.music_swap = True
                elif rects['DAMPER'].collidepoint(loc[0],loc[1]):
                    if not states.fire:
                        if states.damper: 
                            states.damper = False
                            OPEN_DAMPER_S.play()
                        else: 
                            states.damper = True
                            CLOSE_DAMPER_S.play()
                            if states.FP_attack:
                                states.FP_countdown = states.FP_time
                                states.FP_attack = False
                                CLIMB_UP_S.play()
                elif rects['FP_RIGHT'].collidepoint(loc[0], loc[1]): #these next three sections need lots of control logic once the game functionality begins getting coded, this is just for movement control
                    states.view = 'Window'
                elif rects['FP_LEFT'].collidepoint(loc[0], loc[1]): states.view = "Door"
                elif rects['FP_DOWN'].collidepoint(loc[0], loc[1]): 
                    states.view = "Bunker"
                    if not states.B_firstattack:
                        states.B_checked = True
                        states.B_CTcountdown = states.B_checkedtime
                elif rects['egg'].collidepoint(loc[0], loc[1]): 
                    # egg_screen()
                    pass
                    
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
                        BUNKER_RELEASE_S.play()
                    else: 
                        states.holding = True
                        BUNKER_HOLD_S.play()
                        if states.B_attack:
                                states.B_countdown = states.B_time
                                states.B_attack = False
                                WALK_AWAY_S.play()
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
        JIGGLE_S.play()

    # Door
    if states.lock_countdown < 0:
        states.lock_countdown = states.lock_time
        states.door_phase += 1
        LOCK_S.play()

    # Fireplace
    if states.climbdown_countdown < 0:
        states.climbdown_countdown = states.climbdown_time
        if not states.damper:
            CLIMB_DOWN_S.play()
            states.FP_attack = True

    # Bunker
    if states.bunkerwalk_countdown < 0:
        states.bunkerwalk_countdown = states.bunkerwalk_time / 4
        WALK_TOWARDS_S.play()
        states.B_attack = True
        states.B_firstattack = True

    #Fear Bar
    if states.fear_countdown < 0:                     #controls natural fear dropping
        states.fear_countdown = states.fear_time
        states.fear += 1
        FEAR_S.play()
    if states.fire:                                   #controls fire healing fear
        if states.fire_countdown < 0: 
            states.fire_countdown = states.fire_time 
            if states.fear > 1:
                states.fear -= 1

def fear(fear):
    if fear == 1: return FEARBAR1
    elif fear == 2: return FEARBAR2
    elif fear == 3: return FEARBAR3
    elif fear == 4: return FEARBAR4
    elif fear == 5: return FEARBAR5
    elif fear == 6: return FEARBAR6
    elif fear == 7: return FEARBAR7
    elif fear == 8: return FEARBAR8
        
# function that determines which images to display during the game based off current game states
def draw_image(states: States, buttons: dict):
    if states.view == "Fireplace":
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
        
    elif states.view == "Door": 
        WIN.blit(DOOR, (0,0)) #display Frontdoor image
        
    elif states.view == 'Door-lock': 
        if states.door_phase == 1:  WIN.blit(DOOR_LOCKED1, (0,0)) #display fully locked door phase (phase = 1)
        elif states.door_phase == 2: WIN.blit(DOOR_LOCKED2, (0,0)) #display second phase locked door (phase = 2)
        elif states.door_phase == 3: WIN.blit(DOOR_LOCKED3, (0,0)) #display third phase locked door (phase = 3)
        elif states.door_phase == 4: WIN.blit(DOOR_LOCKED4, (0,0)) #display Fourth phase locked door (phase = 4)
        elif states.door_phase == 5: WIN.blit(DOOR_UNLOCKED, (0,0)) #display unlocked door (phase = 5)
        
    elif states.view == "Bunker":
        if not states.holding: WIN.blit(BUNKER, (0,0)) #display Bunker image
        else: WIN.blit(BUNKER_HELD, (0,0)) #display bunker held closed image
        
    # FEAR determining display
    WIN.blit(fear(states.fear), (80,10))

    if states.paused:
        # note: this part needs to be at the bottom so that the pause menu will overlay everything else
        WIN.blit(PAUSE_MENU, (325, 125))

    for button in buttons: buttons[button].process()

    if states.night_lost:
        if states.lose_timer > 10: WIN.blit(JUMPSCARE, (0,0))

    pygame.display.update()

# function that determines whether the player has won or lost the current night
def is_night_over(states: States):
    # player loses
    if states.window_phase == 4 or states.door_phase == 5 or states.FP_countdown < 0 or states.B_countdown < 0 or states.fear >= 7:
        states.night_lost = True

    # player wins
    if states.num_seconds > 600: states.night_won = True

# Function that determines what Buttons are to be displayed based on all current game states
def button_manager(states: States, buttons: dict, rects: dict):
    if states.view == 'Fireplace':
        buttons['FP_LEFT'] = Button('PO_view_left_button_beta.png', 'PO_view_left_button_hover_beta.png', 'swoosh.mp3', (17,32), WIN)
        buttons['FP_RIGHT'] = Button('PO_view_right_button_beta.png', 'PO_view_right_button_hover_beta.png', 'swoosh.mp3', (831,32), WIN)
        buttons['FP_DOWN'] = Button('PO_view_down_button_beta.png', 'PO_view_down_button_hover_beta.png', 'swoosh.mp3', (113,435), WIN)
    
    if states.view == 'Door':
        buttons['DO_RIGHT'] = Button('PO_view_right_button_beta.png', 'PO_view_right_button_hover_beta.png', 'swoosh.mp3', (787,28), WIN)

    if states.view == 'Window':
        buttons['WI_LEFT'] = Button('PO_view_left_button_beta.png', 'PO_view_left_button_hover_beta.png', 'swoosh.mp3', (11,29), WIN)

    if states.view == 'Bunker':
        buttons['BU_DOWN'] = Button('PO_view_down_button_beta.png', 'PO_view_down_button_hover_beta.png', 'swoosh.mp3', (113,422), WIN)

    if states.paused:
        buttons['RESUME_BUTTON'] = Button('PO_resume_button_beta.png', 'PO_resume_button_hover_beta.png', 'button_pressed.mp3', (405, 203), WIN)
        buttons['SETTINGS_BUTTON_PAUSED'] = Button('PO_settings_button_beta.png', 'PO_settings_button_hover_beta.png', 'button_pressed.mp3', (405, 245), WIN)
        buttons['QUIT_BUTTON_PAUSED'] = Button('PO_pausequit_beta.png', 'PO_pausequit_hover_beta.png', 'button_pressed.mp3', (405, 293), WIN)

    # add every Button's rectangle to the rects dictionary
    for button in buttons: rects[button] = buttons[button].rect
        

# Function that manages the in-game portion of the game. The actual implementations for the game's features,
# such as click handeling and displaying images, are defined in the above functions.
def game_screen(states: States):
    sec_timer = pygame.USEREVENT + 0 # event that appears on the event queue once per second, used for timing
    pygame.time.set_timer(sec_timer, 1000)

    # clicking initialization
    clicking = False
    right_clicking = False

    states.playing = True # game is now being played
    advance = False # set to True when the player is ready to move on to the next screen

    beepcheck = False
    jumpscarecheck = False

    while not advance:
        clock.tick(FPS)

        # Dictionary containing all of the Button objects to be used in the game
        buttons = {}

        # Dictionary containing all of the Rect objects to be used in the game
        rects = {
            'LOG': pygame.Rect((343, 157), (92, 18)),
            'DAMPER': pygame.Rect((325, 125), (10, 24)),
            'WI_LOCK': pygame.Rect((489, 207), (68, 22)),
            'DOOR': pygame.Rect((166, 28), (352, 454)),
            'BUNKER': pygame.Rect((112,34), (642, 312)),
            'egg': pygame.Rect((390,290), (10,10))
        }

        loc = pygame.mouse.get_pos()
        button_manager(states, buttons, rects)
        handle_clicks(states, rects, clicking, right_clicking, loc)
        update_states(states)
        update_music(states)
        is_night_over(states)
        draw_image(states, buttons) # update display after all game states have been updated

        if states.night_won: advance = True

        if states.night_lost: 
            if states.lose_timer > 10 and jumpscarecheck == False:
                BEEPS_S.stop()
                JUMPSCARE_S.play()
                jumpscarecheck = True
            elif beepcheck == False:
                BEEPS_S.play()
                beepcheck = True
            if states.lose_timer > 13: advance = True

        clicking = False # one click allowed per frame - may or may not be changed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if not states.night_lost: # if night is lost you can't click or press any buttons
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
                        states.playing = not states.playing
                        states.paused = not states.paused

            if states.playing: # all events that we only want to process while the game is being played (aka not paused)
                if event.type == sec_timer:
                    # anything in here will occur once for every second of playtime
                    if not states.night_lost and not states.night_won:
                        states.num_seconds += 1
                        states.jiggle_countdown -= 1
                        states.lock_countdown -= 1
                        states.climbdown_countdown -= 1
                        states.fear_countdown -= 1

                        if states.FP_attack: states.FP_countdown -= 1
                        
                        if not states.B_checked: states.bunkerwalk_countdown -= 1
                        elif states.B_CTcountdown > 0: states.B_CTcountdown -= 1
                        else:
                            states.B_checked = False
                            states.B_CTcountdown = states.B_checkedtime
                        if states.B_attack: states.B_countdown -= 1

                        if states.fire: states.fire_countdown -= 1

                    elif states.night_lost: states.lose_timer += 1 # increment lose_timer if night is lost

# function that controls the sequencing of the game (which screens are to be displayed and when, current game states, etc.)
def main():
    states = States()

    home_screen(states)
    current_night = states.night
    load_screen(states)

    while states.keep_playing:
        game_screen(states)
        if states.night_won: 
            current_night += 1
            states = States(current_night, True)

            if current_night == 8: 
                # player has beaten the game
                break

            win_screen(states)
            load_screen(states)
            game_screen(states)


        elif states.night_lost: 
            states = States(current_night, True)
            lose_screen(states)
            load_screen(states)
            game_screen(states)
    
    final_win_screen()
            
if __name__ == "__main__":
    main()
