# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 15:09:59 2020

@author: kshay

Fibbonacci sequence function
"""
#Create a functionfibonacci(N)that returns an array of length N 
#containing the first N terms of the Fibonacci sequence.
import numpy as np

def fibonacci(N):
    n = 0
    P = [0,1]
    for i in range(2,N):
        P.append(P[i-2]+P[i-1])
        
    return P