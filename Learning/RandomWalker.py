# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 15:16:37 2017

@author: Malek
"""

import numpy as np
#import scipy as sp
import matplotlib.pyplot as plt

def MCSimRandomWalk(Vol, Time, RandMatrix):
    """ run random walk simulations with a constant volatility or a vector of volatility/time """
    
    RandomWalk = []    

    for j in range(0,len(Time)):
        TimeResults = []
        for i in range(0, len(RandMatrix)):
            if j == 0:
                TimeResults.append(1.0)    
            else:
                if isinstance(Vol, list):
                    TimeResults.append(RandomWalk[j-1][i] + Vol[j] * Time[j] * RandMatrix [j][i])
                else:
                    TimeResults.append(RandomWalk[j-1][i] + Vol * Time[j] * RandMatrix [j][i])
            
            RandomWalk.append(TimeResults)
            
    return RandomWalk
    

Time = []
EndHorizon = 1.0
Number_Of_TimeSteps = 40
Number_Of_Simulations = 100

for i in range(0,Number_Of_TimeSteps):
    Time.append(i/EndHorizon)
    
RandomMatrix = np.random.normal(0, 1, (Number_Of_TimeSteps, Number_Of_Simulations))

Sigma = 0.01

RW = MCSimRandomWalk(Sigma, Time, RandomMatrix)

plt.figure(1)
plt.clf()
plt.plot(RW)

#for SimPath in RW:
#    plt.plot(Time, SimPath)
    

plt.figure(2)
plt.clf()
n = 2048
X = np.random.normal(0, 1, n)
Y = np.random.normal(0, 1, n)
T = np.arctan2(Y, X)

plt.axes([0.025, 0.025, 0.95, 0.95])
plt.scatter(X, Y, s=75, c=T, alpha=.5)

plt.xlim(-1.5, 1.5)
plt.xticks(())
plt.ylim(-1.5, 1.5)
plt.yticks(())

plt.show()