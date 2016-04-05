"""
File: nonlinear_ODE.py
Copyright (c) 2016 Andrew Malfavon
License: MIT
Course: PHYS227
Assignment: C.1 / C.2
Date: March 31, 2016
Name: Andrew Malfavon
Description: 
"""

import numpy as np
import matplotlib.pyplot as plt
import Euler as p1

def uprime(q):
    return lambda x, u: u**q

#solves the ODE for a given q, dt mesh between t=0 and t=T, and an initial u(0)
def solve(q, dt, f0):
    if q == 1:
        T = 6
    else:
        T = 1 / (q - 1) - 0.1
    return p1.euler(uprime(q), f0, np.arange(0, T, dt))

def graph(f, xmin, xmax, ymin, ymax, n = 100):
    x_values = np.linspace(xmin, xmax, n)
    t = x_values
    if q == 1:
        y_exact = np.exp(t)
    else:
        y_exact = (t * (1 - q) + 1)**(1 / (1 - q))
    y_values = f(x_values)
    plt.plot(t, y_exact)
    plt.plot(t, y_values)
    plt.title('u(t)')
    plt.xlabel('t')
    plt.ylabel('u')
    plt.xlim(xmin, xmax)
    plt.ylim(ymin, ymax)