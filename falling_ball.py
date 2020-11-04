# -*- coding: utf-8 -*-
"""
Kristen Pimentel 
u1263226 
ME EN 2450: Lab 7: falling_ball
3 November 2020 
"""
import matplotlib.pyplot as plt

ball_type = ["steel","wood","pingpong"]
m = [0.225,0.021,0.002] #varying mass kg
d = [0.038,0.0367,0.0374] #varying diameter m
r = [] 
for i in range(len(d)):
    r.append(0.5*d[i]) #varying radii m
params1 = [9.81,1.2,m[0],r[0],0.4] #constants gravity, air density, mass, radius, drag coefficient
params2 = [9.81,1.2,m[1],r[1],0.4]
params3 = [9.81,1.2,m[2],r[2],0.4]
tspan = []
for i in range(1000000): # time range
    tspan.append(i*0.001) # time step
y0 = 0

#define function handles for each ball
from ball_motion import ball_motion
odefun1 = lambda t, y: ball_motion(t,y,params1)
odefun2 = lambda t, y: ball_motion(t,y,params2)
odefun3 = lambda t, y: ball_motion(t,y,params3)

#calculate the various velocities and corresponding times
from eullers import eulers
[t1,y1] = eulers(odefun1, tspan, y0)
[t2,y2] = eulers(odefun2, tspan, y0)
[t3,y3] = eulers(odefun3, tspan, y0)

#plot velocity as a function of time and the terminal velocity for each ball
plt.plot(t1,y1,label = "Steel")
plt.plot(t2,y2,label = "Wood")
plt.plot(t3,y3, label = "Ping-pong")
plt.scatter([t1[-1],t2[-1],t3[-1]],[y1[-1],y2[-1],y3[-1]])
plt.text(t1[-1],y1[-1],'('+str(round(t1[-1],3))+', '+str(round(y1[-1],3))+')')
plt.text(t2[-1],y2[-1],'('+str(round(t2[-1],3))+', '+str(round(y2[-1],3))+')')
plt.text(t3[-1],y3[-1],'('+str(round(t3[-1],3))+', '+str(round(y3[-1],3))+')')
plt.title("Velocity of Falling Balls vs. Time")
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.legend()
