from Processing import *
from random import *

#David Medina & Ayinde Eustache
window(500,500)
grid = []
def makeGrid():
    for i in range(0,10):
        for j in range(0,10):
            if j == 0:
                lst = [0]
            else:
                lst.append(0)
            rect(j * 50,i * 50,50,50)
        grid.append(lst)
def colorGrid():
    for i in range(0,len(grid)):
        for j in range(0,len(grid[0])):
            if grid[i][j] == 2:
                fill(0,0,0)
            elif grid[i][j] == 3:
                fill(255,255,0)
            else:
                fill(255,255,255)
            rect(j * 50,i * 50,50,50)
def checkRepeated(num,lst):
    for i in range(len(lst)):
        if(lst[i] == num):
            return True
    return False
makeGrid()
idx1 = randrange(len(grid[0]))
idx2 = randrange(len(grid[0]))

grid[idx1][idx2] = 1

shipCol = []
def setRandomShips():
    for i in range(7):
        num = randrange(0,len(grid[0]))
        while checkRepeated(num,shipCol):
            num = randrange(0,10)
        shipCol.append(num)    
guess = 0
print(idx1,idx2)

setRandomShips()
print(shipCol)
while guess != [idx1,idx2]:
    guess1 = int(raw_input("Enter first index:")) 
    guess2 = int(raw_input("Enter second index:"))
    
    guess = [guess1,guess2]
    if guess != [idx1,idx2]:
        print("Wrong Answer")
        grid[guess1][guess2] = 2
        colorGrid()
grid[idx1][idx2] = 3
colorGrid()
print("correct!")