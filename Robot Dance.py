from Myro import *
init("sim")

def shake(dire,sec,sp):
    if dire == "l":
        turnLeft(sec,sp)
        turnRight(sec,sp)
    else:
        turnRight(sec,sp)
        turnLeft(sec,sp)
def in_out(sec,sp):
    forward(sec,sp)
    backward(sec,sp)

for i in range(1,6):
    rotate(4,2.55)
    in_out(2,1)
    for j in range(1,4):
        shake("l",3,1)
        shake("r",3,2)
    turnRight(4,2.57)
    rotate(4,.55)
    

