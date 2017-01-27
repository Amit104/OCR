# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 19:38:56 2017

@author: Axle
"""

from initialisations import *
def wordSeg(IM):
    r = IM.shape[0]
    c = IM.shape[1]
    a=[]
    flag=0
    
    a.append(0)
    for i in range(c):
        colsum = 0
        for j in range(r):
            if IM[j][i]==0:
                colsum=colsum+1
                
        if colsum==0 and flag==0:
            flag=1
            col=i
        
        elif colsum!=0 and flag==1:
            a.append(int((i+col)/2))
            flag=0
    a.append(c-1)
            
    for i in range(len(a)-1):
        imag = []    
        for j in range(r):                               
            il = []         
            for k in range (a[i+1]-a[i]+1):            
                il.append(0)      
            imag.append(il) 
            
        for j in range(r):                               
            for k in range(a[i+1]-a[i]+1):            
                imag[j][k]=IM[j][a[i]+k]   
                imag = np.array(imag,dtype=np.uint8)
                #wordSeg(imag)
        cv2.imshow('image',imag)
        cv2.waitKey(0)  
        cv2.destroyAllWindows()
                   
            
           
            
        
        
            