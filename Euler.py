#! /usr/bin/env python

"""
File: adaptive_trapezint.py
Copyright (c) 2016 Austin Ayers
License: MIT

Course: PHYS227
Assignment: C.1
Date: Feb 11, 2016
Email: ayers111@mail.chapman.edu
Name: Austin Ayers
Description: Implements Euler's method
"""

import numpy as np

def euler(f, fa, x):
    """
    Implements the Euler's method
    """
    y = []
    dx = x[1] - x[0]
    y.append(fa)
    for elem_x, i in enumerate(x):
        if(i == 0):
            continue
        y.append(elem_x + dx * f(elem_x))
    return y