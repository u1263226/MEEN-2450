# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 13:16:40 2020

@author: kshay
"""

import numpy as np
def runge_kutta_four(odefun, tspan, y0):
    
    l = 10
    n= 51
    h = l/(n-1)
    
    x0 = y0[0]
    
    y = np.zeros((l,n))
    y[0][0] = x0
    y[1][0] = y0[1]
    
    for i in range(n-1):
        k1 = odefun(x0, y0)
        k2 = odefun(x0+0.5*h, np.array([y0[0] + 0.5*k1[0]*h, y0[1] + 0.5*k1[1]*h]))
        k3 = odefun(x0+0.5*h, np.array([y0[0] + 0.5*k2[0]*h, y0[1] + 0.5*k2[1]*h]))
        k4 = odefun(x0+h,     np.array([y0[0] +     k3[0]*h, y0[1] +     k3[1]*h]))
        y[0,i+1] = y0[0] + (1/6)*h*(k1[0] + 2*k2[0] + 2*k3[0] + k4[0])
        y[1,i+1] = y0[1] + (1/6)*h*(k1[1] + 2*k2[1] + 2*k3[1] + k4[1])
        
        x0 = x0 + h
        y0 = y[:,i+1]
        
    return tspan, y
