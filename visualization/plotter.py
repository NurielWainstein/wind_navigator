# plotter.py
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import binary_dilation


def plot_highlighted_matrix(exploration_matrix):
    dilated_matrix = binary_dilation(exploration_matrix, structure=np.ones((10, 10)))
    highlighted_matrix = np.maximum(exploration_matrix, dilated_matrix)

    cmap = plt.cm.viridis
    plt.imshow(highlighted_matrix, cmap=cmap, interpolation='none')
    plt.colorbar()
    plt.title("Highlighted 1s and Surrounding Areas")
    plt.show()
