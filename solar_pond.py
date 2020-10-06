# -*- coding: utf-8 -*-
"""
Kristen Pimentel
u1263226 
MEEN 2450 Lab 5
6 October 2020
"""

import numpy as np

def solar_pond(depth,density,density_top,zone_height):
    #depth: the gradient zone
    #density: the coresponding depth you wish to find at a given density
    #density_zone: the density at the top of the gradient zone
    #zone_height: the height of the gradient zone
    #Outputs the function in root finding form
    
    #density = density_top*sqrt(1 + (math.tan((pi*depth)/(4*zone_height)))**2)
    arg = (np.pi/4)*(depth/zone_height)
    x = 1 + (np.tan(arg))**2
    fd = density - density_top*np.sqrt(x)
    
    return fd