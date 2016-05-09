# -*- coding: utf-8 -*-
"""
Created on Mon May  9 13:15:29 2016

@author: Pablo Aragón Moreno, Juan Antonio Palacios Galván
"""

import pandas

operations = pandas.read_csv("operaciones/allData.csv")

#mapping functions
def time_to_ms(x):
    return (x * 1000).astype(int)

print "Checkpoint 0"

operations.loc[operations["op"] == '+', "op"] = 0
operations.loc[operations["op"] == '-', "op"] = 1
operations.loc[operations["op"] == '*', "op"] = 2
operations.loc[operations["op"] == '/', "op"] = 3
operations.time = operations.time.map(time_to_ms)

print "Checkpoint 1"

from sklearn.linear_model import LinearRegression

predictors = ["op1", "op", "op2"]

alg = LinearRegression()

print "Checkpoint 2"
    
from sklearn import cross_validation
from sklearn.linear_model import LogisticRegression

alg = LogisticRegression(random_state=1)

print "Checkpoint 3"

scores = cross_validation.cross_val_score(alg, operations[predictors], operations["time"], cv = 10, scoring='mean_absolute_error')
print "Predictions done with accuracy of: ", scores.mean(), "\n"

print "Done."


