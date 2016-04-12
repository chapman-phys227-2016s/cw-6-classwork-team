"""
File: nonlinear_ODE.py
Copyright (c) 2016 Andrew Malfavon
License: MIT
Course: PHYS227
Assignment: C.1 / C.2
Date: March 31, 2016
Name: Andrew Malfavon
Description: solves a nonlinear ODE using Euler's method
and plots the approximation and the known exact solution.
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
        T = (1 / float(q - 1)) - 0.1
    return p1.euler(uprime(q), f0, np.arange(0, T, dt))

#graphs the approximation and the exact solution together
def graph(q, dt, f0):
    y_approx = solve(q, dt, f0)
    if q == 1:
        T = 6
        t = np.arange(0, T, dt)
        y_exact = np.exp(t)#known exact solution for this case
    else:
        T = (1 / float(q - 1)) - 0.1
        t = np.arange(0, T, dt)
        y_exact = (t * (1 - q) + 1)**(1 / (1 - q))#known exact solution
    plt.plot(t, y_exact, label = 'Exact Solution')
    plt.plot(t, y_approx, label = 'Approximation')
    plt.title('Nonlinear ODE Approximation and Exact Solution')
    plt.xlabel('t')
    plt.ylabel('u')
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)