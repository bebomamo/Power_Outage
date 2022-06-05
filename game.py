from pickle import TRUE
import pygame
import os
from HomeSelect import *

view = "Home"
WIDTH, HEIGHT = 900, 500 #subject to change
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Power Outage")
FPS = 60
#Objects and backgrounds
HomeDay = DaySelect()
HOME_image = pygame.image.load(os.path.join('Assets', HomeDay)) #adding image
HOME = pygame.transform.scale(HOME_image, (900, 500)) #image resizing

def draw_image():
    if(view == "Home"):
        WIN.blit(HOME, (0, 0)) #display home image
    """elif(view == "Window"):
        WIN.blit(WINDOW, (Window.x, Window.y)) #display window image
    elif(view == "Fireplace"):
        WIN.blit(FIREPLACE, (0,0)) #display Fireplace image
    elif(view == "Frontdoor"):
        WIN.blit(FRONTDOOR, (0,0)) #display Frontdoor image
    elif(view == "Bunker"):
        WIN.blit(BUNKER, (0,0)) #display Bunker image"""
    pygame.display.update()

def main():
    Window = pygame.Rect(200, 50, 100, 300) #Widthpos, Heightpos, Width, Height
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_image()
    pygame.quit()

if __name__ == "__main__":
    main()