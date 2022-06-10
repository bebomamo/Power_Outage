import pygame, os, sys
from objects import *

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

pygame.init() # start pygame

# Window setup
WIDTH, HEIGHT = 900, 500 #subject to change
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
WIN.fill(WHITE) # set to white so we remember it exists, will almost certainly be changed later
pygame.display.set_caption("Power Outage")

#---------Home Screen Startup control logic and day passing logic---------- Temporarily commented out
# def DaySelect():
#     f = open("day.txt", mode = 'r')
#     day = f.read(1)
#     if(day == '1'): 
#         return 'PO_night1.PNG'
#     if(day == '2'):
#         return 'PO_night2.PNG'
#     if(day == '3'):
#         return 'PO_night3.PNG'
#     if(day == '4'):
#         return 'PO_night4.PNG'
#     if(day == '5'):
#         return 'PO_night5.PNG'
#     if(day == '6'):
#         return 'PO_night6.PNG'
#     if(day == '7'):
#         return 'PO_night7.PNG'
#     f.close()
#------------Day getter(as a char)----------------
# def get_day():
#     f = open("day.txt", mode = 'r')
#     day = f.read(1)
#     f.close()
#     return day
#------------Day setter(as a char)----------------
# def set_day(newday):
#     f = open("day.txt", mode = 'r+')
#     f.truncate(0)
#     f.write(newday)
#     f.close()

# --------initialization nation--------
# Pygame stuff
view = "Home"
FPS = 60

# Objects and backgrounds
# HomeDay = DaySelect() # - commented out for now
HOME_image = pygame.image.load(os.path.join('assets', 'PO_night1.PNG')).convert() #adding image ****this line will be changed, PO_night1.PNG will actually be DaySelect()****
HOME = pygame.transform.scale(HOME_image, (WIDTH, HEIGHT)) #image resizing

LOAD_image = pygame.image.load(os.path.join('assets', 'dummy.jpg')).convert() #adding temp loading image
LOAD = pygame.transform.scale(LOAD_image, (WIDTH, HEIGHT)) # resizing temp load image

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


#game control logic
fire = False
damper = False #False is open damper, True is closed
window_phase = 1
door_phase = 1
holding = False
# ------------------------------

# # note: I moved DaySelect from its own file to here because it is only one function. For organization's 
# #       sake it's probably better to not create an entire file for a single function, as doing so would
# #       quickly crowd the repository and is not really convention in Python. Commented out for now



#----------------Image Drawing/View control-----------------
         #for home screens and game load, home select logic is located somewhere else
def draw_image():
    if(view == "Home"):
        WIN.blit(HOME, (0, 0)) #display home image
    elif(view == "Game-load"):
        # here we add an if statement that checks what day we are loading into
        WIN.blit(LOAD, (0, 0)) # temporary

    elif view == "Fireplace":
        # if statements that look at the fireplace's state and determine what image to show
        if damper and not fire:
            WIN.blit(FIREPLACE_unlit_closed, (0,0)) #display unlit closed damper fireplace
        elif not damper and not fire:
            WIN.blit(FIREPLACE_unlit_open, (0,0)) #display unlit open damper fireplace
        else:
            WIN.blit(FIREPLACE_lit_open, (0,0)) #display lit open damper fireplace
        
    elif(view == "Window"):
        # here we add if statements that looks at the window's state and determines what image to show
        if window_phase == 1:
            WIN.blit(WINDOW_locked1, (0, 0)) #display fully locked window phase (phase = 1)
        elif window_phase == 2:
            WIN.blit(WINDOW_locked2, (0,0)) #display second phase locked window (phase = 2)
        elif window_phase == 3:
            WIN.blit(WINDOW_locked3, (0,0)) #display third phase locked window (phase = 3)
        elif window_phase == 4:
            WIN.blit(WINDOW_unlocked, (0,0)) #display window unlocked (phase = 4)

        print()
    # elif(view == "Door"):
    #     # here we add if statements that looks at the door's state and determines what image to show
    #     print()
    # elif(view == "Bunker"):
    #     # here we add if statements that looks at the bunker's state and determines what image to show
    #     print()

    #     #for fireplace screens
    # elif(view == "Fireplace-unlit-open"):
    #     WIN.blit(FIREPLACE_unlit_open, (0,0)) #display unlit open damper fireplace
    # elif(view == "Fireplace-lit-open"):
    #     WIN.blit(FIREPLACE_lit_open, (0,0)) #display lit open damper fierplace
    # elif(view == "Fireplace-unlit-closed"):
    #     WIN.blit(FIREPLACE_unlit_closed, (0,0)) #display unlit closed damper fireplace

    #      #for window screens
    # elif(view == "Window-locked1"):
    #     WIN.blit(WINDOW_locked1, (0, 0)) #display fully locked window phase (phase = 1)
    # elif(view == "Window-locked2"):
    #     WIN.blit(WINDOW_locked2, (0,0)) #display second phase locked window (phase = 2)
    # elif(view == "Window-locked3"):
    #     WIN.blit(WINDOW_locked3, (0,0)) #display third phase locked window (phase = 3)
    # elif(view == "Window-unlocked"):
    #     WIN.blit(WINDOW_unlocked, (0,0)) #display window unlocked (phase = 4)


        #for door and door lock screens
    elif(view == "Door"):
        WIN.blit(DOOR, (0,0)) #display Frontdoor image
    elif(view == "Door-locked1"):
        WIN.blit(DOOR_locked1, (0,0)) #display fully locked door phase (phase = 1)
    elif(view == "Door-locked2"):
        WIN.blit(DOOR_locked2, (0,0)) #display second phase locked door (phase = 2)
    elif(view == "Door-locked3"):
        WIN.blit(DOOR_locked3, (0,0)) #display third phase locked door (phase = 3)
    elif(view == "Door-locked4"):
        WIN.blit(DOOR_locked4, (0,0)) #display Fourth phase locked door (phase = 4)
    elif(view == "Door-unlocked"):
        WIN.blit(DOOR_unlocked, (0,0)) #display unlocked door (phase = 5)

        #for bunker screens
    elif(view == "Bunker"):
        WIN.blit(BUNKER, (0,0)) #display Bunker image
    elif(view == "Bunker-held"):
        WIN.blit(BUNKER_held, (0,0)) #display bunker held closed image
    pygame.display.update()




def main():
    global view
    global fire
    global damper
    global window_phase
    global door_phase
    global holding

    #Functional Control logic initialization
    clock = pygame.time.Clock()
    day = '1' # ****DaySelect() when code is adjusted for day control****
    round_start = False

    SEC = 1000 # 1000 milliseconds
    num_seconds = 0 # number of seconds passed since the current day started
    next_second = SEC # next upcoming second in the day
    jiggle_timer = 0

    window = Window(day)

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

        #view + click control
        if view == "Home" and clicking and START_BUTTON.collidepoint(loc[0],loc[1]):
            view = "Game-load"
        elif view == "Game-load":
            pygame.time.wait(3000)
            view = 'Fireplace'

            # instatiate Window, Door, Fireplace, and Bunker objects
            window = Window(day)
            jiggle_timer = window.jiggle_time

            start_time = pygame.time.get_ticks()
            round_start = True
        
        elif (view == "Fireplace") and clicking:
            if(LOG.collidepoint(loc[0],loc[1])):
                if fire:
                    fire = False
                elif not damper == False:  #must add message to let the player know the damper must be open to turn on fire
                    fire = True
            elif (DAMPER.collidepoint(loc[0],loc[1])):
                if not fire:
                    if damper:
                        damper = False
                    else:
                        damper = True
            elif(FP_RIGHT.collidepoint(loc[0], loc[1])): #these next three sections need lots of control logic once the game functionality begins getting coded, this is just for movement control
                view = 'Window'
            elif(FP_LEFT.collidepoint(loc[0], loc[1])):
                view = "Door"
            elif(FP_DOWN.collidepoint(loc[0], loc[1])):
                view = "Bunker"
        elif (view == "Window") and clicking:
            if(WI_LEFT.collidepoint(loc[0], loc[1])): #this section needs control logic based on what view the fireplace screen should be
                view = "Fireplace"
            elif(WI_LOCK.collidepoint(loc[0], loc[1])):
                if(window_phase == 2):
                    window_phase = 1
                elif(window_phase == 3):
                    window_phase = 2
                elif(window_phase == 4): #unlocked
                    print('you\'re fucked, buddy')
                    #play error audiobite, as in you're already fucking and will be jumpscared within 5 seconds
        elif (view == "Door") and clicking:
            if(DOOR.collidepoint(loc[0], loc[1])):
                if(door_phase == 1):
                    view = "Door-locked1"
                elif(door_phase == 2):
                    view = "Door-locked2"
                elif(door_phase == 3):
                    view = "Door-locked3"
                elif(door_phase == 4):
                    view = "Door-locked4"
                elif(door_phase == 5):
                    view == "Door-unlocked"
            elif(DO_RIGHT.collidepoint(loc[0], loc[1])):
                view = "Fireplace-unlit-open" #Again needs control logic based on what the fireplace state is
        elif (view == "Door-locked1" or view == "Door-locked2" or view == "Door-locked3" or view == "Door-locked4" or view == "Door-unlocked") and (right_clicking or clicking):
            if (right_clicking):
                view = "Door"
            elif(clicking and not(view == "Door-unlocked")): #can relock door fully with click unless fully unlocked
                view = "Door-locked1"
        elif (view == "Bunker" or view == "Bunker-held") and clicking:
            if(BUNKER.collidepoint(loc[0], loc[1])):
                if(holding):
                    holding = False
                    view = "Bunker"
                else:
                    holding = True
                    view = "Bunker-held"
            elif(BU_DOWN.collidepoint(loc[0], loc[1])):
                if(holding):
                    view = "Bunker-held"
                else: #again control logic for phases and states of rooms is needed here
                    view = "Fireplace-unlit-open"


        if round_start:
            ticks = pygame.time.get_ticks() # number of ticks since pygame.init()

            if ticks - start_time > next_second:
                # print(jiggle_timer)
                next_second += SEC
                num_seconds += 1
                # print(num_seconds) # **temp commented out to test for hitbox barriers**

                jiggle_timer -= 1

                if(jiggle_timer == 0):
                    window_phase += 1
                    jiggle_timer = window.jiggle_time

                  

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
            
        draw_image() # update image every every event has been iterated through
        #print(pygame.mouse.get_pos())

if __name__ == "__main__":
    main()
