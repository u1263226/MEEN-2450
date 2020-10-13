# -*- coding: utf-8 -*-
"""
Kristen Pimentel
u1263226 
MEEN 2450: Lab 6
13 October 2020
"""

#Organize pipe data 
g = 9.81
deltaP0 = 100*10**3 #kPa
mu = 1*10**(-3)
ro = 1*10**3
pipeNames = ["AB","BG","CF","DE","GH","BC","CD","EF","FG"]
lengths = [5,5,5,5,5,10,10,10,10] #m
diameters = [0.01,0.005,0.002,0.003,0.005,0.005,0.0035,0.0025,0.0045] #m
pipeData = {}
b = [0,0,deltaP0,0,0]

for idx, key in enumerate(pipeNames):
    pipeData[key] = {} # add a dict inside of pipeData
    pipeData[key]['l'] = lengths[idx] # add pipe quantities to the nested dictionary
    pipeData[key]['D'] = diameters[idx]

for idx, key in enumerate(pipeData):
    pipeData[key]['R'] = 128*(mu*(pipeData[key]['l']))/(np.pi*(pipeData[key]['D'])**4)

A = np.zeros([5,5])
A[0][0] = 1
A[0][1] = -1
A[0][2] = -1
A[0][3] = 0
A[0][4] = 0
A[1][0] = 0
A[1][1] = 1
A[1][2] = 0
A[1][3] = -1
A[1][4] = -1
A[2][0] = pipeData['AB']['R'] + pipeData['GH']['R']
A[2][1] = 0
A[2][2] = pipeData['BG']['R']
A[2][3] = 0
A[2][4] = 0
A[3][0] = 0
A[3][1] = -1*(pipeData['BC']['R']) - (pipeData['FG']['R'])
A[3][2] = (pipeData['BG']['R']) #the same as GB because its the same pipe, resistance is not directional
A[3][3] = -1*(pipeData['CF']['R'])
A[3][4] = 0
A[4][0] = 0
A[4][1] = 0
A[4][2] = 0
A[4][3] = (pipeData['CF']['R']) #the same as FC because its the same pipe, resistance is not directional
A[4][4] = -1*(pipeData['CD']['R'] + pipeData['DE']['R'] + pipeData['EF']['R'])

x = naive_gauss_elimination(A,b)

print("Q0,Q1,Q2,Q3,Q4:",x)


#Calculate the flow in each pipe
pipeData['AB']['Q'] = x[0]
pipeData['BG']['Q'] = x[2]
pipeData['CF']['Q'] = x[3]
pipeData['DE']['Q'] = x[4]
pipeData['GH']['Q'] = x[2]+x[3]+x[4]
pipeData['BC']['Q'] = x[1]
pipeData['CD']['Q'] = x[4]
pipeData['EF']['Q'] = x[4]
pipeData['FG']['Q'] = x[3]+x[4]


#Calculate the Reynolds number of each pipe, report if flow is laminar or turbulent
for idx, key in enumerate(pipeData):
    print("Q of",key,"=",pipeData[key]['Q'],"m**3/s")
    pipeData[key]['V'] = ((pipeData[key]['Q']))/(np.pi*(pipeData[key]['D'])**2/4)
    print("V of",key,"=",pipeData[key]['V'],"m/s")
    pipeData[key]['Re'] = (ro*(pipeData[key]['V'])*(pipeData[key]['D']))/mu
    print("Re of",key,"=",pipeData[key]['Re'])
    pipeData[key]['Flow Condition'] = "Laminar" 
    if pipeData[key]['Re'] > 2000:     
        pipeData[key]['Flow Condition'] = "Turbulent"
    print()

#report results in a table using a dataframe
#data = {"r(m)":r,"h(m)":h,'Volume(m^3)':V,'Pressure(Pa)':p,'Exergy(J)':X,'Avg D Force(N)':F}
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth',-1)
pd.set_option('display.max_columns', None)

df = pd.DataFrame(pipeData)
print(df) #print results table



"""
Using a smaller system of equations and verifying by hand calculations that my program calculated the correct x values so they
match my solution I can then assume wothout calclating by hand that the flow, or Q is correct according to my gauss elimination 
function. This is my check on the given values in the table. I could also check my answers by plugging in the solution to the 
original equation to ensure that the solution is = 0. In the lab assignment the equations (12) should be evaluated to be 0. 

"""
