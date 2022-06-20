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

# Function that returns the climbdown time for the fireplace
def get_climbdown(night):
    if night == '1': return 600 #ten minutes (never attacks night 1)
    elif night == '2': return 267 + random.randrange(0,60,1) #50/50 attacked once or twice
    elif night == '3': return 187 + random.randrange(0,40,1) #attacked twice and sometimes 3 times
    elif night == '4': return 182 + random.randrange(0,14,1) #attacked three times no matter what
    elif night == '5': return 147 + random.randrange(0,20,1) #50/50 attacked 3 or 4 times
    elif night == '6': return 117 #attacked 5 times no matter what
    elif night == '7': return 87 + random.randrange(0,20,1) #attacked 5 or 6 times

# Function that returns when door lockpicked phase based on input night
# All attack timings are very similar to jiggletime, however attacks happen on average 10 seconds more frequently since there are more door phases
def get_locktime(night):
    if night == '1': return 80 + random.randrange(0,30,1) 
    elif night == '2': return 60 + random.randrange(0,30,1) 
    elif night == '3': return 45 + random.randrange(0,20,1) 
    elif night == '4': return 35 + random.randrange(0,15,1) 
    elif night == '5': return 25 + random.randrange(0,10,1) 
    elif night == '6': return 15 + random.randrange(0,5,1) 
    elif night == '7': return 5 + random.randrange(0,5,1)

# Function that determines when the bunker man will attack, attacks begin night 3 and are more frequent after the first attack.
# The first attack can also be slowed by checking the bunker door which will be very useful in later nights, this logic will be implemented in game.py however
# This function will simply give a base attack time that is similar to climbdown based again upon the input night
def get_bunkerwalk(night):
    if night == '1': return 601 #no attacking night 1
    elif night == '2': return 601 #no attacking night 2
    elif night == '3': return 267 + random.randrange(0,60,1) #50/50 attacked once or twice
    elif night == '4': return 187 + random.randrange(0,40,1) #attacked twice and sometimes 3 times
    elif night == '5': return 182 + random.randrange(0,14,1) #attacked three times no matter what
    elif night == '6': return 147 + random.randrange(0,20,1) #50/50 attacked 3 or 4 times
    elif night == '7': return 117 #attacked 5 times no matter what


# Class which contains every game state, initialized with the default values listed below
class States:
    def __init__(self, night=None, view=None, playing=None, paused=None, next_second=None, 
    num_seconds=None, fire=None, damper=None, window_phase=None, door_phase=None, holding=None, jiggle_time=None, 
    climbdown_time=None, lock_time=None, bunkerwalk_time=None):
        # Game states
        if night is None: night = '1'
        self.night = night

        if view is None: view = 'Home'
        self.view = view

        if playing is None: playing = False
        self.playing = playing

        if paused is None: paused = False
        self.paused = paused

        # Time states
        if next_second is None: next_second = 1000
        self.next_second = next_second

        if num_seconds is None: num_seconds = 0
        self.num_seconds = num_seconds

        # Window states
        if window_phase is None: window_phase = 1
        self.window_phase = window_phase

        if jiggle_time is None: jiggle_time = get_jiggletime(self.night)
        self.jiggle_time = jiggle_time

        self.jiggle_countdown = jiggle_time

        # Fireplace states
        if fire is None: fire = False
        self.fire = fire

        if damper is None: damper = False
        self.damper = damper

        if climbdown_time is None: climbdown_time = get_climbdown(self.night)
        self.climbdown_time = climbdown_time

        self.climbdown_countdown = climbdown_time

        # Door states
        if door_phase is None: door_phase = 1
        self.door_phase = door_phase

        if lock_time is None: lock_time = get_locktime(self.night)
        self.lock_time = lock_time

        self.lock_countdown = lock_time

        # Bunker states
        if holding is None: holding = False
        self.holding = holding

        if bunkerwalk_time is None: bunkerwalk_time = get_bunkerwalk(self.night)
        self.bunkerwalk_time = bunkerwalk_time

        self.bunkerwalk_countdown = bunkerwalk_time

class Button(pygame.sprite.Sprite):
    def __init__(self, image: str, pos_x: int, pos_y: int):
        super().__init__()
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.image = pygame.image.load(os.path.join('assets', image)).convert_alpha()
        self.rect = self.image.get_rect(x=pos_x, y=pos_y)
    
    def draw():
        pass
    
    def is_mouse_over():
        pass
