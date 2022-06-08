from pickle import FALSE, TRUE
import pygame, os, sys, objects

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

pygame.init() # start pygame

# Window setup
WIDTH, HEIGHT = 900, 500 #subject to change
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
WIN.fill(WHITE) # set to white so we remember it exists, will almost certainly be changed later
pygame.display.set_caption("Power Outage")

# --------initialization nation--------
view = "Home"
FPS = 60
# Objects and backgrounds
# HomeDay = DaySelect() # - commented out for now
HOME_image = pygame.image.load(os.path.join('assets', 'PO_night1.PNG')).convert() #adding image
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

def draw_image():
    if(view == "Home"):
        WIN.blit(HOME, (0, 0)) #display home image
    elif(view == "Game-load"):
        WIN.blit(LOAD, (0, 0)) # temporary

    # elif(view == "Window"):
    #     WIN.blit(WINDOW, (Window.x, Window.y)) #display window image

    elif(view == "Fireplace-start"):
        WIN.blit(FIREPLACE_unlit_open, (0,0)) #display Fireplace starting image

    # elif(view == "Frontdoor"):
    #     WIN.blit(FRONTDOOR, (0,0)) #display Frontdoor image
    # elif(view == "Bunker"):
    #     WIN.blit(BUNKER, (0,0)) #display Bunker image

    pygame.display.update()


def main():
    global view
    # initialization nation
    clock = pygame.time.Clock()
    day = 1 # DaySelect()
    RoundStart = False

    SEC = 1000 # 1000 milliseconds
    num_seconds = 0 # number of seconds passed since the current day started
    next_second = SEC # next upcoming second in the day

    clicking = False
    right_clicking = False

    START_BUTTON_X_MIN = 378
    START_BUTTON_X_MAX = 780
    START_BUTTON_Y_MIN = 46
    START_BUTTON_Y_MAX = 460

    # stuff that happens while the game is running
    while True:
        clock.tick(FPS)

        mx, my = pygame.mouse.get_pos() # gets mouse's x and y coordinates
        loc = [mx, my] # mouse location

        in_start_range_x = loc[0] >= START_BUTTON_X_MIN and loc[0] <= START_BUTTON_X_MAX
        in_start_range_y = loc[1] >= START_BUTTON_Y_MIN and loc[1] <= START_BUTTON_Y_MAX

        if view == "Home" and clicking and in_start_range_x and in_start_range_y:
            view = "Game-load"
        elif view == "Game-load":
            pygame.time.wait(3000)
            view = 'Fireplace-start'
            start_time = pygame.time.get_ticks()
            RoundStart = True

        if RoundStart:
            ticks = pygame.time.get_ticks() # number of ticks since pygame.init()
            if ticks - start_time > next_second:
                next_second += SEC
                num_seconds += 1
                print(num_seconds)

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

if __name__ == "__main__":
    main()
