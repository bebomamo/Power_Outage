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