# wind_data.py
import numpy as np
import xarray as xr

from data_processing.utilities import expand_ndarrays


def load_wind_data(file_path):
    ds = xr.load_dataset(file_path)
    u_data = ds["u"]
    v_data = ds["v"]
    return u_data, v_data

def process_wind_data(u_timestamp, v_timestamp):
    pressure_levels_data = []
    for u_pl, v_pl in zip(u_timestamp, v_timestamp):
        u_data_array = u_pl.data
        v_data_array = v_pl.data

        wind_speed = np.sqrt(u_data_array ** 2 + v_data_array ** 2)
        wind_direction = np.arctan2(v_data_array, u_data_array)
        wind_direction_deg = np.degrees(wind_direction)

        wind_speed = expand_ndarrays(wind_speed)
        wind_direction_deg = expand_ndarrays(wind_direction_deg)

        pressure_levels_data.append((wind_speed, wind_direction_deg))
    return pressure_levels_data
