from Myro import *
init("COM5")

def triangle():    
    turn_by(60)
    forward(2,1)
    turn_by(180)
    forward(2,1)
    turn_by(120)
    forward(2,1)
    
def sq(size):
    for i in range(1,5):
        forward(size,1)
        turnRight(.6,1)
 
def turn_by(deg):
    turnBy(deg,"deg") 
triangle()


sides = 3
