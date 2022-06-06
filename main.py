#Ben Malone(bebomamo) & Jack Jameson
#6/2/2022 Start Date
#This section is for running the game, the timeline, and bookkeeping the .txt data that will hold the players in game progress.
import time
import os
import sys
import sysconfig
import math
import Window
# import FrontDoor
# import Fireplace
# import Fear
# import Bunker


# note: This file will not be used in the final version of the game, but will be kept as a 
#       reference until we know it is no longer needed. Print calls were added to avoid
#       empty if statement errors


def main():
#total day time is 10 minutes(600 seconds) for timing creation
#access .txt data file for information on what "day of the week" the player is on.

    day = 0
    play = 0
#test for which day to select proper "play day" button
#startup panoramic image with selectable objects in certain positions
#startup each section with day number parameter for difficulty timing selection
    if(day == 0): 
        #monday setup and game screen begin after "play day" select
        while play == 0:
            #if select object change play to 1
            time.sleep[1]
        W = Window(0)
        # F = FrontDoor(0)
        # Fp = Fireplace(0)
        # Fe = Fear(0)
        # B = Bunker(0)
        if((W == 1) or (F == 1) or (Fp == 1) or (Fe == 1) or (B == 1)):
            #any 1 return means that section killed the player
            day = 0
            #return to start screen
    if(day == 1):
        #tuesday setup and game screen begin after "play day" select
        print()
        
    if(day == 2):
        #wednesday setup and game screen begin after "play day" select
        print()
        
    if(day == 3):
        #thursday setup and game screen begin after "play day" select
        print()

    if(day == 4):
        #friday setup and game screen begin after "play day" select
        print()

    if(day == 5):
        #saturday setup and game screen begin after "play day" select
        print()

    if(day == 6):
        #sunday setup and game screen begin after "play day" select
        print()

#Allow for game restart, Select to play any Night, and to do bonus night(potentially add an easter egg here)
    if(day == 7):
        #alldays setup and game screen begin after "play day" select
        print()
    
    

    