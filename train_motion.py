# -*- coding: utf-8 -*-
"""
Kristen Pimentel 
u1263226 
ME EN 2450: Lab 8: Train Motion
3 November 2020
"""

def train_motion(t,y,params):
    
    g = params[0] #gravity 
    ro = params[1] #air density
    m = params[2] #train mass
    A = params[3] #frontal area
    Cd = params[4] #drag coefficient
    Crr = params[5] # rolling coefficient of friction
    Fp = params[6] #Propulsion force
    
    #dx/dt = v
    #dv/dt = d^2x/dt^2 = (Fp - Fd - Frr)/m
    #Fp = constant
    #Fd = (ro*Cd*A*v**2)/2 = (ro*Cd*A*(dx/dt)**2)/2
    #Frr = m*g*Crr
    #dy/dt = {dx/dt, dv/dt}
    
    dxdt = y
    Fd = (ro*Cd*A*(dxdt)**2)/2
    Frr = m*g*Crr
    dvdt = (Fp - Fd - Frr)/m
    dydt = [dvdt,dxdt]
    
    return dydt 
        