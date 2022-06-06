from pickle import TRUE
import pygame, os, sys, objects

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

pygame.init() # start pygame

# Window setup
WIDTH, HEIGHT = 900, 500 #subject to change
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
WIN.fill(WHITE) # set to white so we remember it exists, will almost certainly be changed later
pygame.display.set_caption("Power Outage")

# --------initialization--------
view = "Home"
FPS = 60
# Objects and backgrounds
# HomeDay = DaySelect() # - commented out for now
HOME_image = pygame.image.load(os.path.join('assets', 'PO_night1.PNG')) #adding image
HOME = pygame.transform.scale(HOME_image, (WIDTH, HEIGHT)) #image resizing
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
    if(view == "Game"):
        WIN.fill(BLUE) # temporary

    # elif(view == "Window"):
    #     WIN.blit(WINDOW, (Window.x, Window.y)) #display window image
    # elif(view == "Fireplace"):
    #     WIN.blit(FIREPLACE, (0,0)) #display Fireplace image
    # elif(view == "Frontdoor"):
    #     WIN.blit(FRONTDOOR, (0,0)) #display Frontdoor image
    # elif(view == "Bunker"):
    #     WIN.blit(BUNKER, (0,0)) #display Bunker image

    pygame.display.update()


def main():
    # initialization nation
    Window = pygame.Rect(200, 50, 100, 300) #Widthpos, Heightpos, Width, Height
    clock = pygame.time.Clock()
    day = 1 # DaySelect()
    global view

    clicking = False
    right_clicking = False

    # stuff that happens while the game is running
    while True:
        clock.tick(FPS)

        mx, my = pygame.mouse.get_pos() # gets mouse's x and y coordinates
        loc = [mx, my] # mouse location

        START_BUTTON_X_MIN = 378
        START_BUTTON_X_MAX = 780
        START_BUTTON_Y_MIN = 46
        START_BUTTON_Y_MAX = 460

        in_start_range_x = loc[0] >= START_BUTTON_X_MIN and loc[0] <= START_BUTTON_X_MAX
        in_start_range_y = loc[1] >= START_BUTTON_Y_MIN and loc[1] <= START_BUTTON_Y_MAX

        if view == "Home" and clicking and in_start_range_x and in_start_range_y:
            view = "Game"
        elif view == "Game" and clicking:
            view = "Home"

        clicking = False # one click allowed per frame - probably a temporary solution
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # left clicking
                    clicking = True
                if event.button == 3: # right clicking
                    right_clicking = True
            
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    clicking = False
                if event.button == 3:
                    right_clicking = False
            
        draw_image() # update image every every event has been iterated through

if __name__ == "__main__":
    main()
