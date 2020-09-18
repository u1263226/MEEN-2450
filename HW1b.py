# -*- coding: utf-8 -*-
"""
Kristen Pimentel
u1263226
MEEN 2450 HW 1b
17 September 2020

"""
import math
import numpy as np
import pandas as pd
from math import e

#The quantity e^-5 can be determined two ways
#f1 => e^-x = 1 - x + x^2/2! + x^(n+1)/(n+1)!
#f2 => e^-x = 1/(1+x+x^2/2!+x^(n+1)/(n+1)!)

total = 0
x = 5
true_val = e**(-5)
s = 1
x_r = []
et_r = []
ea_r =[]
#Evaluate f1 from 1-20 terms
for i in range(0,20):
    total_p = total
    total = total + s*(x**(i))/math.factorial(i) #add next term in series
    s = s*-1 #oscilating sign factor
    if total!=0:
        e_t = ((true_val - total)/total)*100 #Calculate the true error
        e_a = ((total-total_p)/(total))*100 #Calculate relative error
    else:
        e_t = ((true_val - total))*100 #True error w/o dividing by 0
        e_a = ((total-total_p))*100 #Approx error w/o dividing by 0
    x_r.append(total) #store the current total in an array
    et_r.append(e_t) #store the true error in an array
    ea_r.append(e_a) #store the approximate error in an array

x = 5
total = 0
total_inv = 0
x2_r = []
et2_r = []
ea2_r = []

#Evaluate f2 from 1-20 terms
for i in range(0,20):
    total_p = total_inv
    total = total + (x**(i))/math.factorial(i) #add next term in series
    total_inv = 1/total #inverse of the sum
    if total_inv!=0:
        e_t = ((true_val - total_inv)/total_inv)*100 #Calculate the true error
        e_a = ((total_inv-total_p)/(total_inv))*100 #Calculate relative error
    else:
        e_t = ((true_val - total_inv))*100 #True error w/o dividing by 0
        e_a = ((total_inv-total_p))*100 #Approx error w/o dividing by 0
    x2_r.append(total_inv) #store the current total in an array
    et2_r.append(e_t) #store the true error in an array
    ea2_r.append(e_a) #store the approximate error in an array


#report results in a table using a dataframe
data = {'value1':x_r,'e_t1 (%)':et_r,'e_a1 (%)':ea_r,'value2':x2_r,'e_t2 (%)':et2_r,'e_a2 (%)':ea2_r}
df = pd.DataFrame(data)
print(df) #print results table

