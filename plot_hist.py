"""
Plots a histogram of random data onscreen using matplotlib.

Goal:  Using the argparse package, change this script so that its parameters can be specified from the terminal.

Interface:  `python plot_hist.py -n 100 --mean 5 --sd 20 --bins 4`
"""


import numpy as np
import matplotlib.pyplot as plt

n = 50
mean = 10
sd = 0.2
n_bins = 10

data = np.random.randn(n) * sd + mean
plt.hist(data, bins=n_bins)
plt.show()
