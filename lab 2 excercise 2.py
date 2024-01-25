# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 12:17:30 2023

@author: ecurry
"""

import numpy as np
import matplotlib.pylab as plt
import math

g = 9.8
L = 9.8
k = 0.0
w = 0
phi = 0.66667
A = 0.0

theta = 0.2
omega = 0.0
t = 0.0
dt = 0.01
n_steps = 0

theta_arr = []
w_arr = []
n_arr = []
t_arr = []

def trag(theta ,w, t) :
    x = -(g/L)*math.sin(theta) - (k*w) + (A*math.cos(phi * t))
    return x
