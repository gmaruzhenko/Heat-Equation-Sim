#   Created by Georgiy Maruzhenko on 2019-06-07.
#   Copyright © 2019 Georgiy Maruzhenko. All rights reserved.

import numpy as np
from numpy import sqrt, sin, cos, pi, e

# Energy function we wish to reach
TARGET = 16. / 15
# How much error can we tolerate when converging to target
ERROR = 0.001

# function average over period
A0 = -2./3


def terms_to_converge(target, error):
    n = 1
    result_so_far = A0 **2 / 2
    while n<80:#result_so_far +error < target or result_so_far-error > target:
        term_b = generate_bn(n)
        term_a = generate_an(n)
        result_so_far += term_b ** 2 + term_a **2
        print("term a= ", term_a, "\nterm b= ", term_b, "\nrsf = ", result_so_far)
        n += 1
    return n


def generate_bn(n):
    return -2. * (2. * cos(n * pi) + n * sin(n * pi) * pi - 2.) / (n ** 3 * pi ** 3)


def generate_an(n):
    return -2 * (n * cos(n * pi) * pi - 2 * sin(n * pi) + n * pi) / (n ** 3 * n ** 3)


# print(generate_bn(1))
#print(generate_an(1))
print(terms_to_converge(TARGET, ERROR))
