
import numpy as np
import matplotlib.pylab as plt
import math

g = 9.8
L = 9.8
k = 0.0
w = 1.0
phi = 0.66667
A = 0.0

theta = 0.0
omega = 1.0
t = 0.0
dt = 0.01
n_steps = 0

theta_arr = []
w_arr = []
n_arr = []
t_arr = []

def trag(theta ,w, t) :
    x = -(g/L)*(theta) - (k*w) + (A*math.cos(phi * t))
    return x

def non_lin_trag(theta ,w, t) :
    x = -(g/L)*math.sin(theta) - (k*w) + (A*math.cos(phi * t))
    return x
"""  
f_arr = []

while n_steps < 5 :   # this checks if the code works
    f_arr.append(trag(theta,w, t))
    t += 1
    w += 1
    theta += 1
    n_steps += 1
    
print(f_arr)   
"""

while n_steps < 1000:
    
    t_arr.append(t)
    theta_arr.append(theta)
    w_arr.append(w)
    n_arr.append(n_steps)
    q = trag(theta, w, t)
    theta = theta + w*0.5*dt + (w + q*dt)*0.5*dt
    w = w + q*0.5*dt + trag(theta, w + q*dt, t + dt)*0.5*dt
    t += dt
    n_steps += 1
    
    

l_nw = plt.plot(n_arr,w_arr)
plt.xlabel("number of steps")
plt.ylabel("angular frequency")
plt.axis([0, 500, -np.pi, np.pi])

plt.show()

l_nt = plt.plot(n_arr,theta_arr)
plt.xlabel("number of steps")
plt.ylabel("angle")
plt.axis([0, 500, -np.pi, np.pi])

plt.show()



plt.plot(t_arr,theta_arr)
plt.xlabel("time")
plt.ylabel("angle (degrees)")
plt.title("theta vs time")

plt.show()


plt.plot(t_arr,w_arr)
plt.xlabel("time")
plt.ylabel("angular frequency (degrees per second)")
plt.title("omega vs time")


plt.show()

g = 9.8
L = 9.8
k = 0.0
w = 1.0
phi = 0.66667
A = 0.0

theta = 0.0
omega = 1.0
t = 0.0
dt = 0.01
n_steps = 0

nl_theta_arr = []
nl_w_arr = []
nl_n_arr = []
nl_t_arr = []

e = non_lin_trag(theta ,w, t)

while n_steps < 1000:
    
    nl_t_arr.append(t)
    nl_theta_arr.append(theta)
    nl_w_arr.append(w)
    q = non_lin_trag(theta, w, t)
    theta = theta + w*0.5*dt + (w + e*dt)*0.5*dt
    w = w + q*0.5*dt + non_lin_trag(theta, w + q*dt, t + dt)*0.5*dt
    t += dt
    n_steps += 1


plt.plot(n_arr,theta_arr,n_arr,nl_theta_arr)
plt.show()

plt.plot(t_arr,theta_arr,nl_t_arr,nl_theta_arr)
plt.xlabel("time")
plt.ylabel("theta")
plt.title("theta vs time")
plt.savefig("p2.4 theta.pdf")

plt.show()



plt.plot(t_arr,w_arr,nl_t_arr,nl_w_arr)
plt.ylabel("omega")
plt.xlabel("time")
plt.title("omega vs time")
plt.savefig("p2.4 omega.pdf")

plt.show()



