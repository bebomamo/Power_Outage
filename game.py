import pygame, os, sys, objects

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

pygame.init() # start pygame

# Window setup
WIDTH, HEIGHT = 900, 500 #subject to change
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
WIN.fill(WHITE) # set to white so we remember it exists, will almost certainly be changed later
pygame.display.set_caption("Power Outage")

#---------Home Screen Startup control logic---------- Temporarily commented out
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
#     f.close
# --------initialization nation--------
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
        WIN.blit(LOAD, (0, 0)) # temporary

         #for window screens
    elif(view == "Window-locked1"):
        WIN.blit(WINDOW_locked1, (0, 0)) #display fully locked window phase (phase = 1)
    elif(view == "Window-locked2"):
        WIN.blit(WINDOW_locked2, (0,0)) #display second phase locked window (phase = 2)
    elif(view == "Window-locked3"):
        WIN.blit(WINDOW_locked3, (0,0)) #display third phase locked window (phase = 3)
    elif(view == "Window-unlocked"):
        WIN.blit(WINDOW_unlocked, (0,0)) #display window unlocked (phase = 4)

        #for fireplace screens
    elif(view == "Fireplace-unlit-open"):
        WIN.blit(FIREPLACE_unlit_open, (0,0)) #display unlit open damper fireplace
    elif(view == "Fireplace-lit-open"):
        WIN.blit(FIREPLACE_lit_open, (0,0)) #display lit open damper fierplace
    elif(view == "Fireplace-unlit-closed"):
        WIN.blit(FIREPLACE_unlit_closed, (0,0)) #display unlit closed damper fireplace

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
    # initialization nation
    clock = pygame.time.Clock()
    day = 1 # ****DaySelect() when code is adjusted for day control****
    RoundStart = False

    SEC = 1000 # 1000 milliseconds
    num_seconds = 0 # number of seconds passed since the current day started
    next_second = SEC # next upcoming second in the day
    fire = False
    damper = False #False is open damper, True is closed
    clicking = False
    right_clicking = False

    START_BUTTON_X_MIN = 378
    START_BUTTON_X_MAX = 780
    START_BUTTON_Y_MIN = 46
    START_BUTTON_Y_MAX = 460
    FP_LOG_X_MIN = 343
    FP_LOG_X_MAX = 435
    FP_LOG_Y_MIN = 157
    FP_LOG_Y_MAX = 175
    FP_DAMPER_X_MIN = 325
    FP_DAMPER_X_MAX = 335
    FP_DAMPER_Y_MIN = 125
    FP_DAMPER_Y_MAX = 149
    FP_RIGHT_X_MIN = 831
    FP_RIGHT_X_MAX = 875
    FP_RIGHT_Y_MIN = 33
    FP_RIGHT_Y_MAX = 437
    FP_LEFT_X_MIN = 17
    FP_LEFT_X_MAX = 57
    FP_LEFT_Y_MIN = 31
    FP_LEFT_Y_MAX = 439
    FP_DOWN_X_MIN = 113
    FP_DOWN_X_MAX = 787
    FP_DOWN_Y_MIN = 435
    FP_DOWN_Y_MAX = 483

    # stuff that happens while the game is running
    while True:
        clock.tick(FPS)

        mx, my = pygame.mouse.get_pos() # gets mouse's x and y coordinates
        loc = [mx, my] # mouse location

        #Click barrier control logic, only executes relevant range selection code based on what "view" player is in
        if (view == "Home"):
            in_start_range = loc[0] >= START_BUTTON_X_MIN and loc[0] <= START_BUTTON_X_MAX and loc[1] >= START_BUTTON_Y_MIN and loc[1] <= START_BUTTON_Y_MAX #cleaned to 1 line range
        if (view == "Fireplace-unlit-open" or view == "Fireplace-lit-open" or view == "Fireplace-unlit-closed"):
            in_damper_range = loc[0] >= FP_DAMPER_X_MIN and loc[0] <= FP_DAMPER_X_MAX and loc[1] >= FP_DAMPER_Y_MIN and loc[1] <= FP_DAMPER_Y_MAX
            in_log_range = loc[0] >= FP_LOG_X_MIN and loc[0] <= FP_LOG_X_MAX and loc[1] >= FP_LOG_Y_MIN and loc[1] <= FP_LOG_Y_MAX
            in_right_range = loc[0] >= FP_RIGHT_X_MIN and loc[0] <= FP_RIGHT_X_MAX and loc[1] >= FP_RIGHT_Y_MIN and loc[1] <= FP_RIGHT_Y_MAX
            in_left_range = loc[0] >= FP_LEFT_X_MIN and loc[0] <= FP_LEFT_X_MAX and loc[1] >= FP_LEFT_Y_MIN and loc[1] <= FP_LEFT_Y_MAX
            in_down_range = loc[0] >= FP_DOWN_X_MIN and loc[0] <= FP_DOWN_X_MAX and loc[1] >= FP_DOWN_Y_MIN and loc[1] <= FP_DOWN_Y_MAX

        #view + click control
        if view == "Home" and clicking and in_start_range:
            view = "Game-load"
        elif view == "Game-load":
            pygame.time.wait(3000)
            view = 'Fireplace-unlit-open'
            start_time = pygame.time.get_ticks()
            RoundStart = True
        elif (view == "Fireplace-unlit-open" or view == "Fireplace-lit-open" or view == "Fireplace-unlit-closed") and clicking:
            if(in_log_range):
                if(fire):
                    fire = False
                    view = "Fireplace-unlit-open"
                elif(damper == False):  #must add message to let the player know the damper must be open to turn on fire
                    fire = True
                    view = "Fireplace-lit-open"
            elif(in_damper_range):
                if(damper):
                    damper = False
                    view = "Fireplace-unlit-open"
                elif(fire == False):
                    damper = True
                    view = "Fireplace-unlit-closed"
            elif(in_right_range): #these next three sections need lots of control logic once the game functionality begins getting coded, this is just for movement control
                view = "Window-locked1"
            elif(in_left_range):
                view = "Door"
            elif(in_down_range):
                view = "Bunker"


        if RoundStart:
            ticks = pygame.time.get_ticks() # number of ticks since pygame.init()
            if ticks - start_time > next_second:
                next_second += SEC
                num_seconds += 1
                # print(num_seconds) **temp commented out to test for hitbox barriers**

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
        print(pygame.mouse.get_pos())
if __name__ == "__main__":
    main()
