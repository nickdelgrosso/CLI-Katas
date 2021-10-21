"""
Plots a histogram of random data onscreen using matplotlib.

Goal:  Using the argparse package, change this script so that its parameters can be specified from the terminal.

Interface:  `python plot_hist.py -n 100 --mean 5 --sd 20 --bins 4`
"""
import numpy as np
import matplotlib.pyplot as plt
from argparse import ArgumentParser

parser = ArgumentParser(description="Plots a histogram")
parser.add_argument('n', type=int)
parser.add_argument('mean', type=float)
parser.add_argument('sd', type=float)
parser.add_argument('n_bins', type=int)
args = parser.parse_args()

data = np.random.randn(args.n) * args.sd + args.mean
plt.hist(data, bins=args.n_bins)
plt.show()
