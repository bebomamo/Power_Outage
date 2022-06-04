#Ben Malone & Jack Jameson
import math
import random
import os
import sys
import sysconfig
#jiggleTime is in seconds, 4 jiggles until unlock
def Window(day):
    jiggleTime = 0
    if(day == 0): 
        jiggleTime = random.sample(range(1,30),90) #attacked once but only once
    if(day == 1):
        jiggleTime = random.sample(range(1,30),70) #attacked once or twice but more likely once
    if(day == 2):
        jiggleTime = random.sample(range(1,20),55) #attacked twice but only twice
    if(day == 3):
        jiggleTime = random.sample(range(1,20),45) #attacked twice or 3 times but likely twice
    if(day == 4):
        jiggleTime = random.sample(range(1,10),35) #attacked three or four times
    if(day == 5):
        jiggleTime = random.sample(range(1,10),25) #attacked four or five times
    if(day == 6):
        jiggleTime = random.sample(range(1,5),15) #attacked seven to nine times
    if(day == 7):
        jiggleTime = random.sample(range(1,5),10) #attacked ten to sixteen times
    tempJiggle = jiggleTime
    stage = 0
    for time in 600:
        time.sleep[1]
        if tempJiggle == 0:
            #play jiggle soundbite
            stage = stage + 1
            tempJiggle == jiggleTime
            if (stage == 4):
                #play window unlock soundbite
                time.sleep[3]
                #player death from window
                return 1
        else:
            tempJiggle = tempJiggle - 1
    return 0