"""
Author:

    Oliver Sheridan-Methven, September 2017.

Description:

    A showcase of how to write more advanced function features, including:

        - Variable and keyword arguments.
        - Partial functions.
        - Vectorised functions.
"""

import numpy as np
from functools import partial
from collections import Iterable

# Variable and keyword arguments.

def sum_2_numbers(x, y):
    """Sums two numbers."""
    return x + y


s = sum_2_numbers(1.0, 3.0)


def sum_n_numbers(*args):
    """Sums many numbers"""
    s = 0
    for x in args:  # "args" will be a list.
        s += x
    return s


s = sum_n_numbers(1, 2, 3, 4, 5)
s = sum_n_numbers(*range(1000))  # Unpacking the values.


def print_my_name(name='Oliver'):
    """Prints a name."""
    print name


print_my_name()  # Use the default value.
print_my_name('David')  # Specify the first argument of the function.
print_my_name(name='Raphael')  # Provide the value of the argument by naming it. (Order no longer important).


def print_names_and_ages(**names):
    """Prints names and ages."""
    for k, v in names.iteritems():
        print('Name: {:<10}\tAge: {}\n'.format(k, v))


print_names_and_ages(Daniel=24, Federico=26, Joseph=33, **{'Oliver': 24, 'Susan': 52})


def example_with_all_arguments(x, y=1, *args, **kwargs):
    """
    An example including:
    :param x: Float, mandatory argument.
    :param y: Float, mandatory argument (default y=1).
    :param args: Floats, extra optional argument.
    :param kwargs: Dict, extra optional argument.
    :return: Something.
    """
    z = x + y + sum(args)
    for k, v in kwargs.iteritems(): print k, v
    return z


example_with_all_arguments(2, 3, 4, 5, instructor='Oliver', students='OIC')


# Suppose we wanted a function which has some default value.
# But we might want different versions using different default values.
# This is where partial functions comes in handy.

def norm(x, metric='l2'):
    """
    Computes the different l-norms.
    :param x: Iterable, vector.
    :param metric: Str or Float, normalisation metric.
    :return: Float, vector norm.
    """
    assert isinstance(x, Iterable), 'Please enter an iterable object to compute the norm over.'
    defined_norms = ('l0', 'l1', 'l2', 'inf')  # And positive floats.
    assert metric in defined_norms or metric > 0, 'The metric {} must be either {} or a positive float.'.format(metric, defined_norms)
    r = 0.0
    for i in x:
        if metric == 'l0':
            r += i != 0
        elif metric == 'l1':
            r += abs(i)
        elif metric == 'l2':
            r += i ** 2.0
        elif metric == 'inf':
            r = max(i, r)
        else:
            r += i ** metric

    if metric == 'l0':
        pass
    elif metric == 'l1':
        pass
    elif metric == 'l2':
        r = r ** 0.5
    elif metric == 'inf':
        pass
    else:
        r = pow(r, 1.0 / metric)

    return r


x = np.array([1.0, 2.0, 3.0, 4.0])

norm(x)  # Use the default value
norm(x, metric='l2')  # Explicitly set the metric.

l_1_norm = partial(norm, metric='l1')  # Redefine the default value.
l_2_norm = partial(norm, metric='l2')
l_inf_norm = partial(norm, metric='inf')

l_1_norm(x)
l_2_norm(x)
l_inf_norm(x)


# Vectorised functions are useful when we have a function which was originally designed
# to only work on one item, but we would like ito to be able to work on many items and
# return a list of results. Consider the following example of a one item function:

def is_a_triangle_number(x):
    """
    Computes whether a number is a triangle number.
    :param x: Int.
    :return: Bool.
    """
    assert isinstance(x, int) and x > 0, 'Please input an integer.'
    i = 1
    while x > 0:
        x -= i
        i += 1
    return x == 0


for i in range(1, 11): print i, is_a_triangle_number(i)

vectorised_function = np.vectorize(is_a_triangle_number)
vectorised_function(range(1, 16))


# Be careful though, this can throw issues with assertions.

@np.vectorize  # Your first encounter with a function wrapper.
def triangle_number(x):
    """
    Computes whether a number is a triangle number.
    :param x: Int.
    :return: Bool.
    """
    assert isinstance(x, int), 'Please input an integer.'
    # assert type(x) == int, 'Please input an integer.' ## This won't work with np.vectorize
    assert x > 0, 'Please input a positive number.'
    i = 1
    while x > 0:
        x -= i
        i += 1
    return x == 0


triangle_number(range(1, 16))


# If all else fails then you can always call the function with a list comprehension, but this
# is not particularly good for performance.

[triangle_number(i) for i in range(1, 16)]