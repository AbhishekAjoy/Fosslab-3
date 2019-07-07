# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 21:04:43 2019

@author: Abhishek
"""

import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:,0:1].values #indepenent
Y = dataset.iloc[:,1].values#dependent
xm = 0
ym = 0
a = 0
b = 0
for i in range(30):
    xm = xm + X[i]/30
    ym = ym + Y[i]/30
for i in range(30):
    a = a + (Y[i]-ym)*(X[i]-xm)
    b = b + (X[i]-xm)*(X[i]-xm)
w1 = a/b
w0 = ym - w1*xm
print(w1)
print(w0)

plt.scatter(X,Y,color = 'red')
plt.plot(X,w1*X+w0, color = 'blue')
plt.show()
