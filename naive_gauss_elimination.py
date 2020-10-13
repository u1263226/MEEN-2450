# -*- coding: utf-8 -*-
"""
Kristen Pimentel
u1263226 
MEEN 2450: Naive Gauss Elimination
13 October 2020
"""

import numpy as np 

def naive_gauss_elimination(A,b):
    
    n = len(A)
    a = A
    #print("length of b:",len(b))
    rows = len(a)
    #print("rows: ",rows)
    if len(b) != n:
        raise ValueError("Vector b is not compatable with matrix A")
        
    for i in range(rows):
        cols = len(a[i])
        if rows != cols:
            raise ValueError("The matrix dimensions are not compatable with Gauss Elimination")
    #print("cols:",cols)
    d = 0  #determine if the the matrix is diagonal or upper triangular
    c = 0
    for j in range(n-1):
        for i in range(j+1,n-1):
            c = c + a[i][j] #lowers of zero
    for i in range(n-1):
        for j in range(i+1,n-1):
            d = d + a[i][j] #uppers of 0
    
    B = np.zeros([n,n+1]) #create augmented matrix prior to solve
    for i in range(n):
        for j in range(n):
            B[i][j] = a[i][j] 
    for i in range(n):
        B[i][n] = b[i]
    
    if not(c+d == 0 or (c == 0 and d != 0)): #not diagonal or not upper triangle matrix
        #Forward Elimination 
        for i in range(n):
            if B[i][i] == 0:
                raise ValueError('Cannot divide by zero')
                
            for j in range(i+1, n):
                r = B[j][i]/B[i][i]
                
                for k in range(n+1):
                    B[j][k] = B[j][k] - r*B[i][k]

    # Back Substitution
    x = np.zeros(n)
    
    x[n-1] = B[n-1][n]/B[n-1][n-1]
    
    for i in range(n-2,-1,-1):
    
        x[i] = B[i][n]
        
        for j in range(i+1,n):
            x[i] = x[i] - B[i][j]*x[j]
        
        x[i] = x[i]/B[i][i]
    
    return x 

    