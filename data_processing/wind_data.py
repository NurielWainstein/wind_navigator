# wind_data.py
import xarray as xr

def load_wind_data(file_path):
    ds = xr.load_dataset(file_path)
    u_data = ds["u"]
    v_data = ds["v"]
    return u_data, v_data
