#David Medina and David Jones
from Myro import *

# set colors needed.
ObamaYellow = makeColor(252,227,166)
ObamaBlue = makeColor(112,150,158)
ObamaRed = makeColor(217,26,33)
ObamaDarkBlue = makeColor(0,51,76)


#the function pickAFile() will ask you to pick a file, and will return directory, so we sotre that in a variable
myFile=pickAFile()
# makePicture will get the data of the picture, using the directory
pict=makePicture(myFile)
#show() not  needed, but its good to check the picture
show(pict)
pixels = getPixels(pict)

#check pixel by pixel and check the gray values and make decisions.
for pixel in pixels:
    grayValue = getGray(pixel)
    if grayValue > 180:
        setColor(pixel,ObamaYellow)
    elif grayValue > 120:
        setColor(pixel,ObamaBlue)
    elif grayValue > 60:
        setColor(pixel,ObamaRed)
    else:
        setColor(pixel,ObamaDarkBlue)
