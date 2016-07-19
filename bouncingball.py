from Processing import *
from random import *

xCoord = (.5 * width())
yCoord = (.5 * height())

def init():
    window(501,501)
    stroke(20,20,20)
    rect(0,0,400,400)
    strokeWeight(15)
    ellipse(xCoord, yCoord, 20, 20 )
def move1Direct(dire,num,speed):
    num = floor(num)
    if dire == "x" or dire == "X":
        global xCoord
        for i in range(0,floor(num)):
            delay(speed)
            background(255,255,255)
            point(  xCoord + i, yCoord )
        xCoord = xCoord + num
    elif dire == "y" or dire == "Y":
        global yCoord
        for i in range(0,floor(num)):
            delay(speed)
            background(255,255,255)
            point(  xCoord, yCoord + i)
        yCoord = yCoord + num
def move2Direct(xChange,yChange,speed):
    global xCoord,yCoord
    if xChange > yChange:
        num = xChange
    else:
        num = yChange
    for i in range(0,num):
        newX = xCoord + xChange
        newY = yCoord + yChange
        delay(speed)
        background(255,255,255)
        if newX <= xCoord or newY <= yCoord:
            if num == xChange:
                point(xCoord + i,yCoord)
                yCoord += 1
            else:
                point(xCoord,yCoord + i)
                xCoord += 1
        else:
            point(xCoord + i, yCoord + i)
            xCoord += 1
            yCoord += 1
        
        
def move3Direct(xChange,yChange,speed):
    global xCoord,yCoord
    print("start",xCoord,yCoord)
    newX = xCoord + xChange
    newY = yCoord + yChange
    if xChange > yChange:
        normal = xChange
        notNormal = yChange / xChange
    else:
        normal = yChange
        notNormal = xChange / yChange
    for i in range(0,normal):
        #delay(0)
        background(255,255,255)
        if normal == xChange:
            print("inloop",xCoord,yCoord)
            ellipse(xCoord + i, yCoord + (i * notNormal),5)
            xCoord += 1
            yCoord += notNormal
        else:
            print("inloop",xCoord,yCoord)
            ellipse(xCoord + (i * notNormal),yCoord + i,5)
            xCoord += notNormal
            yCoord += 1
        print(xCoord,yCoord)
        
init()
xChange = randrange(1,9)
print(xChange)

while xCoord <= 390.5:
    print("f")
    background(255,255,255)
    rect(0,0,400,400)
    ellipse(xCoord,yCoord, 20, 20)
    delay(10)
    xCoord += xChange
    yCoord += 1
    
    


