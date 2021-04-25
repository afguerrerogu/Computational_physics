#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 13:18:00 2021

@author: andres
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.tree import DecisionTreeRegressor

data = pd.read_csv('ionosphere.data',index_col = False, #[str(i) for i in range(351)],
                   names = [str(i) for i in range(35)])

data = data.drop(['1'],axis=1)

data = data.replace({'g':1,'b':-1})
result = data['34']
data = data.drop(['34'],axis=1)


histo = []
for i in data.index:

    Data_test = np.matrix(data.iloc[i].tolist())
    Data_train = data.drop([i],axis=0).values.tolist()
    resul_test = result.iloc[i].tolist()
    resul_train = result.drop([i],axis=0).tolist()
    
    dec_tree = DecisionTreeRegressor()
    dec_tree.fit(Data_train, resul_train)
    predic = dec_tree.predict(Data_train)
    histo.append(predic)
    
    
#    histo.append(L(Data_train,Data_test))