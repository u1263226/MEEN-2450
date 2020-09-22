# -*- coding: utf-8 -*-
"""
MEEN 2450 Lab 3: RPSround function
Kristen Pimentel
u1263226
22 September 2020

"""

def RPSround(userChoice,computerChoice):
    #paper beats rock
    #rock beats scissors
    #scissors beats paper
    #lizard Spock?
    if userChoice == 'r':
        if computerChoice == 's':
            roundResult = 1
        elif computerChoice == 'p':
            roundResult = -1
        elif computerChoice == 'r':
            roundResult = 0
    elif userChoice == 'p':
        if computerChoice == 's':
            roundResult = -1
        elif computerChoice == 'p':
            roundResult = 0
        elif computerChoice == 'r':
            roundResult = 1
    elif userChoice == 's':
        if computerChoice == 's':
            roundResult = 0
        elif computerChoice == 'p':
            roundResult = 1
        elif computerChoice == 'r':
            roundResult = -1
    
    return roundResult #user result win = 1/loss = -1/draw = 0