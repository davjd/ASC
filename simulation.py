from Myro import *
init("sim")

def triangle():    
    turn_by(60)
    forward(2,1)
    turn_by(120)
    forward(2,1)
    turn_by(120)
    forward(2,1)
    
def sq(size,speed):
    for i in range(1,5):
        forward(size,speed)
        turn_by(90)
 
def turn_by(deg):
    turnBy(deg,"deg") 
def poly(sides):
    angle = ((sides - 2) * 180)/ sides
    for i in range(1,5):
        forward(2,1)
        turn_by(angle)
sz = int(input("Please input size:"))
sp = int(input("Please input speed:"))
penDown()
sq(sz,sp)


    