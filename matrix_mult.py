# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 15:12:07 2020

@author: kshay

matrix_mult(x,y)
"""

# Create a functionmatrix_mult(X,Y)that does matrix multiplication between matricies X and Y

def matrix_mult(X,Y):
    # chack dimensions of X,Y. Issue an error is the dimensions do not match
    if len(X)!=len(Y[0]) or len(Y)!=len(X[0]):
        raise ValueError("Error! The matricies cannot be multiplied")
    # using the dot product and a nested for loop
    P = ChooseArray(len(X),len(Y[0]),"true")
    for i in range(len(X)):
        for j in range(len(Y[i])):
            P[i,j] = np.dot(X[i,:],Y[:,j])
    
    return P # returns the product of the two matricies