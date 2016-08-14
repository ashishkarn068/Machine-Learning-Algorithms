# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 20:05:39 2016

A very basic implementation of Linear Regression Model

@author: Ashish
"""

from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import random

# Style for the graph

style.use('fivethirtyeight')                                    


# Below is the function to generate a desired random data set that returns two array 'xs' and 'ys'

def create_dataset(howmany, variance, step=2, correlation=False):     
    val = 1
    ys = []
    for i in range(howmany):
        y = val + random.randrange(-variance, variance)
        ys.append(y)
        if(correlation and correlation=='pos'):
            val+= step
        elif(correlation and correlation=='neg'):
            val-= step
        
    xs = [i for i in range(len(ys))]
    
    return np.array(xs, dtype=np.float64), np.array(ys, dtype=np.float64)
    

#xs = np.array([1, 2, 3, 4, 5, 6, 12, 7,10, 11], dtype=np.float64)
#ys = np.array([5, 4, 8, 9, 15, 11, 19, 13, 17, 21], dtype=np.float64)


# Random stored in xs and ys

xs, ys = create_dataset(100, 50, 2, correlation='pos')

print xs, ys

# Function to obtain best fit slope(m) and y intercept(b) of a regression line using data stored in xs and ys

def best_fit_slope_intercept(xs, ys):
    x_mean = mean(xs)
    y_mean = mean(ys)
    
    numerator = (x_mean*y_mean) - (mean(xs*ys))
    denominator = (x_mean**2) - mean(xs**2)
    
    m = numerator / denominator
    b = mean(ys) - m*mean(xs)
   
    return m,b
    
    
# Function to calculate sum of squared error

def squared_error(ys_orig, ys_line):
    #print ys_orig - ys_line
    return sum((ys_orig - ys_line)**2)


# Function to determine the value of coefficient of determination that determines how good the regression line is (Higher value is better)

def coefficient_of_determination(ys_orig, ys_line):
    ys_mean_line = mean(ys_orig)
    #print ys_mean_line
    squared_error_regr = squared_error(ys_orig, ys_line)
    #print "squared Error Regression -->" + str(squared_error_regr)
    squared_error_mean = squared_error(ys_orig, ys_mean_line)
    #print "squared Error Mean -->" + str(squared_error_mean)
    
    return 1 - (squared_error_regr/ squared_error_mean)

m,b = best_fit_slope_intercept(xs,ys)
print m,b

# regression_line storing value of y for every x in xs to generate regression line

regression_line = [ m*x + b for x in xs]

# Taking few values for prediction or testing
predict_x = [17, 19, 20]
predict_y = [m*i + b for i in predict_x]


# Storing coefficient of determination in variable r_squared

r_squared = coefficient_of_determination(ys, regression_line)
print r_squared

plt.scatter(xs,ys)
plt.scatter(predict_x, predict_y,s=100, color='g')
plt.plot(xs,regression_line)
plt.show()


        

