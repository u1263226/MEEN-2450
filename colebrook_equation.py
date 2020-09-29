# -*- coding: utf-8 -*-
"""
Kristen Pimentel
u1263226 
MEEN 2450 Lab 4: Colebrook Equation
29 September 2020
"""
import numpy as np
import math

#Colebrook eqn
 
def colebrook_equation(f,e,D,Re):
    q = 2.51
    w = 3.7
    r = 2.0
    if D <=0:
        raise ValueError('invalid D')
    k = ((e/D)/w) + (q/(math.sqrt(f)*Re))
    #print('k=',k)
    if k<=0:
        raise ValueError('value must be positive for log10')
        
    #estimate of the friction factor
    g = r*math.log10(k)
    #print('g = ',g)
    
    if f<0:
        raise ValueError('the sqrt of a negative number is imaginary')
    if f==0:
        raise ValueError('cant divide by zero')
    
    h = 1/math.sqrt(f) + g
    #print('h=',h)
    
    return h
    

    