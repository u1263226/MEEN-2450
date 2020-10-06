# -*- coding: utf-8 -*-
"""
Kristen Pimentel
u1263226 
MEEN 2450 Lab 5
6 October 2020
"""
import numpy as np

#analytical derivative of solor_pond with respect to depth

def solar_pond_deriv(depth,density_top,zone_height):
    
    #the derivative of 
    #fd  = density - density_top*sqrt(1 + (math.tan((pi*depth)/(4*zone_height)))**2) 
    #with respect to depth
    x = (np.pi*depth)/(4*zone_height)
    sec2 = (1/np.cos(x))**2
    num = np.pi*density_top*(np.tan(x))*sec2
    denom = 4*zone_height*np.sqrt(sec2)
    
    fdprime = num/denom 
    
    return fdprime 