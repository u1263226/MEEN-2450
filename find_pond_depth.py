# -*- coding: utf-8 -*-
"""
Kristen Pimentel
u1263226 
MEEN 2450 Lab 5
6 October 2020
"""
import numpy as np 
import matplotlib.pyplot as plt

#inittialize input paramaters
depth = 0
density = 1200
density_top = 1100
zone_height = 5
a = -3
b = 3
step = (b-a)/100
#function handle for solar_pond
from solar_pond import solar_pond

fun = lambda depth: solar_pond(depth,density,density_top,zone_height)

#function handle for solar_pond_deriv
from solar_pond_deriv import solar_pond_deriv

fprime = lambda depth: solar_pond_deriv(depth,density_top,zone_height)


#plot solar_pond to find initial guess
x = [a]
for i in range(1,100):
    x.append(x[i-1] + step)
y = []
y2 = []
o = []
for i in range(len(x)):
    y.append(fun(x[i]))
    y2.append(fprime(x[i]))
    o.append(0)
    
plt.plot(x,y,label = "solar_pond")
plt.plot(x,y2,label = "solar_pond_deriv",color = 'g')
plt.plot(x,o,"-",label = 'Y=0')
plt.scatter(2.617,0,s=100,facecolors='none',edgecolors='r',label = "intercept")
plt.title("Plot of Solar Pond Eqn")
plt.xlabel("Depth")
plt.ylabel("Density")
plt.legend()
plt.show()


#call newton with the following
from newton import newton 

density = 1200 #kg/m^3
density_top = 1100 #kg/m^3
zone_height = 5 #m
x0 = 2.6
depth = newton(fun,x0)
print("depth =",depth)

#print output of the root in solar_pond
fd = solar_pond(depth,density,density_top,zone_height)
print("solar_pond(depth) = ",fd)

print("With a given density of", density,"the depth of the pond is",depth)