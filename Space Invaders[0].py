#David Medina & Abdelrahman
from Processing import *
window(920,700) 
spaceShip=loadImage("Spaceship.png")
galaxy=loadImage("Galaxy.jpg")
global spaceLocX, spaceLocY
spaceLocX=420
frameRate(100)
spaceLocY=510
ballSpeed=10
global ballSpeed
alienHi = 60
alienWi = 60
rowNum = 5
colNum = 5
layerBgn = 0
layerEnd = (rowNum - 1)
direction = "right"
global layerEnd
def draw():
    while True:
        global spaceLocX, spaceLocY,direction
        spaceLocY=510
        ballX=spaceLocX+50
        if getX((layerEnd - 0),0) == 0:
            direction = "right"
            print(getX((layerEnd - 0),0) )
        elif getX(layerBgn,0) == 375:
            print(getX(layerBgn,0))
            direction = "left"
        if direction == "right":
            delay(250)
            image(galaxy,0,0,920,700)
            moveCol(0,25)
            moveCol(1,25)
            moveCol(2,25)
            moveCol(3,25)
            moveCol(4,25)
            image(spaceShip,spaceLocX,560,100,100)
            print("hi")
        elif direction == "left":
            delay(250)
            image(galaxy,0,0,920,700)
            moveCol(0,-25)
            moveCol(1,-25)
            moveCol(2,-25)
            moveCol(3,-25)
            moveCol(4,-25)
            image(spaceShip,spaceLocX,560,100,100)
            print("bye")
                
        if isKeyPressed() and 25<=spaceLocX and spaceLocX<=790:
            image(spaceShip,spaceLocX,560,100,100)
            if key()=='a' or key()=='Left':
                spaceLocX-=15                  
            elif key()=='d' or key()=='Right':
                spaceLocX+=15
            if key()=='space':
                ellipse(ballX,spaceLocY,5,30)
                while spaceLocY!=0:
                    spaceLocY-=ballSpeed 
                    ellipse(ballX,spaceLocY,5,30)
                    image(spaceShip,spaceLocX,560,100,100)
                    delay(1)
                    image(galaxy,0,0,920,700)
                    reDrawAliens()
                    if isKeyPressed()and 25<=spaceLocX and spaceLocX<=790:
                       if key()=='a' or key()=='Left':
                            spaceLocX-=15                  
                       elif key()=='d' or key()=='Right':
                            spaceLocX+=15
                    elif 25>spaceLocX:
                        if key()=='d' or key()=='Right':
                            spaceLocX+=15
                    elif spaceLocX>790:
                         if key()=='a' or key()=='Left':
                            spaceLocX-=15  

        elif 25>spaceLocX:
            if key()=='d' or key()=='Right':
                spaceLocX+=15
        elif spaceLocX>790:
             if key()=='a' or key()=='Left':
                spaceLocX-=15  
        #image(spaceShip,spaceLocX,560,100,100)
alienList = []
def setupAliens():
    for i in range(colNum):
        for j in range(rowNum): # will make aliens go right will create row
            img = loadImage("alien.png")
            if j == 0:
                alienLayer = [[img]]
            else:
                alienLayer.append([img])
            
            coordinates = [(j * alienWi) + (j * 60), (i * alienHi) + (i * 10)]
            alienLayer[j].append(coordinates)
            image(img,coordinates[0],coordinates[1],alienHi,alienWi)    
        alienList.append(alienLayer)
def getX(idx1,idx2):
    return alienList[idx1][idx2][1][0]
def getY(idx1,idx2):
    return alienList[idx1][idx2][1][1]
def getCoords(idx1,idx2):
    return [getX(idx1,idx2),getY(idx1,idx2)]
def getImg(idx1,idx2):
    return alienList[idx1][idx2][0]
def removeAlien(idx1,idx2):
    alienList[idx1][idx2][0] = None
def reDrawAliens():
    image(galaxy,0,0,920,700)
    for i in range(colNum):
        for j in range(rowNum):
            if alienList[i][j][0] is not None:
                image(getImg(i,j), getX(i,j),getY(i,j),alienHi,alienWi)
                delay(1)
def moveRow(rowNum,xChange,yChange):
    for j in range(len(alienList[rowNum])):
        alienList[rowNum][j][1][0] = (getX(rowNum,j) + xChange)
        alienList[rowNum][j][1][1] = (getY(rowNum,j) + yChange)
        delay(300)
        image(getImg(rowNum,j), getX(rowNum,j),getY(rowNum,j),alienHi,alienWi)
def moveCol(rowNum,xChange):
    for i in range(len(alienList[rowNum])):
        alienList[i][rowNum][1][0] = (getX(i,rowNum) + xChange)
        #alienList[j][rowNum][1][1] = (getY(rowNum,j) + yChange)
        image(getImg(i,rowNum), getX(i,rowNum),getY(i,rowNum),alienHi,alienWi)
setupAliens()
draw()
