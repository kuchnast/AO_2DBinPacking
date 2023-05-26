import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from data_structures.bin_2d import *

PACKAGE_FACE = 'c'
PACKAGE_EDGE = 'k'
BIN_EDGE = 'k'


def add_bin2d_to_plot(ax: plt.Axes, bin: Bin2D):
    ax.add_patch(Rectangle((0, 0), bin.width, bin.height, edgecolor=BIN_EDGE))
    ax.set_xlim(0, bin.width)
    ax.set_ylim(0, bin.height)

    for package in bin.packages:
        ax.add_patch(Rectangle(package.location(), package.width, package.height, edgecolor=PACKAGE_EDGE,
                               facecolor=PACKAGE_FACE))


def plot_bins2d(bins: List[Bin2D], block=False):
    bin_num = len(bins)
    fig, ax = plt.subplots(1, bin_num)
    for i in range(bin_num):
        add_bin2d_to_plot(ax[i], bins[i])

    plt.show(block=block)