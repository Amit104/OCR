# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 15:41:37 2017

@author: Axle
"""

import cv2
import numpy as np
from sklearn.cluster import KMeans
from matplotlib import pyplot as plt
from scipy.interpolate import interp1d

img = cv2.imread('D:/Study/ML/OCR/hh2.jpg',0)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
ret2,th2 = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
#cv2.imshow('image',th2)
#cv2.waitKey(0)  
#cv2.destroyAllWindows()
r = th2.shape[0]
c = th2.shape[1]
avg = []
print(r)
for i in range(r):
    rowsum = 0
    f= 0
    for j in range(c):
        if th2[i][j] == 0:
            rowsum = rowsum + 1
            f = 1
    avg.append(rowsum)
print(max(avg))
f = interp1d(range(r), avg)
plt.plot(range(r), avg,'o', range(r), f(range(r)), '-',)
plt.show()
avg = np.asarray(avg)
avg = np.reshape(avg,(-1,1))
kmeans = KMeans(n_clusters=3, random_state=0).fit(avg)
print(kmeans.cluster_centers_)
c = 0
for i in kmeans.labels_:
    if i==0:
        c = c+1
print(c)


        