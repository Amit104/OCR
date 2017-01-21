# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 19:17:25 2017

@author: Axle
"""

from initialisations import *

def getNodeNumber(r, c, x, y):
    return (x * c) + y + 1
        
diction = {}
pathList = []

            
def startBFSandReturnPathList(IM, r, c, brkPts, size):
    for i in range(1, r * c):
        diction[i] = [-1 for x in range(1, 4)]
    
    for i in range(1, size):
        bfs(IM, getNodeNumber(r, c, (brkPts[i - 1] + brkPts[i]) / 2 , 0), brkPts[i - 1], brkPts[i], r, c)
        pathList.append(getPath(getNodeNumber(r, c, (brkPts[i - 1] + brkPts[i]) / 2 , c - 1)))
    
    
def LineSeg(IM, r, c, brkPts, size):
    startBFSandReturnPathList(IM, r, c, brkPts, size)
    
    

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
            neighbour = getNodeNumber(x + 1, y)
            if diction[neighbour][3] == 0:
                diction[neighbour][3] = 1
                diction[neighbour][2] = current
                vertQueue.enqueue(neighbour)
        
        #left node
        if x - 1 >= x1 and IM[x - 1][y] == 255:
            neighbour = getNodeNumber(x - 1, y)
            if diction[neighbour][3] == 0:
                diction[neighbour][3] = 1
                diction[neighbour][2] = current
                vertQueue.enqueue(neighbour)
                
        #top node
        if y - 1 >= 0 and IM[x][y - 1] == 255:
            neighbour = getNodeNumber(x, y - 1)
            if diction[neighbour][3] == 0:
                diction[neighbour][3] = 1
                diction[neighbour][2] = current
                vertQueue.enqueue(neighbour)
                
        #bottom node
        if y + 1 <= c - 1 and IM[x][y + 1] == 255:
            neighbour = getNodeNumber(x, y + 1)
            if diction[neighbour][3] == 0:
                diction[neighbour][3] = 1
                diction[neighbour][2] = current
                vertQueue.enqueue(neighbour)
        

def getPath(NodeNumber):
    path = []
    while not diction[NodeNumber][2] == -1:
        path.append(NodeNumber)
        NodeNumber = diction[NodeNumber][2]
    path.append(NodeNumber)
    return path
    