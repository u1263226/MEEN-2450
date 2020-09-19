# -*- coding: utf-8 -*-
"""
MEEN 2450 Lab 2
Kristen Pimentel
u1263226
18 September 2020
"""
import numpy as np

# Define the global arrays for problems 1-10 using my "ChooseArray" function from lab 1

A = [1,2,3,4,5]
B = [2,3,4,5,6]
C = ChooseArray(2,3,"true")
D = ChooseArray(2,3,"false")
E = ChooseArray(3,2,"true")

print("A = ",A)
print("B = ",B)
print("C = ",C)
print("D = ",D)
print("E = ",E)

#%% Problem 1 ELEMENT-WISE ARITHMETIC ON A SINGLE ARRAY

# Calculate 5*A - 2
A = np.array(A) #make sure A is an array so that built in functions produce correct results
x1 = 5*A - 2
print("1: 5*A-2 = ",x1)

#%% Problem 2 ELEMENT-WISE ARITHMETIC ON A SINGLE ARRAY

#Subtract 5 times the first row of D from the second row of D

d1 = D[0][:] #index first row of D
d2 = D[1][:] #index second row of D
x2 =  d2 - (d1)*5 #The new second row in D

D2 = [[d1],[x2]] # !!!!!!!!!!!! does not give a final array

print("2: d2 - d1*5 = ",D2)

#%% Problem 3 ELEMENT-WISE ARITHMETIC WITH TWO ARRAYS

# A) Calculate A + B using a for loop to create the solution vector element-by-element.
x3a = []
A = [1,2,3,4,5]
B = [2,3,4,5,6]

for i in range(len(A)):
    x3a += [A[i] + B[i]]
    
print("3a: A+B =",x3a)

# B) Calculate A + B using the + operator or built-in functions
A = np.array(A) #make sure A and B are arrays so built in functions can be applied
B = np.array(B)

x3b = A + B #add arrays
print("3b: A+B =",x3b)

#%% Problem 4 ELEMENT-WISE ARITHMETIC WITH TWO ARRAYS

# Calculate C + D using nested for loop to create the solution vector element-by-element.
for i in range(len(C)):
    for j in range(len(C[i])):
        s[i,j] = C[i,j] + D[i,j]
print("4a: C+D =",s)

# Calculate C + D using built-in operators or functions (Which operator/function should you use? 
#(Remember, this is element-wise multiplication, NOT matrix multiplication.)
s2 = C+D
print("4b: C+D =",s2)

#%% Problem 5 SUMS

# Calculate the sum of all elements in A using a for loop
p = 0 
for i in range(len(A)):
    p = p + A[i] #sum of each element in A
    
print("5a: Sum in A =",p)
    
# Calculate the sum of all elements in A using a built-in function
p2 = np.sum(A)
print("5b: Sum in A =",p2)

#%% Problem 6 SUMS

# Calculate the sum of all elements in C using a for loop 
w = 0
ww = 0
for i in range(len(C)):
    w = w + C[i] #sum of rows, partial sum
for j in range(len(w)):
    ww = ww + w[i] #sum of columns = total sum
    
print("6a: Sum in C =",ww)

# Calculate the sum of all elements in C using a built-in function
w2 = np.sum(C)
print("6b: Sum in C =",w2)

#%% Problem 7 SUMS

#Calculate the sum of the second row of C only, using a built-in function
c2 = C[1][:] #index 2nd row of c
p7 = np.sum(c2)
print("7: Sum of the second row of C =",p7)

#%% Problem 8 DOT PRODUCT

# Calculate A dot B using a for loop
x1 = 0
total = 0
for i in range(len(A)):
    x1 = A[i]*B[i] #multiply element-wise of A and B
    total = total + x1 #add each element multiplication to produce a scalar value of the dot product
print("8a: A dot B =",total)

# Calculate A dot B using a built-in function
e = np.dot(A,B) #apply the dot product
print("8b: A dot B =",e)

#%% Problem 9 DOT PRODUCT

# Calculate the dot product of the first row of D with the first column of E using a built-in function
d1 = D[0][:] #index first row of D
e1 = E[:,0] #index first column of E
f = np.dot(d1,e1) #apply the dot product
print("9: first row D dot first column E =",f)

#%% Problem 10 MATRIX MULTIPLICATION

# using your matrix_mult(X,Y) function calculate the product of D and E
de = matrix_mult(D,E) #using my function matrix multiplication of D and E
print("10a: Matrix multiplication of D and E = ",de)

#compare the value of your function to a bulit in numpy.matmul()
de2 = np.matmul(D,E) #matrix multiplication of D and E
print("10b: Matrix multiplication of D and E = ",de2)

#%% Problem 11 ALGORITHMIC ARRAY CREATION

# using your fibonacci(N) function output a sequence of 10 values
fib = fibonacci(10) 
print("11: Fibonacci sequence of 10 values =",fib)