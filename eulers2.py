# -*- coding: utf-8 -*-
"""
Kristen Pimentel 
u1263226 
ME EN 2450: Lab 8: eulers
3 November 2020 
"""
import numpy as np

#Implement Eulers Method that integrates a DE from t0 to tf with initial comdition y0
# y(ti+1) = y(ti) + dydt(ti+1 - ti)

def eulers(odefun, tspan, y0,tol = 10**-6):
    #tspan: time values of integration
    #dydt = odefun(t,y)
    #y0: initial conditions 
    
    y = np.zeros((len(y0),len(tspan)))
    t = tspan
    #print("y = ", y)
    #print("tspan = ", tspan)
    #print("t = ", t)
    #print("y0 = ", y0)
    for j in range(len(y0)):
        for i in range(len(tspan)-1):
            
            f = odefun(t[i],y[:,i])
            #print ("(i,j,f) = (",i,",",j,",",f,")")
            y[j][i+1] = y[j][i] + f[j][0] * (t[i+1]-t[i])
            
            # if ((y[i+1]-y[i])/(y[i] if y[i]!=0 else 1))<tol:
            #     break
        
    return t,y
