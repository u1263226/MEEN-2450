# -*- coding: utf-8 -*-
"""
Kristen Pimentel 
u1263226 
ME EN 2450: Lab 8: Moving train
3 November 2020
"""

import numpy as np
from runge_kutta_four import runge_kutta_four
from train_motion import train_motion
import matplotlib.pyplot as plt

#define system properties
g = 9.81  #m/s^2 gravity 
ro = 1 #kg/m^3 air density
m = 10 #kg train mass
mw = 0.1 #kg wheel mass
A = 0.05 #m^2 frontal area
Cd = 0.8 #drag coefficient
Crr = 0.03 #rolling coefficient of friction
Fp = 1 #N Propulsion force
mu = 0.7 #coefficient of static friction
Pgauge = 100000 #Pa tank gauge pressure
rw = 0.025 #m wheel radius 
rp = 0.01 #m piston radius
lp = 0.1 #m piston stroke length
rg = 0.01 #m gear radius
x0 = 0
v0 = 0
y0 = [x0,v0] #initial conditions
n = 10

tspan = np.linspace(0,10,11)
params = [g,ro,m,A,Cd,Crr,mw,mu,Pgauge,rw,rp,rg,lp]

odefun = lambda t,y: train_motion(t,y,params) 

t,y1 = runge_kutta_four(odefun,tspan,y0)

#print(t)
#print(y)
plt.figure(1)
plt.plot(t,y1[1],label = "velocity")
plt.xlabel("Time(s)")
plt.ylabel("Velocity(m/s)")
plt.title("Velocity vs. Time of Train Motion")
plt.figure(2)
plt.plot(t,y1[0],label = "position")
plt.xlabel("Time(s)")
plt.ylabel("Position(m)")
plt.title("Position vs. Time of Train Motion")
