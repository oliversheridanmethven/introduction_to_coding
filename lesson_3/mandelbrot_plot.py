"""
Author:

    Oliver Sheridan-Methven, November 2017.

Description:

    Plotting the Mandelbrot set.
"""

# Makes nice plots.
import matplotlib as mpl
mpl.use("TkAgg")
rc_fonts = {
    "text.usetex": True,
    "font.size": 30,
    'mathtext.default': 'regular',
    'axes.titlesize': 33,
    "axes.labelsize": 33,
    "legend.fontsize": 30,
    "xtick.labelsize": 30,
    "ytick.labelsize": 30,
    'figure.titlesize': 33,
    'figure.figsize': (15, 9.3),
    'text.latex.preamble': [r'\usepackage{amsmath,amssymb,bm,physics,lmodern}'],
    "font.family": "serif",
    "font.serif": "computer modern roman",
}
mpl.rcParams.update(rc_fonts)
import matplotlib.pylab as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from functools import partial


def f(c, N=100):
    """
    Colour scheme for the Mandelbrot set.
    :param c: Complex Number
    :return: Float, fraction of iterations until c left the mandlebrot set.
                Values close to 1 -> Black.
                Values close to 0 -> White.
    """
    def p(z, c):
        """ The Mandelbrot iterative function """
        return z ** 2 + c

    p = partial(p, c=c)

    z = 0 + 0j  # Starting value
    l = np.array([z] * (N + 1))  # Initialise array.
    for i in xrange(1, N):
        l[i] = p(l[i - 1])
    l[-1] = 2 + 1  # Ensure the final value is outside the set so the generator finds a value.
    return (1.0 * (k for k, v in enumerate(l) if np.abs(v) > 2.0).next()) / N

#  Setting up the grid.
xl, xu = -2.0, 0.6
yl, yu = -1.3, 1.3
n = 500  # Grid resolution
x = np.outer(np.linspace(xl, xu, n), np.ones(n))
y = np.outer(np.linspace(yl, yu, n), np.ones(n)).T
xv = np.array(zip(np.concatenate(x), np.concatenate(y)))
N = 100  # Mandelbrot colour resolution.
z = np.reshape(np.apply_along_axis(lambda z: f((z[0] + z[1] * 1j), N=N), 1, xv), x.shape).T

plt.clf()
plt.imshow(z)
plt.xticks([])
plt.yticks([])
plt.title('The Mandelbrot set')
# plt.savefig('lesson_3/mandelbrot_set.pdf', format='pdf', bbox_inches='tight')

