# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 14:41:34 2020

@author: kshay

ChooseArray
"""
# This function generates an array based on the input of (row,cols,"true/false")
# when "true" the array increases across the row
# when "false" the array increases down the columns 

import numpy as np
import math

def ChooseArray(N,M,row_orient):
    if row_orient == "true":
        #row array
        r = np.zeros((N,M)).astype(int)
        for i in range(N):
            for j in range(M):
                r[i][j] = (j+1)+M*(i)
      # print(r)
        
    else:
        #column array
        r = np.zeros((N,M)).astype(int)
        for i in range(N):
            for j in range(M):
                r[i][j] = (i+1)+N*(j)
       # print(r)
        
    return r