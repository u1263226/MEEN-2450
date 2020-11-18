# -*- coding: utf-8 -*-
"""
Kristen Pimentel 
u1263226 
ME EN 2450: Lab 9: Train Motion
3 November 2020
"""
import numpy as np

def train_motion(t,y,params):
    
    g = params[0] #gravity 
    ro = params[1] #air density
    m = params[2] #train mass
    A = params[3] #frontal area
    Cd = params[4] #drag coefficient
    Crr = params[5] #rolling coefficient of friction
    mw = params[6] #wheel mass
    mu = params[7] #coefficient of static friction
    Pg = params[8] #Pa tank gauge pressure
    rw = params[9] #wheel radius
    rp = params[10] #piston radius
    rg = params[11] #gear radius
    lp = params[12] #length of piston
    
    Ap = np.pi*rp**2 #area of piston head
    
    #dx/dt = v
    #dv/dt = d^2x/dt^2 = (Fp - Fd - Frr)/m
    #Fp = constant
    #Fd = (ro*Cd*A*v**2)/2 = (ro*Cd*A*(dx/dt)**2)/2
    #Frr = m*g*Crr
    #dy/dt = {dx/dt, dv/dt}
    #Fp = Pgauge*Ap
    #T = rg*Fp
    #alpha = (1/rw)*a
    #T-rw*Ft = I*alpha
    #Ft = T/rw - mw*rw*alpha
    #Ft = (rg*(Pgauge*Ap))/rw - mw*a
    
    dxdt = y[0]
    
    Fd = (ro*Cd*A*(dxdt)**2)/2
    Frr = m*g*Crr
    Ft = (rg*Pg*Ap)/rw
    La = (lp*rw)/rg
    
    if Ft > (mu*(m+mw)/2*g):
        raise ValueError("Wheel slip has occured")
        
    if y[1] <= La:
        dvdt = (Ft - Fd - Frr)/(m + mw)
    else:
        dvdt = -Fd -Frr
    
    dydt = [dvdt,dxdt]
    
    return dydt 
        
        
