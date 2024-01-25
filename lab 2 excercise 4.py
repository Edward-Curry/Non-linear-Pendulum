# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 11:16:24 2023

@author: ecurry
"""

import numpy as np
import matplotlib.pylab as plt
import math

def f(theta ,w, t) :
    x = -(g/L)*math.sin(theta) - (k*w) + (A*math.cos(phi * t))
    return x

g = 9.8
L = 9.8
k = 0.5
w = 0
phi = 0.66667
A = 0.0

theta = 3.0
omega = 0.0
t = 0.0
dt = 0.01
n_steps = 0

nl_theta_arr = []
nl_w_arr = []
nl_n_arr = []
nl_t_arr = []





e = f(theta ,w, t)

while n_steps < 10000:
    
    nl_t_arr.append(t)
    nl_theta_arr.append(theta)
    nl_w_arr.append(omega)
    q = f(theta, w, t)
    k1a = dt * omega 
    k1b = dt * f(theta, omega, t)
    k2a = dt * (omega + k1b/2)
    k2b = dt * f(theta + k1a/2, omega + k1b/2, t + dt/2)
    k3a = dt * (omega + k2b/2)
    k3b = dt * f(theta + k2a/2, omega + k2b/2, t + dt/2)
    k4a = dt * (omega + k3b)
    k4b = dt * f(theta + k3a, omega + k3b, t + dt)
    theta = theta + (k1a + 2*k2a + 2*k3a + k4a) / 6
    omega = omega + (k1b + 2*k2b + 2*k3b + k4b) / 6
    n_steps += 1
    t += dt
    
g = 9.8
L = 9.8
k = 0.5
phi = 0.66667
A = 0.0

theta = 3.0
omega = 0.0
tt = 0.0
dt = 0.01
nt_steps = 0

nlt_theta_arr = []
nlt_w_arr = []
nlt_n_arr = []
nlt_t_arr = []

while nt_steps < 10000:
    
    
    nlt_t_arr.append(tt)
    nlt_theta_arr.append(theta)
    nlt_w_arr.append(w)
    q = f(theta, w, t)
    theta = theta + w*0.5*dt + (w + e*dt)*0.5*dt
    w = w + q*0.5*dt + f(theta, w + q*dt, t + dt)*0.5*dt
    tt += dt
    nt_steps += 1
    

plt.plot(nlt_t_arr,nlt_theta_arr,nl_t_arr,nl_theta_arr)
plt.xlabel("time")
plt.ylabel("theta")
plt.title("theta vs time")
plt.savefig("p4 theta vs time.pdf")
plt.show()

plt.plot(nlt_t_arr,nlt_w_arr,nl_t_arr,nl_w_arr)
plt.xlabel("time")
plt.ylabel("omega")
plt.title("omega vs time")
plt.savefig("p4 omega vs time.pdf")
plt.show()