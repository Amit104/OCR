# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 19:17:25 2017

@author: Axle
"""

from initialisations import *

def getNodeNumber(r, c, x, y):
    return int((x * c) + y + 1)
        
diction = {}
pathList = []

            
def startBFSandReturnPathList(IM, r, c, brkPts, size):
    for i in range(r):
        for j in range(c):
            diction[getNodeNumber(r, c, i, j)] = [i, j, -1, -1]
    
    for i in range(1, size):
        bfs(IM, getNodeNumber(r, c, (brkPts[i - 1] + brkPts[i]) / 2 , 0), brkPts[i - 1], brkPts[i], r, c)
        pathList.append(getPath(getNodeNumber(r, c, (brkPts[i - 1] + brkPts[i]) / 2 , c - 1)))
    
    
def LineSeg(IM, r, c, brkPts, size):
    startBFSandReturnPathList(IM, r, c, brkPts, size)
    #first row
    
    for i in range(1,size-1):
        #above
        currPath = pathList[i]
        for j in currPath:
            x = diction[j][0]
            y = diction[j][1]
            print(IM[x][y])
        prevPath = pathList[i-1]
        mini = prevPath[len(prevPath) - 2]
        maxi = currPath[len(currPath) - 1]
        
        #initialise temporary image
        imag = []  
        for j in range(maxi-mini+1):                               
            il = []         
            for k in range (c):            
                il.append(0)      
            imag.append(il) 
            
        for j in prevPath[:-2]:
            for k in range(mini,diction[j][0]+1):
                imag[k-mini][diction[j][1]] = 255
            
        for j in currPath[:-2]:
            for k in range(diction[j][0],maxi+1):
                imag[k-mini][diction[j][1]] = 255
        
        for j in range (maxi-mini+1):                                
            for k in range (c):     
                if imag[j][k]==0:
                    imag[j][k]=IM[j+mini][k] 
           
        imag = np.array(imag,dtype=np.uint8)
        
        cv2.imshow('image',imag)
        cv2.waitKey(0)  
        cv2.destroyAllWindows()
    #last row

def bfs(IM, start, x1, x2, r, c):
    x = diction[start][0]
    y = diction[start][1]
    diction[start][2] = -1;
    diction[start][3] = 1;
    vertQueue = Queue()
    vertQueue.enqueue(start)
    while (vertQueue.size() > 0):
        current = vertQueue.dequeue()
        x = diction[current][0]
        y = diction[current][1]
        
        #right node
        if x + 1 <= x2 and IM[x + 1][y] == 255:
            neighbour = getNodeNumber(r,c,x + 1, y)
            if diction[neighbour][3] == -1:
                diction[neighbour][3] = 1
                diction[neighbour][2] = current
                vertQueue.enqueue(neighbour)
        
        #left node
        if x - 1 >= x1 and IM[x - 1][y] == 255:
            neighbour = getNodeNumber(r,c,x - 1, y)
            if diction[neighbour][3] == -1:
                diction[neighbour][3] = 1
                diction[neighbour][2] = current
                vertQueue.enqueue(neighbour)
                
        #bottom node
        if y + 1 <= c - 1 and IM[x][y + 1] == 255:
            neighbour = getNodeNumber(r,c,x, y + 1)
            if diction[neighbour][3] == -1:
                diction[neighbour][3] = 1
                diction[neighbour][2] = current
                vertQueue.enqueue(neighbour)
        
        #top node
        if y - 1 >= 0 and IM[x][y - 1] == 255:
            neighbour = getNodeNumber(r,c,x, y - 1)
            if diction[neighbour][3] == -1:
                diction[neighbour][3] = 1
                diction[neighbour][2] = current
                vertQueue.enqueue(neighbour)

def getPath(NodeNumber):
    path = []
    minP = 1000000
    maxP = -1
    while not diction[NodeNumber][2] == -1:
        x = diction[NodeNumber][0]
        if minP > x:
            minP = x
        if maxP < x:
            maxP = x
        path.append(NodeNumber)
        NodeNumber = diction[NodeNumber][2]
    x = diction[NodeNumber][0]
    if minP > x:
        minP = x
    if maxP < x:
        maxP = x
    path.append(NodeNumber)
    path.append(minP)
    path.append(maxP)
    return path
