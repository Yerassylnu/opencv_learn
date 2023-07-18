import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
#cv.imshow('Blank', blank)

#1. paint the image a certain color
#blank[200:300, 300:400] = 0,0,255
#cv.imshow('Green', blank)

#2. Draw A Rectangle
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=cv.FILLED)
#cv.imshow('Rectangle', blank)

#3. Draw A Circle
cv.circle(blank, (250,250), 40, (0,0,255), thickness=-1 )
#cv.imshow('Circle', blank)

#4. Draw A Line
cv.line(blank, (100,250), (300,400), (255,255,0), thickness=3)
#cv.imshow('Line', blank)

#5. Write text 
cv.putText(blank, 'Hello, my name is Yerasyl', (15,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (66,90,0), 2)
cv.imshow('Text', blank)

cv.waitKey(0)