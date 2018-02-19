"""
Author:

    Oliver Sheridan-Methven.

Description:

    A miscellaneous file where I will write code examples live.
"""


def my_max(a):
    """ Return's the maximum item in a list. """
    my_running_max = None
    for i in a:
        if my_running_max < i:
            my_running_max = i
    return my_running_max

a = [1, 2, 3, 6, 5, 3, 4, 4, 4, 7, 8, 9, 2, 3]  # my input list
b = my_max(a)
print a
print b


def compute_pi(n):
    """
    Computes an approximation to pi.
    :param n: Int, level of approximation.
    :return: Float.
    """
    assert n >= 1, ''
    return -4.0 * sum([((-1.0)**i) / (2*i - 1) for i in range(1, n+1)])

import numpy as np

e_level = np.abs([np.pi - compute_pi(n) for n in range(1, 1000)])
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pylab as plt
plt.clf()
plt.plot(e_level)
plt.yscale('log')
plt.xscale('log')
for n in range(1, 100):
    print compute_pi(n)
