#   Created by Georgiy Maruzhenko on 2019-06-04.
#   Copyright © 2019 Georgiy Maruzhenko. All rights reserved.

import numpy as np
import matplotlib.pyplot as plt


U1 = 1.
U2 = 3.
L = 3.
K = 0.5
FN = 0
T_INITIAL = 0
x_axis = np.linspace(0, L)
t_array = np.linspace(T_INITIAL, 10)

# Steady state solution
def w(x):
    result = K * x**2 / (6 * L) + ((U2-U1)/L - K*L / 6) * x +U1
    return result


plt.plot(x_axis, w(x_axis))
plt.show()