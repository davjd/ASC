#david Medina
"""myFirstList = ["hi","yeah","x",2.2]
myFirstList[3] = "wooo"
myFirstList.append(3)
print(myFirstList)"""

#question 1
def _10To20():
    lst = []
    for i in range(10,21):
        lst.append(i)
        return lst
#question 2
def empty5():
    lst = []
    for i in range(1,6):
        lst.append(0)
    return lst
#question 3
def empyLst():
    return []
#question 4
def getLen(lst):
    return len(lst)
#question 5
def getLenQ5():
    return len(["a",5,"doodle",3,10])
# question 6
def removeItm3():
    del ["a",5,"doodle",3,1][2]

# questoin 7
lst = [1]
lst.append(2)

#questoin 8
lst = ["a",5,"doodle",3,10]
lst[0] = 8.4

#question 9
def appendBegin(lst,itm):
    newLst = [itm]
    for i in lst:
        newLst.append(i)
    return newLst
print(appendBegin(lst,3))
    
# question 10
def addOdd():
    lst = []
    for i in range(1,11):
        if i % 2 != 0:
            lst.append(i)
    return lst
print(addOdd())


