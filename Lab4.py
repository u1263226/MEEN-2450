# -*- coding: utf-8 -*-
"""
Kristen Pimentel
u1263226 
MEEN 2450 Lab 4
29 September 2020

"""
import numpy as np
import matplotlib.pyplot as plt
import math

e = 0.0002 #roughness of the pipe m
D = 0.25 #diameter m
V = 10 #average velocity of flow m/s
ro = 1000 #density kg/m^3
mu = 6*10**(-4) #viscosity Pa/s
L = 110 #length of pipe m 
g = 9.81 # force due to gravity
Re = ro*V*D/mu #Reynolds number kg*Pa/m*s^2
#print("Re = ",Re)
#print("e/D = ",(e/D))

#define a function handle relating to colebrook that only takes one input f
fun = lambda f:colebrook_equation(f,e,D,Re)

#Use bisection to calculate the friction factor 
a = 0.015
b = 0.06
f = bisection(fun, a, b,plot_output=True)
print('f=',f)

#calculate the head loss
headLoss = f*(L/D)*(V**2/(2*g))
print("The headloss is ",headLoss,"\ngiven an initial guess of [",a,",",b,"] and the given values:\ne =",e,"m\nD =",D,"m\nV =",V,"m/s\nro =",ro,"kg/m^3\nmu =",mu,"Pa/s\nL =",L,"m")

# compute the number of iterations to achieve eSuba<1*10**-6
tol = 1*10**-6
n = math.log((b-a)/tol)/math.log(2)
print('n = ',n)