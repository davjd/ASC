#David Medina 

from Processing import *
from random import *

#initialize the lab
window(500,500)
rect(0,0,400,400)
#initialize the ball
xCoord = .5 * width()
yCoord = .5 * height()
strokeWeight(20)
point(xCoord,yCoord)

#variables needed for movement
#direction for x and y. Either inc, increase (move down), or dec, decrease (mov up).
xDirect = ""
yDirect = ""
#the change done to the coordinates of the point. It will be chose randomly.
xChange = randrange(-15,15)
yChange = randrange(-15,15)
#this variable needs to be global so it can be set and reffered to in multiple functions. For now let it hold nothing.
change = 0

#function that takes in "x" for xCoordinate change, or "y" for yCoordnate change. Will ultimately make a new change.
def getChange(coord):
    global change
    change = randrange(-15,15)
    while change == 0:
        change = randrange(-15,15) #loop needed so the change is not zero, so it always move diagonally
    checkChange(coord)
#function that will set the direction of the ball and the change of the ball, depending on what coordinate ( x or y) youu want to change
def checkChange(coord):
    global change,xChange,yChange,xDirect,yDirect
    if change < 0:
        if coord == "x" or coord == "X":
            xChange = abs(change)
            xDirect = "dec"
        else:
            yChange = abs(change)
            yDirect = "dec"     
    else:
        if coord == "x" or coord == "X":
            xChange = change
            xDirect = "inc"
        else:
            yChange = change
            yDirect = "inc"
#lets set the changes that will be done to the xCoordinates and yCoorinates, Will never be zero!      
getChange("x")
getChange("y")

#this is where the fun begins ...
while True:
    # in order to erase the trails left behind, by the moving circle, we must change the background to white, but then recreate the origial rectangel.
    #but we unfortunately also need a delay, because thats how computers are!
    delay(1)
    background(255,255,255)
    strokeWeight(1)
    rect(0,0,400,400)
    #the ifs will check if the xCoords and yCoords are in the boundaires, if not make it go teh opposite way
    if xCoord > 7 and xCoord < 390:
        if xDirect == "inc":
            xCoord += xChange
        else:
            xCoord -= xChange
    if yCoord > 10 and yCoord < 390:
        if yDirect == "inc":
            yCoord +=yChange
        else:
            yCoord -= yChange
    #these ifs shall only be met when the ball is out of the boundary.
    #if so, we must get a new random number to be the change. Thats why we will use the getChange() function.
    if xCoord <= 7:
        getChange("x")
        xDirect = "inc"
        xCoord += xChange
    elif xCoord >= 390:
        getChange("x")
        xDirect = "dec"
        xCoord -= xChange
            
    if yCoord <= 10:
        getChange("y")
        yDirect = "inc"
        yCoord += yChange
    elif yCoord >= 390:
        getChange("y")
        yDirect = "dec"
        yCoord -= yChange
    #not move the ball, by recreating the bal in another coordinate.
    #strokeWeight determines the size of the ball. 20 seems like a reasonable size!
    strokeWeight(20)
    point(xCoord,yCoord)   