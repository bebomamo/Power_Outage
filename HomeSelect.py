import os

#A file containing code to select which day to launch the game using file IO
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
