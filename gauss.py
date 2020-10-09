# -*- coding: utf-8 -*-
"""
Kristen Pimentel
u1263226 
MEEN 2450 HW3
6 October 2020
"""
import numpy as np

#Ask for number of unknowns
n = int(input('Enter number of unknowns: '))

# Initialize an n x n+1 array 
a = np.zeros((n,n+1))

#Initialize solution vector
x = np.zeros(n)

# Reading augmented matrix coefficients
print('Please Enter Augmented Matrix Coefficients:')
for i in range(n):
    for j in range(n+1):
        a[i][j] = float(input( 'a['+str(i)+']['+ str(j)+']='))

# Applying Gauss Elimination
for i in range(n):
    if a[i][i] == 0.0:
        raise ValueError('Cannot divide by zero')
        
    for j in range(i+1, n):
        r = a[j][i]/a[i][i]
        
        for k in range(n+1):
            a[j][k] = a[j][k] - r*a[i][k]

# Back Substitution
x[n-1] = a[n-1][n]/a[n-1][n-1]

for i in range(n-2,-1,-1):
    x[i] = a[i][n]
    
    for j in range(i+1,n):
        x[i] = x[i] - a[i][j]*x[j]
    
    x[i] = x[i]/a[i][i]

# Display solution
print('\nSolution: ')
for i in range(n):
    print('X%d = %0.2f' %(i,x[i]), end = '\t')
