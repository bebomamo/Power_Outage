class Window:
    def __init__(self, jiggletime):
        self.jiggletime = jiggletime

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

