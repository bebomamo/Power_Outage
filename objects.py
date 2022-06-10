import random

class Window:
    def __init__(self, day):
        if(day == 1): self.jiggleTime = 90 + random.randrange(0,30,1) #attacked once but only once
        elif(day == 2): self.jiggleTime = 70 + random.randrange(0,30,1) #attacked once or twice but more likely once
        elif(day == 3): self.jiggleTime = 55 + random.randrange(0,20,1) #attacked twice but only twice
        elif(day == 4): self.jiggleTime = 45 + random.randrange(0,15,1) #attacked twice or 3 times but likely twice
        elif(day == 5): self.jiggleTime = 35 + random.randrange(0,10,1) #attacked three or four times
        elif(day == 6): self.jiggleTime = 25 + random.randrange(0,5,1) #attacked four or five times
        elif(day == 7): self.jiggleTime = 15 + random.randrange(0,5,1) #attacked seven to nine times

class Fireplace:
    def __init__(self, day):
        if(day == 1): self.climbdown = 600 #ten minutes
        elif(day == 2): self.climbdown = 267 + random.randrange(0,60,1) #50/50 attacked once or twice
        elif(day == 3): self.climbdown = 187 + random.randrange(0,40,1) #attacked twice and sometimes 3 times
        elif(day == 4): self.climbdown = 182 + random.randrange(0,14,1) #attacked three times no matter what
        elif(day == 5): self.climbdown = 147 + random.randrange(0,20,1) #50/50 attacked 3 or 4 times
        elif(day == 6): self.climbdown = 117 #attacked 5 times no matter what
        elif(day == 7): self.climbdown = 87 + random.randrange(0,20,1) #attacked 5 or 6 times

class Door:
    def __init__(self, day):
        if()
# note: FrontDoor, Bunker, and Fireplace (at least) will all be added once their attributes have been precisely defined
#       At this point, it seems like FrontDoor, Bunker, and Fireplace should all be classes and Fear should not,
#       although this may change.

#coordinate hitbox outlines
#Play button -> top left = (378, 46)
#            -> bottom left = (378, 460)
#            -> bottom right = (780, 460)
#            -> top right = (780, 46)

#Fireplace -> log top left  (343, 157)
#          -> log bottom left
#          -> log bottom right  (435, 175)
#          -> log top right
#         
#          -> damper tl  (325, 125)
#          -> damper bl  (325, 149)
#          -> damper br  (335, 149)
#          -> damper tr  (335, 125)
#
#          -> right tl  (831, 33)
#          -> right bl
#          -> right br  (875, 437)
#          -> right tr
#
#          -> left tl (17, 31)
#          -> left br (57, 439)
#
#          -> down tl (113, 435)
#          -> down br (787, 483)
#
#WINDOW
#          ->left left = 19
#          ->left top = 27
#          ->left width = 62
#          ->left height = 460
#
#          ->lock left = 489
#          ->lock top = 207
#          ->lock width = 68
#          ->lock height = 22
#
#DOOR
#          ->door left = 166
#          ->door top = 28
#          ->door width = 352
#          ->door height = 454
#
#          ->right left = 786
#          ->right top = 28
#          ->right width = 80
#          ->right height = 458
#
#BUNKER
#          ->bunker left = 112
#          ->bunker top = 34
#          ->bunker width = 642
#          ->bunker height = 312
#
#          ->down left = 112
#          ->down top = 422
#          ->down width = 644
#          ->down height = 43
#
#
#