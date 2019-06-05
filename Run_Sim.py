#   Created by Georgiy Maruzhenko on 2019-06-04.
#   Copyright © 2019 Georgiy Maruzhenko. All rights reserved.

import numpy as np
from numpy import sqrt, sin, cos, pi, e
import matplotlib.pyplot as plt
from scipy.integrate import quad
import math as math

# Number of terms for fourier expansion
N = 20
# Boundary conditions
U1 = 1.
U2 = 3.
# Variables
L = 3.
K = 0.5
# Initial Condition
FN = 0
# x range to work in
START = 0
END = L
# Times to plot between
T_INITIAL = 0.1
T_FINAL = 2
T_STEP = 0.1

# prep arrays
x_axis = np.linspace(START, END)
t_array = np.arange(T_INITIAL, T_FINAL, T_STEP)


# Steady state solution
def w(x):
    result = K * x**2 / (6 * L) + ((U2-U1)/L - K*L / 6) * x +U1
    return result


# Creates fourier expansion for the transient solution given a time and x domain
def v(t, x_values):
    # find value for the positional component
    x_step = list(map(get_x_value, x_values))
    # multiply positional component by the decay function
    decay_component = get_t_value(t)
    transient_solution = list(map(lambda x: x * decay_component, x_step))
    return transient_solution


# Get position component with number of terms N
def get_x_value(x):
    n_terms = np.arange(0, N)
    terms = np.ones(len(n_terms))
    count = 0
    while(count < N):
        terms[count] = get_bn(n_terms[count]) * sin(n_terms[count] * pi * x / L)
        count += 1
    return sum(terms)


# Get decay component with number of terms N
def get_t_value(t):
    n_terms = np.arange(0, N)
    terms = np.ones(len(n_terms))
    count = 0
    while (count < N):
        terms[count] = e**(-1 * (n_terms[count] * pi / L)**2 * t)
        count += 1
    return sum(terms)


# solves integration to get constant for a given n
def get_bn(n):
    integral = quad(bn_integrand, 0, L, args=(n))
    return -2. / L * integral[0]


# sets up integral for quad library
def bn_integrand(x, n):
    return w(x) * sin(n * pi * x / L)


# plot one time for the domain
def plot_one_timestep(t):
    plt.plot(x_axis, v(t, x_axis) + w(x_axis))


# Show and label graph
def show_plots():
    plt.title('Heat Equation Solutions')
    plt.xlabel('x')
    plt.ylabel('u(x,t)')
    # labeled just a few timestamps
    plt.legend(
        ['Steady State Solution w(x)',
         't = ' + str(t_array[0]),
         't = ' + str(t_array[1]),
         't = ' + str("%.1f" % t_array[2])])
    plt.show()

# Run plotting functions
plt.plot(x_axis, w(x_axis), 'r')
[plot_one_timestep(t) for t in t_array]

show_plots()

