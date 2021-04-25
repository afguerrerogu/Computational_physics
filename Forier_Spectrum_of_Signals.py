#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 10:46:46 2021

@author: andres
"""

import numpy as np
from matplotlib import pyplot as plt 
import  seaborn as sns
sns.set()

c1 = 1j 
N = 30
# Funcion
a = 1;
n = int(N/2)

def function(x):
    return np.exp(a*x*c1/N)


#Definimos los nodos

x_j = [2*np.pi*i/N for i in range(0, N)]
k = [x for x in range(-n,n)]

   
# Transformacion discreta de Forier (DFT)


def DFT(k, N):
    # La funcion DTF recibe como paramentros:
    # k la variable independiente
    # N numero de pasos
    x_j = [2*np.pi*i/N for i in range(0, N)]
    fk = 0
    for x in x_j:
        fk += (1/N)*(function(x)*np.exp(-c1*k*x))
    return fk

#transformada teorica
def TEO(k, a, N):
    fk = (1/N)*((np.exp(1j*a)-1)/(np.exp(1j*(a-2*np.pi*k))-1))
    return fk

Re_DFT = [np.real(DFT(j,N)) for j in k]
Im_DFT = [np.imag(DFT(j,N)) for j in k]

Re_teorico = [np.real(TEO(j,a,N)) for j in k]
Im_teorico = [np.imag(TEO(j,a,N)) for j in k]
                 
plt.plot(figsize=(15,15))
plt.plot(x_j, Re_DFT,'-.',lw=0.5,label=r'$DFT_{Re}$', )
plt.plot(x_j, Im_DFT, '-.',lw = 0.5, label=r'$DTF_{Im}$')
plt.plot(x_j, Re_teorico,'-', label='$Teo_{Re}$')
plt.plot(x_j, Im_teorico,'-',label='$teo_{Im}$')
plt.legend()

plt.savefig('fourier.pdf')
               
   
    