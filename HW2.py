# -*- coding: utf-8 -*-
"""
Kristen Pimentel
u1263226 
MEEN 2450 Homework 2
1 October 2020
"""
import numpy as np
import matplotlib.pyplot as plt

#%%
#Testing my functions with the function in question 2
fun = lambda x:(0.8-0.3*x)/x

x = bisection(fun,1,3) #using the bisection method
print("Bisection x = ",x[0])

x = false_position(fun,1,3) #using the false position method
print("False Position x = ",x[0])

x = secant(fun,1,3) #using the secant method
print("Secant x = ",x[0],"\n")


#%%
#Find the roots to the following eqn
fun6 = lambda x: x**4 - x**2 + 3*x - 8

#Report the roots and the # of iters needed for the Bisection Method to converge.
x,iters = bisection(fun6,-1,5) #using the bisection method
print("Bisection x = ",x,"with tol of 1e-6")
print("Number of iterations = ",iters)

x,iters = false_position(fun6,-1,5,maxiter=500) #using the false position method
print("False Position x = ",x,"with tol of 1e-6")
print("Number of iterations = ",iters)

x,iters = secant(fun6,-1,5) #using the secant method
print("Secant x = ",x,"with tol of 1e-6")
print("Number of iterations = ",iters)
print("\nThere is only one root of the function x**4 - x**2 + 3*x - 8 between -1,5 and it is",x)
print("")


x,iters = bisection(fun6,-1,5,tol=0.5) #using the bisection method
print("Bisection x = ",x,"with tol of 0.5")
print("Number of iterations = ",iters)

x,iters = false_position(fun6,-1,5,tol=0.5) #using the false position method
print("False Position x = ",x,"with tol of 0.5")
print("Number of iterations = ",iters)

x,iters = secant(fun6,-1,5,tol=0.5) #using the secant method
print("Secant x = ",x,"with tol of 0.5")
print("Number of iterations = ",iters,"\n")

#%% THE OTHER ROOT

#Report the roots and the # of iters needed for the Bisection Method to converge.
x,iters = bisection(fun6,-3,-1) #using the bisection method
print("Bisection x = ",x,"with tol of 1e-6")
print("Number of iterations = ",iters)

x,iters = false_position(fun6,-3,-1,maxiter=500) #using the false position method
print("False Position x = ",x,"with tol of 1e-6")
print("Number of iterations = ",iters)

x,iters = secant(fun6,-3,-1) #using the secant method
print("Secant x = ",x,"with tol of 1e-6")
print("Number of iterations = ",iters)
print("\nThere is only one root of the function x**4 - x**2 + 3*x - 8 between -3,-1 and it is",x)
print("")


