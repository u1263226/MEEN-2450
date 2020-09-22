# -*- coding: utf-8 -*-
"""
MEEN 2450 Lab 3
Kristen Pimentel
u1263226
22 September 2020

"""
import numpy as np
import matplotlib.pyplot as plt
import random

#Rock Paper Scissors
maxRounds = 50 #limit the amount of playable rounds
cc = np.array(["r","p","s"])
ua = [] #user choice array
ca = [] #computer choice array
uw = [] #user win array
tr = 0 #initialize total rounds played
r = 0
while r<maxRounds:
    r = r + 1
    c = random.choice(cc) #computer chooses randomly amoung rock papaer and scissors
    u = input("Choose rock, paper or scissors: ") #ask for user input: rock paper scissors
    if u == "stop": #game plays until user inputs stop OR max # of rounds has been played(15)
         print("Stopping now") 
         r = maxRounds
         break
    elif u == "r":
        tr = tr + 1
    elif u == "p":
        tr = tr + 1
    elif u == "s":
        tr = tr + 1
    else:
        print("User input is invalid")#generate an error if an invalid input is given and ask for correct input
        continue #invalid results do not contribute to play statistics

    result = RPSround(u,c) #win/lose/draw
    print("The user chose ",u)
    print("The computer chose ",c)
    if result == 1: #display resuts of each round
        print("The user won")
    elif result == -1:
        print("The user lost")
    else:
        print("It was a tie")

    uw.append(result) #keep win/lose/draw in an array
    ua.append(u) #keep user input in an array
    ca.append(c) #keep random computer input in an array

print("There were ",str(tr),"rounds played")#total amount of rounds played
win = 0
lose = 0
draw = 0
for i in range(len(uw)):
    if uw[i] == 1:
        win = win + 1
    elif uw[i] == -1:
        lose = lose + 1
    else:
        draw = draw + 1
wp = win/len(uw)*100 #user win/loss/draw %
lp = lose/len(uw)*100
dp = draw/len(uw)*100
print("The user won ",round(wp),"% of the time")
print("The user lost ",round(lp),"% of the time")
print("The user tied ",round(dp),"% of the time")

r = 0
p = 0
s = 0
for i in range(len(ua)):
    if ua[i] == 'r':
        r = r + 1
    elif ua[i] == 'p':
        p = p + 1
    else:
        s = s + 1
rp = r/len(ua)*100 #choice % for user
pp = p/len(ua)*100
sp = s/len(ua)*100
print("The user chose rock ",round(rp),"% of the time")
print("The user chose paper ",round(pp),"% of the time")
print("The user chose scissors ",round(sp),"% of the time")

r = 0
p = 0
s = 0
for i in range(len(ca)):
    if ca[i] == 'r':
        r = r + 1
    elif ca[i] == 'p':
        p = p + 1
    else:
        s = s + 1
rp = r/len(ca)*100 #choice % for computer
pp = p/len(ca)*100
sp = s/len(ca)*100
print("The computer chose rock ",round(rp),"% of the time")
print("The computer chose paper ",round(pp),"% of the time")
print("The computer chose scissors ",round(sp),"% of the time")

#Extra credit plot
#create arrays of win/loss/draw %
uwp = [0]
ulp = [0]
udp = [0]
tr = [0]
wp = 0
lp = 0
dp = 0
win = 0
lose = 0
draw = 0
for i in range(len(uw)):
    if uw[i] == 1:
        win = win + 1 
    elif uw[i] == -1:
        lose = lose + 1
    else:
        draw = draw + 1

    wp = win/len(uw)*100
    lp = lose/len(uw)*100
    dp = draw/len(uw)*100

    uwp.append(wp)
    ulp.append(lp)
    udp.append(dp)
    tr.append(i)
    
#plot the user win/loss/draw % as a function of the number of rounds played
plt.plot(tr,uwp, color = "green",label = "User win %")
plt.plot(tr,ulp, color = "red",label = "User loss %")
plt.plot(tr,udp, color = "blue",label = "User draw %")
plt.title("Users Win/Loss/Draw % vs. Round")
plt.xlabel("Number of rounds played")
plt.ylabel("%")
plt.legend()
plt.show()





