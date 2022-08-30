from game import WIN, WHITE, BLUE, GREEN, RED
import pygame, sys
# ---------------------------------------------------------------------------------------------------
# This module contains unfinished code that is currently not in use in the game, but may be completed
# at some point in the future.
# ---------------------------------------------------------------------------------------------------

# Function that controls the game's cutscene/dialogue screens
def cutscene(states: dict):
    dialogue = []

    if states.night == 1: dialogue = ['C> Child speaking', 'D> Dad speaking', 'M> Mom speaking', 'C> Child speaking again']
    elif states.night == 2: dialogue = ['C> Child speaking', 'D> Dad speaking', 'M> Mom speaking', 'C> Child speaking again']
    elif states.night == 3: dialogue = ['C> Child speaking', 'D> Dad speaking', 'M> Mom speaking', 'C> Child speaking again']
    elif states.night == 4: dialogue = ['C> Child speaking', 'D> Dad speaking', 'M> Mom speaking', 'C> Child speaking again']
    elif states.night == 5: dialogue = ['C> Child speaking', 'D> Dad speaking', 'M> Mom speaking', 'C> Child speaking again']
    elif states.night == 6: dialogue = ['C> Child speaking', 'D> Dad speaking', 'M> Mom speaking', 'C> Child speaking again']
    elif states.night == 7: dialogue = ['C> Child speaking', 'D> Dad speaking', 'M> Mom speaking', 'C> Child speaking again']

    position = (80, 120) # position on screen where text is to be displayed

    while dialogue:
        WIN.fill(WHITE)

        if dialogue[0][:2] == 'C>': display_text(dialogue[0][3:], BLUE, position)
        elif dialogue[0][:2] == 'D>': display_text(dialogue[0][3:], GREEN,  position)
        elif dialogue[0][:2] == 'M>': display_text(dialogue[0][3:], RED, position)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE: dialogue.pop(0)
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

# Function that displays the inputted message in the desired location on the screen
def display_text(message: str, color: str, loc: tuple):
    font = pygame.font.SysFont(None, 80)
    text = font.render(message, True, color)
    WIN.blit(text, loc)

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