from Processing import *
window(300,500)
value = 0
colors = [[255,0,0],[0,128,0],[0,0,255],[0,0,0],[255,255,255],[128,0,128]]

def doMouseDragged():
    mouseClicked()
    print("drawing line")
 
    rect(100,100,10,10)


onMouseDragged += doMouseDragged

def mouseClicked(): 
    if isMousePressed() == True:
        whatColor()
        
def drawRects():
    for i in range(0,6):
        fill(colors[i][0],colors[i][1],colors[i][2])
        rect(i * 50,0,50,50)
        
def whatColor():
    if mouseY() <= 50:
        if mouseX() <= 50:
            print("color is red")
            fill(colors[0][0],colors[0][1],colors[0][2])
        elif mouseX() <= 100:
            print("color is green")
            fill(colors[1][0],colors[1][1],colors[1][2])
        elif mouseX() <= 150:
            print("color is blue")
            fill(colors[2][0],colors[2][1],colors[2][2])
        elif mouseX() <= 200:
            print("color is  black")
            stroke(colors[3][0],colors[3][1],colors[3][2])
        elif mouseX() <= 250:
            print("color is white")
            stroke(colors[4][0],colors[4][1],colors[4][2])
        elif mouseX() <= 300:
            print("color is purple")
            stroke(colors[5][0],colors[5][1],colors[5][2])
drawRects()
onMousePressed += doMouseDragged  



