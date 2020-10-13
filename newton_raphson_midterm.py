# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 14:37:57 2020

@author: kshay
"""

#newton raphson

def newton_raphson(fun,fprime,guess,tol=0.001,maxiter=100,plot=False):
    i = 0
    c = guess
    dc = tol*2
    while i < maxiter:
        i += 1
        
        if fprime(c)<0 or fprime(c)>0:
            
            c = c - fun(c)/fprime(c)
        
        if abs(dc)<= tol:
            break
        if plot = True:
            plt.plot(c,fun(c),s=50,facecolors = 'none')
            
    return c, i