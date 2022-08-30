from ast import Num
from math import nextafter
from sre_constants import JUMP
from tkinter import N
import pygame, os, sys
from objects import *
from dataclasses import dataclass
from pygame import QUIT, mixer

# constants
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (34, 139, 34)
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
BLANK_IMAGE = pygame.image.load(os.path.join('assets', 'blankscreen.jpg')).convert()
BLANK_SCREEN = pygame.transform.scale(BLANK_IMAGE, (WIDTH, HEIGHT))

HOME_IMAGE = pygame.image.load(os.path.join('assets', 'homescreen.png')).convert() #adding image 
HOME = pygame.transform.scale(HOME_IMAGE, (WIDTH, HEIGHT)) #image resizing

NIGHT_WIN_IMAGE = pygame.image.load(os.path.join('assets', 'yousurvivedscreen.png')).convert()
NIGHT_WIN = pygame.transform.scale(NIGHT_WIN_IMAGE, (WIDTH, HEIGHT)) #image resizing

NIGHT_LOSE_IMAGE = pygame.image.load(os.path.join('assets', 'youlostscreen.png')).convert()
NIGHT_LOSE = pygame.transform.scale(NIGHT_LOSE_IMAGE, (WIDTH, HEIGHT))

FINAL_WIN_IMAGE = pygame.image.load(os.path.join('assets', 'yousurvivedscreen.png')).convert()
FINAL_WIN = pygame.transform.scale(FINAL_WIN_IMAGE, (WIDTH, HEIGHT))

JUMPSCARE_IMAGE = pygame.image.load(os.path.join('assets', 'IMG_0328.png')).convert_alpha()
JUMPSCARE = pygame.transform.scale(JUMPSCARE_IMAGE, (WIDTH, HEIGHT))

PAUSE_MENU = pygame.image.load(os.path.join('assets', 'pausemenu.png')).convert_alpha()

SAVE_MENU = pygame.image.load(os.path.join('assets', 'saveprogressmenu.png')).convert_alpha()

NIGHT1_LOAD_IMAGE = pygame.image.load(os.path.join('assets', 'night1load.jpg')).convert()
NIGHT1_LOAD = pygame.transform.scale(NIGHT1_LOAD_IMAGE, (WIDTH, HEIGHT))
NIGHT2_LOAD_IMAGE = pygame.image.load(os.path.join('assets', 'night2load.jpg')).convert()
NIGHT2_LOAD = pygame.transform.scale(NIGHT2_LOAD_IMAGE, (WIDTH, HEIGHT))
NIGHT3_LOAD_IMAGE = pygame.image.load(os.path.join('assets', 'night3load.jpg')).convert()
NIGHT3_LOAD = pygame.transform.scale(NIGHT3_LOAD_IMAGE, (WIDTH, HEIGHT))
NIGHT4_LOAD_IMAGE = pygame.image.load(os.path.join('assets', 'night4load.jpg')).convert()
NIGHT4_LOAD = pygame.transform.scale(NIGHT4_LOAD_IMAGE, (WIDTH, HEIGHT))
NIGHT5_LOAD_IMAGE = pygame.image.load(os.path.join('assets', 'night5load.jpg')).convert()
NIGHT5_LOAD = pygame.transform.scale(NIGHT5_LOAD_IMAGE, (WIDTH, HEIGHT))
NIGHT6_LOAD_IMAGE = pygame.image.load(os.path.join('assets', 'night6load.jpg')).convert()
NIGHT6_LOAD = pygame.transform.scale(NIGHT6_LOAD_IMAGE, (WIDTH, HEIGHT))
NIGHT7_LOAD_IMAGE = pygame.image.load(os.path.join('assets', 'night7load.jpg')).convert()
NIGHT7_LOAD = pygame.transform.scale(NIGHT7_LOAD_IMAGE, (WIDTH, HEIGHT))

FIREPLACE_UNLIT_OPEN_IMAGE = pygame.image.load(os.path.join('assets', 'fireplace_closed.jpg')).convert() #adding image
FIREPLACE_UNLIT_OPEN = pygame.transform.scale(FIREPLACE_UNLIT_OPEN_IMAGE, (WIDTH, HEIGHT)) #image resizing
FIREPLACE_UNLIT_CLOSED_IMAGE = pygame.image.load(os.path.join('assets', 'fireplace_extinguish.jpg')).convert() #adding image
FIREPLACE_UNLIT_CLOSED = pygame.transform.scale(FIREPLACE_UNLIT_CLOSED_IMAGE, (WIDTH, HEIGHT)) #image resizing
FIREPLACE_LIT_OPEN_IMAGE = pygame.image.load(os.path.join('assets', 'fireplace_on.jpg')).convert() #adding image
FIREPLACE_LIT_OPEN = pygame.transform.scale(FIREPLACE_LIT_OPEN_IMAGE, (WIDTH, HEIGHT)) #image resizing-----------------------------------------------------------

BUNKER_IMAGE = pygame.image.load(os.path.join('assets', 'bunker.jpg')).convert() #adding image
BUNKER = pygame.transform.scale(BUNKER_IMAGE, (WIDTH, HEIGHT)) #image resizing
BUNKER_HELD_IMAGE = pygame.image.load(os.path.join('assets', 'bunkerheld.jpg')).convert() #adding image
BUNKER_HELD = pygame.transform.scale(BUNKER_HELD_IMAGE, (WIDTH, HEIGHT)) #image resizing
DOOR_LOCKED1_IMAGE = pygame.image.load(os.path.join('assets', 'doorlocked.jpg')).convert() #adding image
DOOR_LOCKED1 = pygame.transform.scale(DOOR_LOCKED1_IMAGE, (WIDTH, HEIGHT)) #image resizing
DOOR_LOCKED2_IMAGE = pygame.image.load(os.path.join('assets', 'doorphase2.jpg')).convert() #adding image
DOOR_LOCKED2 = pygame.transform.scale(DOOR_LOCKED2_IMAGE, (WIDTH, HEIGHT)) #image resizing
DOOR_LOCKED3_IMAGE = pygame.image.load(os.path.join('assets', 'doorphase3.jpg')).convert() #adding image
DOOR_LOCKED3 = pygame.transform.scale(DOOR_LOCKED3_IMAGE, (WIDTH, HEIGHT)) #image resizing
DOOR_LOCKED4_IMAGE = pygame.image.load(os.path.join('assets', 'doorphase4.jpg')).convert() #adding image
DOOR_LOCKED4 = pygame.transform.scale(DOOR_LOCKED4_IMAGE, (WIDTH, HEIGHT)) #image resizing
DOOR_UNLOCKED_IMAGE = pygame.image.load(os.path.join('assets', 'doorunlocked.jpg')).convert() #adding image
DOOR_UNLOCKED = pygame.transform.scale(DOOR_UNLOCKED_IMAGE, (WIDTH, HEIGHT)) #image resizing

WINDOW_LOCKED1_IMAGE = pygame.image.load(os.path.join('assets', 'windowlocked.jpg')).convert() #adding image
WINDOW_LOCKED1 = pygame.transform.scale(WINDOW_LOCKED1_IMAGE, (WIDTH, HEIGHT)) #image resizing
WINDOW_LOCKED2_IMAGE = pygame.image.load(os.path.join('assets', 'windowphase2.jpg')).convert() #adding image
WINDOW_LOCKED2 = pygame.transform.scale(WINDOW_LOCKED2_IMAGE, (WIDTH, HEIGHT)) #image resizing
WINDOW_LOCKED3_IMAGE = pygame.image.load(os.path.join('assets', 'windowphase4.jpg')).convert() #adding image
WINDOW_LOCKED3 = pygame.transform.scale(WINDOW_LOCKED3_IMAGE, (WIDTH, HEIGHT)) #image resizing
WINDOW_UNLOCKED_IMAGE = pygame.image.load(os.path.join('assets', 'windowopen.jpg')).convert() #adding image
WINDOW_UNLOCKED = pygame.transform.scale(WINDOW_UNLOCKED_IMAGE, (WIDTH, HEIGHT)) #image resizing

#Fear bar section initialization
FEARBAR1_IMAGE = pygame.image.load(os.path.join('assets', 'fear1.png')).convert_alpha() #initializing all fear bar images
FEARBAR1 = pygame.transform.scale(FEARBAR1_IMAGE, (200, 50)) # image resizing 
FEARBAR2_IMAGE = pygame.image.load(os.path.join('assets', 'fear2.png')).convert_alpha()
FEARBAR2 = pygame.transform.scale(FEARBAR2_IMAGE, (200, 50))
FEARBAR3_IMAGE = pygame.image.load(os.path.join('assets', 'fear3.png')).convert_alpha()
FEARBAR3 = pygame.transform.scale(FEARBAR3_IMAGE, (200, 50))
FEARBAR4_IMAGE = pygame.image.load(os.path.join('assets', 'fear4.png')).convert_alpha()
FEARBAR4 = pygame.transform.scale(FEARBAR4_IMAGE, (200, 50))
FEARBAR5_IMAGE = pygame.image.load(os.path.join('assets', 'fear5.png')).convert_alpha()
FEARBAR5 = pygame.transform.scale(FEARBAR5_IMAGE, (200, 50))
FEARBAR6_IMAGE = pygame.image.load(os.path.join('assets', 'fear6.png')).convert_alpha()
FEARBAR6 = pygame.transform.scale(FEARBAR6_IMAGE, (200, 50))
FEARBAR7_IMAGE = pygame.image.load(os.path.join('assets', 'fear7.png')).convert_alpha()
FEARBAR7 = pygame.transform.scale(FEARBAR7_IMAGE, (200, 50))
FEARBAR8_IMAGE = pygame.image.load(os.path.join('assets', 'fear8.png')).convert_alpha()
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
    tenth_sec = pygame.USEREVENT + 0
    pygame.time.set_timer(tenth_sec, 100)

    START_BUTTON = Button('startbutton.png', 'startbuttonhover.png', 'button_pressed.mp3', (275, 197), WIN)
    RESTART_BUTTON = Button('restartbutton.png', 'restartbuttonhover.png', 'button_pressed.mp3', (275, 297), WIN)
    QUIT_BUTTON = Button('quitbutton.png', 'quitbuttonhover.png', 'button_pressed.mp3', (275, 397), WIN)

    advance = False # set to True when the player is ready to move on to the next screen
    pre_advance = False # set to True a short time period before the player is ready to advance so that Button clicks can be heard
    advance_timer = 0 # counts the duration of the pre-advance phase (in 10s of ms) 

    # set to True when the corresponding Button is pressed
    start = False
    restart = False
    quit = False

    while not advance:
        clock.tick(FPS)

        loc = pygame.mouse.get_pos()

        WIN.blit(HOME, (0,0))

        for button in [START_BUTTON, RESTART_BUTTON, QUIT_BUTTON]: button.process()

        pygame.display.update()

        if pre_advance: 
            if advance_timer > 2: # 20 ms delay before screen advances
                if start:
                    states.keep_playing = True
                    advance = True
                if restart:
                    states.night = 1 # start at night 1 no matter what
                    states.keep_playing = True
                    advance = True
                if quit:
                    pygame.quit()
                    sys.exit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == tenth_sec:
                if pre_advance: advance_timer += 1 # increment advance timer if in pre-advance phase

            if event.type == pygame.MOUSEBUTTONDOWN:
                if START_BUTTON.rect.collidepoint(loc[0],loc[1]): 
                    pre_advance = True
                    start = True
                if RESTART_BUTTON.rect.collidepoint(loc[0],loc[1]):
                    pre_advance = True
                    restart = True
                    start = True
                if QUIT_BUTTON.rect.collidepoint(loc[0],loc[1]):
                    pre_advance = True
                    quit = True

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
    tenth_sec = pygame.USEREVENT + 0
    pygame.time.set_timer(tenth_sec, 100)

    NEXT_NIGHT_BUTTON = Button('nextnightbutton.png', 'nextnightbuttonhover.png', 'button_pressed.mp3', (275, 250), WIN)
    QUIT_BUTTON = Button('quitbutton.png', 'quitbuttonhover.png', 'button_pressed.mp3', (275, 360), WIN)
    SAVE_BUTTON_YES = Button('yesbutton.png', 'yesbuttonhover.png', 'button_pressed.mp3', (275, 250), WIN)
    SAVE_BUTTON_NO = Button('nobutton.png', 'nobuttonhover.png', 'button_pressed.mp3', (275, 360), WIN)
    
    quit_pressed = False # set to True when the player has pressed the quit button
    quit_timer = 0 # counts the time after the quit button has been pressed (in 10s of ms)

    advance = False # set to True when the player is ready to move on to the next screen
    pre_advance = False # set to True a short time period before the player is ready to advance so that Button clicks can be heard
    advance_timer = 0 # counts the duration of the pre-advance phase (in 10s of ms) 

    save_menu = False # set to True when the save menu is to be displayed

    # set to True when the corresponding Button is pressed
    next_night = False
    save_yes = False
    save_no = False

    while not advance:
        clock.tick(FPS)

        loc = pygame.mouse.get_pos()

        WIN.blit(NIGHT_WIN, (0,0))
        NEXT_NIGHT_BUTTON.process()
        QUIT_BUTTON.process()

        if save_menu:
            WIN.blit(BLANK_SCREEN, (0, 0))
            WIN.blit(SAVE_MENU, (245, 30))
            SAVE_BUTTON_YES.process()
            SAVE_BUTTON_NO.process()

        if pre_advance:
            if advance_timer > 2:
                if next_night: advance = True
                if save_yes:
                    set_night(states.night) # write night to night.txt (it will already have been incremented when this is called)
                    pygame.quit()
                    sys.exit()
                if save_no:
                    pygame.quit()
                    sys.exit()
        
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == tenth_sec: 
                if quit_pressed: quit_timer += 1 # increment quit timer if quit button has been pressed
                if pre_advance: advance_timer += 1 # increment advance timer if in pre-advance phase

            if event.type == pygame.MOUSEBUTTONDOWN:
                if not save_menu:
                    if NEXT_NIGHT_BUTTON.rect.collidepoint(loc[0],loc[1]):
                        pre_advance = True
                        next_night = True
                    if QUIT_BUTTON.rect.collidepoint(loc[0],loc[1]):
                        quit_pressed = True
                        save_menu = True
                if save_menu and quit_timer > 2:
                    if SAVE_BUTTON_YES.rect.collidepoint(loc[0],loc[1]):
                        pre_advance = True
                        save_yes = True
                    if SAVE_BUTTON_NO.rect.collidepoint(loc[0],loc[1]):
                        pre_advance = True
                        save_no = True

# function that controls the game's lose screen
def lose_screen(states: States):
    tenth_sec = pygame.USEREVENT + 0
    pygame.time.set_timer(tenth_sec, 100)

    RESTART_BUTTON = Button('restartbutton.png', 'restartbuttonhover.png', 'button_pressed.mp3', (275, 250), WIN)
    QUIT_BUTTON = Button('quitbutton.png', 'quitbuttonhover.png', 'button_pressed.mp3', (275, 360), WIN)
    SAVE_BUTTON_YES = Button('yesbutton.png', 'yesbuttonhover.png', 'button_pressed.mp3', (275, 250), WIN)
    SAVE_BUTTON_NO = Button('nobutton.png', 'nobuttonhover.png', 'button_pressed.mp3', (275, 360), WIN)
    
    quit_pressed = False # set to True when the player has pressed the quit button
    quit_timer = 0 # counts the amount of time after the player pressed the quit button (in 10s of ms)

    advance = False # set to True when the player is ready to move on to the next screen
    pre_advance = False # set to True a short time period before the player is ready to advance so that Button clicks can be heard
    advance_timer = 0 # counts the duration of the pre-advance phase (in 10s of ms) 

    save_menu = False # set to True when the save menu is to be displayed

    # set to True when the corresponding Button is pressed
    restart = False
    save_yes = False
    save_no = False

    while not advance:
        clock.tick(FPS)

        loc = pygame.mouse.get_pos()

        WIN.blit(NIGHT_LOSE, (0,0))
        RESTART_BUTTON.process()
        QUIT_BUTTON.process()

        if save_menu:
            WIN.blit(BLANK_SCREEN, (0,0))
            WIN.blit(SAVE_MENU, (245, 30))
            SAVE_BUTTON_YES.process()
            SAVE_BUTTON_NO.process()
        
        if pre_advance:
            if advance_timer > 2:
                if restart: advance = True
                if save_yes:
                    set_night(states.night) # write night to night.txt (it will already have been incremented when this is called)
                    pygame.quit()
                    sys.exit()
                if save_no:
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == tenth_sec: 
                if quit_pressed: quit_timer += 1 # increment quit timer if the player has pressed the quit button
                if pre_advance: advance_timer += 1 # increment advance timer if in pre-advance phase

            if event.type == pygame.MOUSEBUTTONDOWN:
                if not save_menu:
                    if RESTART_BUTTON.rect.collidepoint(loc[0],loc[1]):
                        pre_advance = True
                        restart = True
                    if QUIT_BUTTON.rect.collidepoint(loc[0],loc[1]):
                        quit_pressed = True
                        save_menu = True
                if save_menu and quit_timer > 2:
                    if SAVE_BUTTON_YES.rect.collidepoint(loc[0],loc[1]):
                        pre_advance = True
                        save_yes = True
                    if SAVE_BUTTON_NO.rect.collidepoint(loc[0],loc[1]):
                        pre_advance = True
                        save_no = True

def final_win_screen():
    tenth_sec = pygame.USEREVENT + 0
    pygame.time.set_timer(tenth_sec, 100)

    QUIT_BUTTON = Button('quitbutton.png', 'quitbuttonhover.png', 'button_pressed.mp3', (275, 310), WIN)

    advance = False # set to True when the player is ready to move on to the next screen
    pre_advance = False # set to True a short time period before the player is ready to advance so that Button clicks can be heard
    advance_timer = 0 # counts the duration of the pre-advance phase (in 10s of ms) 

    # set to True when the corresponding Button is pressed
    quit = False

    while not advance:
        clock.tick(FPS)

        loc = pygame.mouse.get_pos()

        WIN.blit(FINAL_WIN, (0,0))
        QUIT_BUTTON.process()

        if pre_advance:
            if advance_timer > 2:
                if quit:
                    set_night(1)
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == tenth_sec: 
                if pre_advance: advance_timer += 1 # increment advance timer if in pre-advance phase
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if QUIT_BUTTON.rect.collidepoint(loc[0],loc[1]):
                    pre_advance = True
                    quit = True

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
                # elif rects['egg'].collidepoint(loc[0], loc[1]): 
                #     # egg_screen()
                #     pass
                    
            elif states.view == "Window":
                if rects['WI_LEFT'].collidepoint(loc[0], loc[1]): #this section needs control logic based on what view the fireplace screen should be
                    states.view = "Fireplace"
                elif rects['WI_LOCK'].collidepoint(loc[0], loc[1]):
                    if states.window_phase == 2: states.window_phase = 1
                    elif states.window_phase == 3: states.window_phase = 2
                    elif states.window_phase == 4: pass #unlocked
                
            elif states.view == "Door":
                if rects['DO_RIGHT'].collidepoint(loc[0], loc[1]):
                    states.view = "Fireplace" #Again needs control logic based on what the fireplace state is
                elif states.door_phase < 5: #can relock door fully with click unless fully unlocked
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
        WIN.blit(BLANK_SCREEN, (0,0))
        # note: this part needs to be at the bottom so that the pause menu will overlay everything else
        WIN.blit(PAUSE_MENU, (245, 30))

    for button in buttons: buttons[button].process()

    if states.night_lost:
        if states.lose_timer > 10: WIN.blit(JUMPSCARE, (0,0))

    pygame.display.update()

# function that determines whether the player has won or lost the current night
def is_night_over(states: States):
    # player loses
    if states.window_phase == 4 or states.door_phase == 5 or states.FP_countdown < 0 or states.B_countdown < 0 or states.fear >= 8:
        states.night_lost = True

    # player wins
    if states.num_seconds > 300: states.night_won = True

# Function that determines which Buttons out of all possible Buttons are to be displayed in the current frame
def update_buttons(states: States, buttons: dict, all_buttons: dict, rects: dict):
    if not states.paused:
        if states.view == 'Fireplace':
            buttons['FP_LEFT'] = all_buttons['FP_LEFT']
            buttons['FP_RIGHT'] = all_buttons['FP_RIGHT']
            buttons['FP_DOWN'] = all_buttons['FP_DOWN']
        
        if states.view == 'Door':
            buttons['DO_RIGHT'] = all_buttons['DO_RIGHT']

        if states.view == 'Window':
            buttons['WI_LEFT'] = all_buttons['WI_LEFT']

        if states.view == 'Bunker':
            buttons['BU_DOWN'] = all_buttons['BU_DOWN']

    if states.paused:
        buttons['RESUME_BUTTON'] = all_buttons['RESUME_BUTTON']
        buttons['QUIT_BUTTON_PAUSED'] = all_buttons['QUIT_BUTTON_PAUSED']

    if states.night_lost: Button.audible = False # make Buttons silent when player is about to be jumpscared

    # add every Button's rectangle to the rects dictionary so that they can be used by handle_clicks
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

    # jumpscare stuff
    beepcheck = False
    jumpscarecheck = False

    # Dictionary containing all of the Buttons that are used in any frame of the game
    all_buttons = {
        'FP_LEFT': Button('viewbuttonleft.png', 'viewbuttonlefthover.png', 'swoosh.mp3', (57,102), WIN),
        'FP_RIGHT': Button('viewbuttonright.png', 'viewbuttonrighthover.png', 'swoosh.mp3', (743,102), WIN),
        'FP_DOWN': Button('viewbuttondown.png', 'viewbuttondownhover.png', 'swoosh.mp3', (342,393), WIN),
        'DO_RIGHT': Button('viewbuttonright.png', 'viewbuttonrighthover.png', 'swoosh.mp3', (743,102), WIN),
        'WI_LEFT': Button('viewbuttonleft.png', 'viewbuttonlefthover.png', 'swoosh.mp3', (57,102), WIN),
        'BU_DOWN': Button('viewbuttondown.png', 'viewbuttondownhover.png', 'swoosh.mp3', (342,393), WIN),
        'RESUME_BUTTON': Button('resumebutton.png', 'resumebuttonhover.png', 'button_pressed.mp3', (275, 250), WIN),
        'QUIT_BUTTON_PAUSED': Button('quitbutton.png', 'quitbuttonhover.png', 'button_pressed.mp3', (275, 360), WIN)
    }

    while not advance:
        clock.tick(FPS)

        # Dictionary containing all of the Button objects to be used in this frame of the game
        buttons = {}

        #(76, 32) - (485, 233) new window hitbox
        #(394, 230) - (555, 290) new log hitbox
        #(226, 61) - (273, 245) new damper pull hitbox

        # Dictionary containing all of the Rect objects to be used in the game
        rects = {
            'LOG': pygame.Rect((394, 230), (161, 60)),
            'DAMPER': pygame.Rect((226, 61), (47, 184)),
            'WI_LOCK': pygame.Rect((76, 32), (409, 200)),
            'DOOR': pygame.Rect((166, 28), (352, 454)),
            'BUNKER': pygame.Rect((112,34), (642, 312)),
            # 'egg': pygame.Rect((390,290), (10,10))
        }

        loc = pygame.mouse.get_pos()

        update_buttons(states, buttons, all_buttons, rects)
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
    states.reset_timers() # reset states so that if the player chooses to restart the state timers and current night will be synced

    load_screen(states)
    # cutscene(states)

    while states.keep_playing:
        game_screen(states)
        Button.audible = True # make clicksounds audible again so that they'll be heard in win/lose screens

        if states.night_won: 
            current_night += 1
            states = States(current_night, True)

            if current_night == 8: 
                # player has beaten the game
                break

            win_screen(states)
            load_screen(states)
            # cutscene(states)
            game_screen(states)

        elif states.night_lost: 
            states = States(current_night, True)
            lose_screen(states)
            load_screen(states)
            # cutscene(states)
            game_screen(states)
    
    final_win_screen()
            
if __name__ == "__main__":
    main()