# -*- coding: utf-8 -*-
"""
Kristen Pimentel 
u1263226 
ME EN 2450: Lab 7: ball_motion
3 November 2020 
"""
import numpy as np
# Ball motion function calculates y' = f(t,y) for a particular t and y
# using: dv/dt = g - 1/2*((ro*C_d*A*v**2)/m_b)

def ball_motion(t,y,params):
    #params is an array 
    g = params[1] #gravity
    ro = params[2] #air density 
    m_b = params[3] # ball mass
    r_b = params[4] # ball radius
    C_d = params[5] # drag coefficient
    A = np.pi*(r_b)**2 # cross sectional area
    
    dydt = g - (ro*C_d*A*y**2)/(2*m_b) # the ode function dv/dt
    
    return dydt 
