#Hydrogen energy.  D. Barton 11/20/2021
import numpy as np
import random
#import matplotlib.pyplot as plt

# Limits of integration
a = 0
b = 4
N = 10 #Steps

#define the displacement 'r' and the energy function 'v'

for i in range(N):
    r = random.uniform(a,b)
    dr = random.uniform(-0.05,0.05)
    r0 = r + dr

    if r != 0:
        v_old = -1/r

    def psi(r): #original wavefunction Hydrogen
        return r**2*np.exp(-2*r)
    def psi_0(r0): #new wavefunction Hydrogen
        return r0**2*np.exp(-2*r0)
    dpsi = psi(r)/psi_0(r0)

    if psi_0(r0) >= psi(r): #accept if new psi is larger than old
        i = i + 1
        v_new = v_old + (-1/r0)
        v_old = v_new
        r = r0

    elif dpsi <= random.uniform(0,1): #also accept if
        i = i + 1
        v_new = v_old + (-1/r0)
        v_old = v_new
        r = r0

    else:
        i = i + 1
        v_new = v_old - (-1/r)
        v_old = v_new

    v_new = (v_old)/i

print(v_new)
