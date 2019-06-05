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

T_INITIAL = 0
T_FINAL = 10
x_axis = np.linspace(START, END)
t_array = np.arange(T_INITIAL, T_FINAL)


# Steady state solution
def w(x):
    result = K * x**2 / (6 * L) + ((U2-U1)/L - K*L / 6) * x +U1
    return result


# Creates fourier expansion for the transient solution given index n
def v(t, x_values):
    # for one x and t
    x_step = list(map(get_x_value, x_values))
    total = list(map(lambda x: x * get_t_values(t), x_step))

    print(total)
    return total

def get_x_value(x):
    n_terms = np.arange(0, N)
    terms = np.ones(len(n_terms))
    count = 0
    while(count < N):
        terms[count] = get_bn(n_terms[count]) * sin(n_terms[count] * pi * x / L)
        count += 1
    return sum(terms)


def get_t_values(t):
    n_terms = np.arange(0, N)
    terms = np.ones(len(n_terms))
    count = 0
    while (count < N):
        terms[count] = e**(-1 * (n_terms[count] * pi / L)**2 * t)
        count += 1
    return sum(terms)



# solves intergation to get constant for a given n
def get_bn(n):
    integral = quad(bn_integrand, 0, L, args=(n))
    return -2. / L * integral[0]


# sets up integral for quad library
def bn_integrand(x, n):
    return w(x) * sin(n * pi * x / L)


def plot_one_timestep(t):
    plt.plot(x_axis, v(t, x_axis) + w(x_axis))


#I =  quad(bn_integrand, 0, L, args=(1))

# print(I)
# print(get_bn(5))
[plot_one_timestep(t) for t in t_array]

# plt.plot(x_axis, v(1,x_axis))
plt.show()