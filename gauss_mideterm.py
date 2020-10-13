# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 14:21:02 2020

@author: kshay
"""

#gauss

def gauss(A,b):
    
    n = len(A)
    
    #forward elimintation
    for k in range(1,n-1):
        for i in range(k+1,n):
            s=A[i][k]/A[k][k]
            for j in range(k,n):
                A[i][j] = A[i][j] - s*A[k][i]
            b[i] = b[i] - s*b[k]
            
    #backward substitution
    
    x = np.zeros(n)
    
    x[n] = b[n]/A[n][n]
    
    for i in range(n-1,-1,1):
        s = 0
        for j in range(i+1,n):
            s = s + A[i][j]*x[j]
        x[i] = (b[i] - s)/A[i][i]
    