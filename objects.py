import random, pygame, os

# Function which calculates a valid jiggletime based on the inputted night
def get_jiggletime(night):
    if night == '1': return 90 + random.randrange(0,30,1) #attacked once but only once
    elif night == '2': return 70 + random.randrange(0,30,1) #attacked once or twice but more likely once
    elif night == '3': return 55 + random.randrange(0,20,1) #attacked twice but only twice
    elif night == '4': return 45 + random.randrange(0,15,1) #attacked twice or 3 times but likely twice
    elif night == '5': return 35 + random.randrange(0,10,1) #attacked three or four times
    elif night == '6': return 25 + random.randrange(0,5,1) #attacked four or five times
    elif night == '7': return 15 + random.randrange(0,5,1) #attacked seven to nine times

# Class which contains every game state, initialized with the default values listed below
class States:
    def __init__(self, night=None, view=None, playing=None, paused=None, next_second=None, 
    num_seconds=None, fire=None, damper=None, window_phase=None, door_phase=None, holding=None, jiggle_time=None):
        if night is None: night = '1'
        self.night = night

        if view is None: view = 'Home'
        self.view = view

        if playing is None: playing = False
        self.playing = playing

        if paused is None: paused = False
        self.paused = paused

        if next_second is None: next_second = 1000
        self.next_second = next_second

        if num_seconds is None: num_seconds = 0
        self.num_seconds = num_seconds

        if fire is None: fire = False
        self.fire = fire

        if damper is None: damper = False
        self.damper = damper

        if window_phase is None: window_phase = 1
        self.window_phase = window_phase

        if door_phase is None: door_phase = 1
        self.door_phase = door_phase

        if holding is None: holding = False
        self.holding = holding

        if jiggle_time is None: jiggle_time = get_jiggletime(self.night)
        self.jiggle_time = jiggle_time

        self.jiggle_countdown = jiggle_time

class Button(pygame.sprite.Sprite):
    def __init__(self, image: str, pos_x: int, pos_y: int):
        super().__init__()
        self.image = pygame.image.load(os.path.join('assets', image)).convert_alpha()
        self.rect = self.image.get_rect(x=pos_x, y=pos_y)

# class Fireplace:
#     def __init__(self, day):
#         if(day == '1'): self.climbdown = 600 #ten minutes
#         elif(day == '2'): self.climbdown = 267 + random.randrange(0,60,1) #50/50 attacked once or twice
#         elif(day == '3'): self.climbdown = 187 + random.randrange(0,40,1) #attacked twice and sometimes 3 times
#         elif(day == '4'): self.climbdown = 182 + random.randrange(0,14,1) #attacked three times no matter what
#         elif(day == '5'): self.climbdown = 147 + random.randrange(0,20,1) #50/50 attacked 3 or 4 times
#         elif(day == '6'): self.climbdown = 117 #attacked 5 times no matter what
#         elif(day == '7'): self.climbdown = 87 + random.randrange(0,20,1) #attacked 5 or 6 times