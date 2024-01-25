# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 11:48:27 2023

@author: ecurry
"""
import numpy as np
import matplotlib.pylab as plt
import math

transient = 5000

def f(theta ,w, t) :
    x = -(g/L)*math.sin(theta) - (k*w) + (A*math.cos(phi * t))
    return x

g = 9.8
L = 9.8
k = 0.5
w = 0
phi = 0.66667
A = 1.5


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

while n_steps < 200000:
    
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
    shift = theta + 5
    
    if  n_steps > transient:
        if (shift > np.pi + 5):
            theta -= 2 * np.pi * np.abs(theta) / theta
            theta = theta + 5
            nl_t_arr.append(t)
            nl_theta_arr.append(theta)
            nl_w_arr.append(omega)
        elif (shift < -np.pi +5):
            theta -= 2 * np.pi * np.abs(theta) / theta
            theta = theta + 5
            nl_t_arr.append(t)
            nl_theta_arr.append(theta)
            nl_w_arr.append(omega)
        else:
            nl_t_arr.append(t)
            nl_theta_arr.append(theta)
            nl_w_arr.append(omega) 
    
    

    

plt.plot(nl_t_arr,nl_theta_arr)
plt.show()

plt.plot(nl_t_arr,nl_w_arr)
plt.show()


plt.scatter(nl_theta_arr,nl_w_arr, s=1)
plt.xlabel("theta")
plt.ylabel("omega")
plt.title("theta vs omega")
plt.savefig("p5.pdf")
plt.show()