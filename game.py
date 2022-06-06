from pickle import TRUE
import pygame
import os
import objects

WHITE = (255, 255, 255)

pygame.init() # start pygame

# Window setup
WIDTH, HEIGHT = 900, 500 #subject to change
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
WIN.fill(WHITE) # set to white so we remember it exists, will almost certainly be changed later
pygame.display.set_caption("Power Outage")


# note: I moved DaySelect from its own file to here because it is only one function. For organization's 
#       sake it's probably better to not create an entire file for a single function, as doing so would
#       quickly crowd the repository and is not really convention in Python. 
def DaySelect():
    f = open("day.txt", mode = 'r')
    day = f.read(1)
    if(day == '0'): 
        return 'PO_night1.PNG'
    if(day == '1'):
        return 'PO_night2.PNG'
    if(day == '2'):
        return 'PO_night3.PNG'
    if(day == '3'):
        return 'PO_night4.PNG'
    if(day == '4'):
        return 'PO_night5.PNG'
    if(day == '5'):
        return 'PO_night6.PNG'
    if(day == '6'):
        return 'PO_night7.PNG'
    f.close

def draw_image():
    if(view == "Home"):
        WIN.blit(HOME, (0, 0)) #display home image
    
    # elif(view == "Window"):
    #     WIN.blit(WINDOW, (Window.x, Window.y)) #display window image
    # elif(view == "Fireplace"):
    #     WIN.blit(FIREPLACE, (0,0)) #display Fireplace image
    # elif(view == "Frontdoor"):
    #     WIN.blit(FRONTDOOR, (0,0)) #display Frontdoor image
    # elif(view == "Bunker"):
    #     WIN.blit(BUNKER, (0,0)) #display Bunker image

    pygame.display.update()

# --------initialization--------
view = "Home"
FPS = 60
# Objects and backgrounds
HomeDay = DaySelect()
HOME_image = pygame.image.load(os.path.join('Assets', HomeDay)) #adding image
HOME = pygame.transform.scale(HOME_image, (WIDTH, HEIGHT)) #image resizing
# ------------------------------

def main():
    # initialization nation
    Window = pygame.Rect(200, 50, 100, 300) #Widthpos, Heightpos, Width, Height
    clock = pygame.time.Clock()
    run = True
    day = DaySelect()
    
    # stuff that happens while the game is running
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False # exit while loop
        
        draw_image() # update image every every event has been iterated through
        #print (pygame.mouse.get_pos()) #prints mouse position for object creation (comment out if not using)

    pygame.quit()

if __name__ == "__main__":
    main()
