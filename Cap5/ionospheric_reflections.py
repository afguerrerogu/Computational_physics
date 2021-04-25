#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 09:54:57 2021

@author: andres
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

data = pd.read_csv('ionosphere.data',index_col = False, #[str(i) for i in range(351)],
                   names = [str(i) for i in range(35)])

data = data.drop(['1'],axis=1)

def Sxx_(data, x):
    Sxx = np.zeros((33,33))
    for i in data.iterrows():
        desv = i[1].to_numpy()-x
        desv = np.matrix(desv)
        desv_t = np.transpose(desv)
        desv_to = np.matmul(desv_t,desv)
        Sxx += desv_to
    return Sxx
    


def L(Data_train, Data_test):
    
    datos_buenos = Data_train[Data_train["34"]=='g']
    datos_malos = Data_train[Data_train["34"]=='b']
    datos_buenos = datos_buenos.drop(['34'],axis=1)
    datos_malos = datos_malos.drop(['34'],axis=1)
    
    
    x1 = np.array([datos_buenos[medida].mean() for medida in datos_buenos])
    x2 = [datos_malos[medida].mean() for medida in datos_malos]
    x1_t = np.transpose(x1)
    x2_t = np.transpose(x2)
    
    n1 = len(datos_buenos)
    n2 = len(datos_malos)
    
    Sxx1 = Sxx_(datos_buenos,x1)
    Sxx2 = Sxx_(datos_malos,x2)    
    
    Sxx = (1/(n1+n2))*(Sxx1+Sxx2)
    Sxx_in = np.linalg.inv(Sxx)
    
    x1 = np.matrix(x1)
    x2 = np.matrix(x2)
    x1_t = np.transpose(x1)
    x2_t = np.transpose(x2)
    
    arg_1 = np.matmul(x1,Sxx_in)
    arg_2 = np.matmul(arg_1,x1_t)
    
    arg_3 = np.matmul(x2,Sxx_in)
    arg_4 = np.matmul(arg_3,x2_t)
    
    a_0 = (1/2)*(arg_2 - arg_4)+np.log10(n1/n2)
    a = np.matmul(Sxx_in,np.transpose(x1-x2))
    a_t = np.transpose(a)
    
    L = a_0 + np.matmul(a_t,Data_test)
    return L.tolist()[0]

histo = []
for i in data.index:    
    Data_test = data.iloc[i].to_numpy()
    Data_test = np.delete(Data_test,33)
    Data_train = data.drop([i],axis=0)
    histo.append(L(Data_train,Data_test))
    
plt.hist(histo)
plt.show()
