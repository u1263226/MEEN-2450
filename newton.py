# -*- coding: utf-8 -*-
"""
Kristen Pimentel
u1263226 
MEEN 2450 Lab 5: Newton Raphson Method
6 October 2020
"""


import numpy as np
import math
from central_difference import central_difference 

def newton(fun,x0,fprime = None,tol = 1e-6,maxiter = 50):
    
    #check whether the initial guess is a root
    if fun(x0) == 0:
        return x0
    
    #create copy of x0
    x = x0
    
    #if fprime is not given use central_difference
    if fprime is None:
        fprime = lambda x:central_difference(fun,x,1e-4)

    
    #use the Newton Raphson method to estimate the root
    iters = 0
    dx = tol*2
    while iters <= maxiter :
        iters += 1
        if fprime(x) > 0 or fprime(x)<0:
            xOld = x
            dx = fun(x)/fprime(x) #increment in x
            x = x + dx
            xNew = x
        else:
            raise ValueError("dx = 0; root is returned as is")
        
        if abs(dx) <= tol:
            break
        
    #if root is not determined within maxiter or desired tol issue RuntimeError
    if abs(dx)> tol:
        raise RuntimeError("The solution does not converge withing the given tol = "+str(tol))
    
        
    
    return x