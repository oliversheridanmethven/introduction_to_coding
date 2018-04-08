"""
Author:

    oliver
"""
import matplotlib as mpl
# mpl.use("TkAgg")
import matplotlib.pylab as plt
import pandas as pd
import numpy as np
import scipy as sp
import matplotlib.image as img
import time

def colour_png_to_greyscale(file_name = "lesson_3/usv/example_image.png"):
    g = img.imread(file_name)
    l = np.concatenate(g)
    l = np.delete(l, 3, 1)
    l = np.array([0.2989, 0.5870, 0.1140]) * l
    l = l.sum(axis=1)
    l = l.reshape(g.shape[:2])
    return l

l = colour_png_to_greyscale()
plt.clf()
u, s, v = np.linalg.svd(l)
#
# for N in [1<<i for i in range(9)]:
#     # N = 2
#     u, s, v = np.linalg.svd(l)
#     S = s[:N]
#     U = u[:, :N]
#     V = v[:N, :]
#     [np.savetxt('usv/{}_{}.npy'.format(k, N), j, fmt='%1.4e') for k, j in zip(list('usv'), [U,S,V])]
#     S = np.mat(np.diag(S))
#     U = np.mat(U)
#     V = np.mat(V)
#     g2 = U * S * V
#     g2 = np.array(g2)

def plot_svd_image(N=None):
    assert isinstance(N, int) or N is None, 'Please request an integer'
    assert N in [1<<i for i in range(9)] or N is None, 'Please request a decomposition value which exists in the file system'
    u, s, v = [np.loadtxt('lesson_3/usv/{}{}.npy'.format(i, '' if N is None else '_{}'.format(N))) for i in list('usv')]
    S = np.mat(np.diag(s))
    [i.shape for i in [u,s,v]]
    U,V = [np.mat(i) for i in (u, v)]
    g = U*S*V
    # return g
    plt.clf()
    plt.imshow(g, cmap=plt.get_cmap('gray'))
    plt.gca().get_xaxis().set_visible(False)
    plt.gca().get_yaxis().set_visible(False)


# plot_svd_image()
#
# plot_svd_image(2)
# plot_svd_image(4)
# plot_svd_image(8)
# plot_svd_image(16)
# plot_svd_image(32)
# plot_svd_image(64)
# plot_svd_image(128)
# plot_svd_image(256)
