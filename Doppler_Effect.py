#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 19:55:09 2021

@author: andres
"""

#from Forier_Spectrum_of_Signals import DTF
from scipy import optimize
from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns
sns.set()

# Parametros

A = 1       # amplitud
v = 100     # velocidad radial [m/s]
L = 10.5    # Distancia al  [m] 
R = 10      # Radio [m]
w = 1000    # velocidad angular [1/s] 
c = 340     # velocidad [m/s]
N = 1000

omega = v/R
l = omega*L / c
r = omega*R / c


t_inicial = 0
t_fin = 2*np.pi/10 
t = np.linspace(t_inicial,2*t_fin,N)    # Pasos



# x function

def x_equ(x,t):
    return pow(l,2) + pow(r, 2) + 2*l*r*np.sin(t-x)-pow(x,2)

x = np.zeros(N)
for i in range(0, N):
    x[i] = optimize.bisect(x_equ, 0, 10, args = (t[i]*omega))



def pressure_difference(t):
    return A*((np.cos(w*(t-(optimize.bisect(x_equ,0,2, args = omega*t)/c))))
              /optimize.bisect(x_equ,0,2, args = omega*t))

def f_j(j):
    fj = [pressure_difference(j*t) for t in t]
    return fj        
        

# fig, ax = plt.subplots(figsize=(15,15))
# for j in N-1:
#     ax.plot.scatter(delta_t,f_j(j))

    
#deltap = [np.abs(f_j(j))for j in t]

#plt.scatter(t,deltap)
#plt.ylim(1,10**2)
#plt.yscale('log')
#plt.ylim(1,10**2)
#plt.savefig('dopler.jpeg')



# plt.plot(x_gra, pow(l,2) + pow(r, 2) + 2*l*r*np.sin(T-X))
# plt.plot(x_gra, pow(X,2))
# #plt.plot(x,x_equ(X,T))
# plt.show()



