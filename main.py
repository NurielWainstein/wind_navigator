# main.py
import numpy as np
from config import UNIT_DISTANCE, HAP_SPEED, LAT_LON_MULTIPLIER
from data_processing.wind_data import load_wind_data
from data_processing.utilities import expand_ndarrays
from calculations.vector_calculations import calculate_vector2_direction_and_length
from calculations.movement import calculate_angle, move_in_direction
from exploration.exploration_matrix import zigzag_iterator
from visualization.plotter import plot_highlighted_matrix

# Load wind data
u_data, v_data = load_wind_data("wd.nc")

# Initialize exploration matrix
latitude, longitude = u_data.shape[1], u_data.shape[2]
roi_shape = (latitude * LAT_LON_MULTIPLIER, longitude * LAT_LON_MULTIPLIER)
exploration_matrix = np.zeros((roi_shape[0], roi_shape[1]))
zigzag_iterator = zigzag_iterator(exploration_matrix)
current_position = next(zigzag_iterator)
target_point = next(zigzag_iterator)

# Iterate through the data and calculate wind speed and direction
for u_timestamp, v_timestamp in zip(u_data, v_data):
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

    remaining_minutes = 60
    while remaining_minutes > 0 or exploration_matrix.min == 1:
        optimal_pressure_level = None
        closest_angle_deg = None
        current_path = calculate_angle(current_position, target_point)

        for pl in pressure_levels_data:
            wind_speed, wind_direction = pl
            current_wind_speed = wind_speed[current_position]
            current_wind_direction = wind_direction[current_position]

            current_speed, current_direction = calculate_vector2_direction_and_length(
                current_wind_direction, current_wind_speed, HAP_SPEED, current_path)

            if closest_angle_deg is None or abs(current_direction - current_path) < abs(closest_angle_deg - current_path):
                closest_angle_deg = current_direction
                optimal_pressure_level = pl

        new_point = move_in_direction(current_position, closest_angle_deg)
        x, y = new_point

        if x >= 0 and y >= 0 and x < exploration_matrix.shape[0] and y < exploration_matrix.shape[1]:
            current_position = new_point
            exploration_matrix[current_position] = 1

        if current_position == target_point:
            target_point = next(zigzag_iterator)

        travel_time = UNIT_DISTANCE / current_speed
        remaining_minutes -= travel_time

# Visualize the results
plot_highlighted_matrix(exploration_matrix)
