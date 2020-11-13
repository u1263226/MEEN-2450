# -*- coding: utf-8 -*-
"""
Kristen Pimentel 
u1263226 
ME EN 2450: Lab 8: Moving train
3 November 2020
"""

import numpy as np
from eulers2 import eulers
from train_motion import train_motion
import matplotlib.pyplot as plt

#define system properties
g = 9.8  #m/s^2 gravity 
ro = 1 #kg/m^3 air density
m = 10 #kg train mass
A = 0.05 #m^2 frontal area
Cd = 0.8 #drag coefficient
Crr = 0.002 # rolling coefficient of friction
Fp = 1  #N Propulsion force
x0 = 0
v0 = 0
y0 = [x0,v0]

tspan = np.linspace(0,10,11)
params = [g,ro,m,A,Cd,Crr,Fp]

odefun = lambda t,y: train_motion(t,y,params) 

t,y = eulers(odefun,tspan,y0)
#print(t)
#print(y)
plt.figure(1)
plt.plot(t,y[0],label = "velocity")
plt.xlabel("Time(s)")
plt.ylabel("Velocity(m/s)")
plt.title("Velocity vs. Time of Train Motion")
plt.figure(2)
plt.plot(t,y[1],label = "position")
plt.xlabel("Time(s)")
plt.ylabel("Position(m)")
plt.title("Position vs. Time of Train Motion")
