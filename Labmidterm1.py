# -*- coding: utf-8 -*-
"""
Kristen Pimentel
u1263226 
MEEN 2450: Lab Midterm 1
13 October 2020
"""
import numpy as np
import matplotlib.pyplot as plt
import math

#%% Problem 1

#part a

b = np.zeros([3,1], dtype='int')
n = 0

for i in range(len(b)):
    if i == 0:
        b[i] = n 
    elif i == 1:
        b[i] = n + 3
    else:
        b[i] = n + 5
print(b)

#part b
rows = 3
cols = 3
A = np.zeros([rows,cols])
n = 2
for i in range(rows):
    for j in range(cols):
        if i == 2:
            if j == 1:
                A[i][j] = 7
            else:
                A[i][j] = 6
        if i == 1:
            if j == 0:
                A[i][j] = 3
            if j == 1:
                A[i][j] = 4
            if j == 2:
                A[i][j] = 5
        if i == 0:
            if j == 1:
                A[i][j] = 1
            else:
                A[i][j] = 2
            
print(A)
#part c
s = np.zeros(len(b))
a = 0
for i in range(len(A)):
    for j in range(len(A)):
        a = A[i][j]*b[i]
        s[j] = a + s[j]
print(s)

np.dot(A,b)

#%% Problem 2

epsilon = 1.43*10**-6
ro = 1.38
mu = 1.91*10**-5
D = 0.0061
V = 54

Re = (ro*V*D)/mu
       
colebrook = lambda f: (1/math.sqrt(f) + 2.0*math.log10((epsilon/(3.7*D))+(2.51/(Re*math.sqrt(f)))))

colebrookprime = lambda f: (1/(2*f**(3/2)))*(1.0+(2.18261/Re)*(((epsilon)/D)/3.7)+1/(2.51/(Re*math.sqrt(f))))
    
#part a
x = np.linspace(1,10,100)
y = np.zeros(100)
y2 = np.zeros(100)
for i in range(len(x)):
    y2[i] = colebrook(x[i]) #various y values for given x-
plt.plot(x,y2)

#part c
f,iters = newton_raphson(colebrook,colebrookprime,0.85)
print("The root of eqn 1:",f,"in",iters,"iterations")
print("colebrook",colebrook(f))

#part d

plt.scatter(f,colebrook(f),s=100)


        
#%% Problem 3

#part a
"""        
sand = 4800 
fine = 5810
coarse = 5690

pit1 = 0.52*sand + 0.3*fine + 0.18*coarse
pit2 = 0.2*sand + 0.5*fine + 0.3*coarse
pit3 = 0.25*sand + 0.2*fine + 0.55*coarse

sand = 0.52*pit1 + 0.2*pit2 + 0.25*pit3 #these are what should be used as the augmented matrix
fine = 0.3*pit1 + 0.5*pit2 + 0.2*pit3
coarse = 0.18*pit1 + 0.3*pit2 + 0.55*pit3
"""
#part b
A = [[0.52,0.2,0.25],[0.3,0.5,0.2],[0.18,0.3,0.55]]
b = [4800,5810,5690]

result = gauss(A,b)
print("sand:",result[0],"fine gravel:",result[1],"coarse gravel:",result[2])

#part c

#If the material composition remains fixed then the LU decomposition
#would be a better solution since all that is changing is the requirements 
#of sand, fine or coarse gravel. This is because you would be using a
#reduced row-echelon matrix which would allow the solution set to solve along the 
#diagonal matrix. This would make the calculation realatively easy for future 
#projects



        