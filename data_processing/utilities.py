# utilities.py
import numpy as np

from config import LAT_LON_MULTIPLIER


def expand_ndarrays(original_array, reshape_rate=LAT_LON_MULTIPLIER):
    expanded_array = np.repeat(np.repeat(original_array, reshape_rate, axis=0), reshape_rate, axis=1)
    return expanded_array
