#! /usr/bin/env python

"""
File: Euler.py
Copyright (c) 2016 Austin Ayers
License: MIT

Course: PHYS227
Assignment: C.1 / C.2
Date: March 31, 2016
Email: ayers111@mail.chapman.edu, 
Name: Austin Ayers, 
Description: Implements Euler's method for solving linear and non-linear ODE's
"""

import numpy as np
from sympy import Function, dsolve, Eq, Derivative, sin, cos, symbols
from sympy.abc import x

def c1func(q):
    """
    function for problem C.1 to solve
    """
    return (lambda x, u: 2 * u - 1)
def euler(df, f0, x):
    """
    Implements the forward Euler's method
    """
    f = np.zeros(len(x))
    dx = x[1] - x[0]
    f[0] = f0
    for i, elem_x in enumerate(x):
        if i == len(x) - 1:
            break
        f[i+1] = (f[i] + dx * df(elem_x, f[i]))
    return f

def symbolic_solve():
    """
    Solves the problem symbolically using sympy
    """
    f = Function('f')
    sol = dsolve(2 * Derivative(f(x), x, x) - 1, f(x))
    print sol
def run():
    x_mesh = np.linspace(0, 6, 24)
    y = euler(c1func, 2, x_mesh)
    print y
    symbolic_solve()
def test_euler():
    """
    Euler test function to ensure proper behavior
    """