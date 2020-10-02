# -*- coding: utf-8 -*-
"""
Kristen Pimentel
u1263226 
MEEN 2450 Homework 2: False Position
1 October 2020
"""
import numpy as np
import math
import matplotlib.pyplot as plt
import time

#The false position method

def false_position(fun,a,b,tol=1*10**(-6), maxiter=50, plot_output=False):
    
    #check the validity of the guess(that they bracket a root)
    if fun(a)*fun(b) > 0 :
        raise ValueError('initial guesss does not bracket a root')
        
    if fun(a) == 0:
        return a
    if fun(b) == 0:
        return b
    
    #number of iterations for the error to drop below the tol
    n = math.log((b-a)/tol)/math.log(2)
    #if the root is not determined to be within the desired tol in the maxiters, raise Runtimeerror
    if n>maxiter:
        raise RuntimeError('the root cannot be determined within the desired tolerence in the max iterations')
    
    c = 0 #the root
    cOld = c #initialize cOld
    iters = 0 #initialize iters
    
    while iters<maxiter:
        
        iters = iters+1 #increment iteration
        c = b - ((fun(b)*(a-b))/(fun(a)-fun(b))) #calculate estimated root
        
        if iters<=1 :
            if plot_output == True :
                xArray = [a,c,b]
                fArray = [fun(a),fun(c),fun(b)]
                #plot updated guess as well as the current brackets of each iteration
                plt.figure()
                plt.plot(xArray,fArray)
                plt.scatter(xArray,fArray,s=100,facecolors='none',edgecolors='r')
                plt.plot([a,b],[fun(c),fun(c)],'--') #dashed line at y=root estimate
                plt.xlabel("Step "+str(iters)+"\nError = n/a"+"\nZero Estimate = "+str(c))
                plt.show()
                time.sleep(0.5)#0.5 second pause
                
        if iters>1:
            eSuba = abs(c-cOld) #calculate error
        
            if plot_output == True :
                xArray = [a,c,b]
                fArray = [fun(a),fun(c),fun(b)]
                #plot updated guess as well as the current brackets of each iteration
                plt.figure()
                plt.plot(xArray,fArray)
                plt.scatter(xArray,fArray,s=100,facecolors='none',edgecolors='r')
                plt.plot([a,b],[fun(c),fun(c)],'--') #dashed line at y=root estimate
                plt.xlabel("Step "+str(iters)+"\nError ="+str(eSuba)+"\nZero Estimate = "+str(c))
                plt.show()
                time.sleep(0.5)#0.5 second pause 
            
            if abs(fun(c)) <= tol or eSuba<=tol:
                break #exit
        
        if fun(a)*fun(c) > 0 : #determine if f(a) and f(c) is positive or negative
            a = c #if positive replace lower estimate
        else:
            b = c #if negative replace upper estimate
        
            
        cOld = c #assign cOld to be the previous c in order to calculate the new error
            
    return c,iters #return the best estimated root