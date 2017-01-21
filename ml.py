# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 15:41:37 2017

@author: Axle
"""

from initialisations import *
from denoise import *
from lineSegment import *

def getSum(r,c,IM):
    sum1 = []
    for i in range(r):
        rowsum = 0
        for j in range(c):
            if IM[i][j] == 0:
                rowsum = rowsum + 1
        sum1.append(rowsum)
        
        
def showImage(x):
    cv2.imshow('image',x)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


img = cv2.imread('D:/Study/ML/OCR/hh2.jpg',0)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
ret2,IM = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

r = IM.shape[0]
c = IM.shape[1]

sum1 = getSum(r,c,IM)
f = interp1d(range(r), sum1)

x = range(r)
y = sum1

plt.plot(range(r), sum1,'o', range(r), f(range(r)), '-',)
plt.show()