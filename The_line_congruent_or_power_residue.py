#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 10:12:54 2021

@author: andres
"""

#THE LINE CONGRUENT OR POWER RESIDUE

from matplotlib import pyplot as plt
import numpy as np
import math

c = 1;
a = 57;
M = 256;



math.modf(M)

def lcg(x, seed):
    cont = 0;
    """Linear congruential generator."""
    while cont < x:
        cont = cont +1
        seed = (a * seed + c) % M
    return seed


x = np.linspace(0,1000,1000)
y = [lcg(i, 10) for i in x]
i_pl = range(1,500)

x_pl = [y[2*i-1] for i in i_pl]
y_pl = [y[2*i] for i in i_pl]

fig = plt.scatter(x_pl,y_pl, lw = 0)


    