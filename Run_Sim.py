#   Created by Georgiy Maruzhenko on 2019-06-04.
#   Copyright © 2019 Georgiy Maruzhenko. All rights reserved.

import numpy as np
from numpy import sqrt, sin, cos, pi, e
import matplotlib.pyplot as plt
from scipy.integrate import quad
import math as math

# Number of terms for fourier expansion
N = 10
# Boundary conditions
U1 = 1.
U2 = 3.
# Variables
L = 3.
K = 0.5
# Initial Condition
FN = 0

T_INITIAL = 0
x_axis = np.linspace(0, L)
t_array = np.linspace(T_INITIAL, 10)

v_terms = np.full(N, map(lambda n: v(), range(0,N-1,1)))

# Steady state solution
def w(x):
    result = K * x**2 / (6 * L) + ((U2-U1)/L - K*L / 6) * x +U1
    return result


# Creates fourier expansion for the transient solution given index n
def v(x, t, n):
    return get_bn(n) * sin(n * pi * x / L) * e**((n * pi / L)**2 * t)


# solves intergation to get constant for a given n
def get_bn(n):
    integral = quad(bn_integrand, 0, L, args=(n))
    return -2. / L * integral[0]


# sets up integral for quad library
def bn_integrand(x, n):
    return w(x) * sin(n * pi * x / L)


#I =  quad(bn_integrand, 0, L, args=(1))

# print(I)
print(get_bn(5))
plt.plot(x_axis, w(x_axis))
plt.plot(x_axis, v(x_axis,0,1), 'red')
plt.show()