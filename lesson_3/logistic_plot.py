"""
Author:

    Oliver Sheridan-Methven, November 2017.

Description:

    Plotting the logistic map.
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
import numpy as np
from functools import partial

N = 8000  # Number of points to plot for a given r
burn = N  # Number of points to burn.
n = 1000  # Resolution of x axis.

xl = 2.8
xu = 4.0
dx = (xu - xl) / (n - 1)

plt.clf()
for r in np.linspace(xl, xu, n):
    x0 = np.random.random()
    y = [x0] * (N + burn)
    for i in range(1, len(y)): y[i] = r * y[i - 1] * (1.0 - y[i - 1])
    y = y[burn:]
    plt.plot([r] * len(y), y, 'k.', ms=20*dx, alpha=0.5)

plt.xlim([xl, xu])
plt.yticks([])
plt.xticks([])
plt.title('The logistic map', y=1.01)
plt.savefig('lesson_3/logistic_map.png', format='png', bbox_inches='tight', dpi=300)