# -*- coding: utf-8 -*-
"""
Kristen Pimentel 
u1263226 
ME EN 2450: Lab 7: eullers
3 November 2020 
"""
import numpy as np

#Implement Eulers Method that integrates a DE from t0 to tf with initial comdition y0
# y(ti+1) = y(ti) + dydt(ti+1 - ti)

def eulers(odefun, tspan, y0,tol = 10**-6):
    #tspan: time values of integration
    #dydt = odefun(t,y)
    #y0: initial conditions 
    y = [y0]
    t = [tspan[0]]
    
    for i in range(len(tspan)-1):
        
        t.append(tspan[i+1])
        y.append(y[i] + odefun(t[i],y[i])*(t[i+1]-t[i]))
        
        if ((y[i+1]-y[i])/(y[i] if y[i]!=0 else 1))<tol:
            break
        
    return t,y