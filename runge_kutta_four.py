# -*- coding: utf-8 -*-
"""
Kristen Pimentel 
u1263226 
ME EN 2450: Lab 9: RK4
3 November 2020
"""

import numpy as np
def runge_kutta_four(odefun, tspan, y0):
    
    n = len(tspan)
      
    x0 = tspan[0] 
    
    y = np.zeros((2,n))
    y[0][0] = y0[0]
    y[1][0] = y0[1]
    
    for i in range(0,n-1):
        
        h = tspan[i+1] - tspan[i]
        
        k1 = odefun(x0, y0)
        k2 = odefun(x0+0.5*h, np.array([y0[0] + 0.5*k1[0]*h, y0[1] + 0.5*k1[1]*h]))
        k3 = odefun(x0+0.5*h, np.array([y0[0] + 0.5*k2[0]*h, y0[1] + 0.5*k2[1]*h]))
        k4 = odefun(x0+h,     np.array([y0[0] +     k3[0]*h, y0[1] +     k3[1]*h]))
        y[0,i+1] = y0[0] + (1/6)*h*(k1[0] + 2*k2[0] + 2*k3[0] + k4[0])
        y[1,i+1] = y0[1] + (1/6)*h*(k1[1] + 2*k2[1] + 2*k3[1] + k4[1])
        
        x0 = x0 + h
        y0 = y[:,i+1]
        
    return tspan, y
