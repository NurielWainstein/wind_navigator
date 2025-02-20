# plotter.py
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import binary_dilation


def plot_highlighted_matrix(exploration_matrix, idx):
    dilated_matrix = binary_dilation(exploration_matrix, structure=np.ones((5, 5)))
    highlighted_matrix = np.maximum(exploration_matrix, dilated_matrix)

    cmap = plt.cm.viridis
    plt.imshow(highlighted_matrix, cmap=cmap, interpolation='none')
    plt.colorbar()
    plt.title("Highlighted 1s and Surrounding Areas")

    plt.savefig(f"images/frame_{idx}.png")
    plt.close()  # Close the plot to free memory
