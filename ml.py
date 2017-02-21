# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 15:41:37 2017

@author: Axle
"""

from initialisations import *
from denoise import *
from lineSegment import *

def showImg(th2):
    cv2.imshow('image',th2)
    cv2.waitKey(0)  
    cv2.destroyAllWindows()
    
img = cv2.imread('D:/Study/ML/OCR/hh2.jpg',0)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
ret2,th2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
r = th2.shape[0]
c = th2.shape[1]
avg = []
for i in range(r):
    rowsum = 0
    f= 0
    for j in range(c):
        if th2[i][j] == 0:
            rowsum = rowsum + 1
            f = 1
    avg.append(rowsum)
f = interp1d(range(r), avg)
plt.plot(range(r), avg,'o', range(r), f(range(r)), '-',)
plt.show()

brkpts = [11,30,50,70,90,109,129,150,168,188,208,226]
brkpts2 = [115,357,532,677,834,1022,1221,1385,1590,1827,2056,2219,2389,2570,2782]
brkpts3 = [105,285,446,671]
LineSeg(th2,r,c,brkpts2,15)