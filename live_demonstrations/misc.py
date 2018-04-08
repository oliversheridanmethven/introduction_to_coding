"""
Author:

    Oliver Sheridan-Methven.

Description:

    A miscellaneous file where I will write code examples live.
"""

import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pylab as plt
import numpy as np
import pandas as pd

df = pd.read_csv('lesson_3/something.csv')
df['date'] = pd.to_datetime(df['date'])
plt.clf()
plt.plot(df['date'], df['something'], 'ko:', ms=3)