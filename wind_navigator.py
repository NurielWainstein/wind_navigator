import numpy as np
from config import UNIT_DISTANCE, HAP_SPEED_DAY, LAT_LON_MULTIPLIER
from data_processing.wind_data import load_wind_data, process_wind_data
from calculations.vector_calculations import calculate_resultant_vector_length_and_direction
from calculations.movement import calculate_angle, move_in_direction
from exploration.exploration_strategies import zigzag_iterator
from visualization.plotter import plot_highlighted_matrix


class Hap:
    def __init__(self, wind_data_path, roi_shape_multiplier=LAT_LON_MULTIPLIER):
        self.wind_data_path = wind_data_path
        self.roi_shape_multiplier = roi_shape_multiplier
        self.exploration_matrix = None
        self.current_position = None
        self.target_position = None
        self.time_frames = None
        self.pressure_levels = None
        self.latitude = None
        self.longitude = None
        self.wind_data = None
        self.target_iterator = None
        self._load_data()

    def _load_data(self):
        # Load wind data and initialize exploration matrix
        u_data, v_data = load_wind_data(self.wind_data_path)
        self.wind_data = (u_data, v_data)

        # Initialize exploration matrix
        self.time_frames, self.pressure_levels, self.latitude, self.longitude = u_data.shape

        roi_shape = (self.latitude * self.roi_shape_multiplier, self.longitude * self.roi_shape_multiplier)
        self.exploration_matrix = np.zeros(roi_shape)
        self.target_iterator = zigzag_iterator(self.exploration_matrix)

        self.current_position = next(self.target_iterator)
        self.exploration_matrix[self.current_position] = 1

        self.target_position = next(self.target_iterator)

    def _explore(self, u_data, v_data):
        remaining_minutes = 60
        pressure_levels_data = process_wind_data(u_data, v_data)

        # run until we get new wind data
        while remaining_minutes > 0:
            current_direction = None
            current_speed = None
            target_angle = calculate_angle(self.current_position, self.target_position)

            for pl in pressure_levels_data:
                # get current position data
                wind_speed, wind_direction = pl
                current_wind_speed = wind_speed[self.current_position]
                current_wind_direction = wind_direction[self.current_position]

                # calculate possible speed and direction of the HAP
                expected_speed, expected_direction = calculate_resultant_vector_length_and_direction(
                    current_wind_direction, current_wind_speed, HAP_SPEED_DAY, target_angle)

                # choose pest altitude
                if current_direction is None or (abs(expected_direction - target_angle) < abs(
                        current_direction - target_angle) and expected_speed > current_speed):
                    current_speed = expected_speed
                    current_direction = expected_direction

            # make the movement
            new_position = move_in_direction(self.current_position, current_direction)
            new_x_position, new_y_position = new_position

            # check that we didn't go out of bound
            if (new_x_position >= 0 and new_y_position >= 0 and new_x_position < self.exploration_matrix.shape[0]
                    and new_y_position < self.exploration_matrix.shape[1]):
                # update position data
                self.current_position = new_position
                self.exploration_matrix[self.current_position] = 1

                # exit condition - matrix fully explored
                if self.exploration_matrix.min() == 1:
                    break

                if self.current_position == self.target_position:
                    self.target_position = next(self.target_iterator)

            # roughly estimate the time it took to move
            travel_time = UNIT_DISTANCE / current_speed
            remaining_minutes -= travel_time

    def run_exploration(self):
        u_data, v_data = self.wind_data
        for u_timestamp, v_timestamp in zip(u_data, v_data):
            self._explore(u_timestamp, v_timestamp)

    def visualize_exploration(self):
        plot_highlighted_matrix(self.exploration_matrix)

    def print_exploration_result(self):
        total_explored_blocks = self.exploration_matrix.sum()
        total_blocks = self.exploration_matrix.shape[0] * self.exploration_matrix.shape[1]
        percent_of_exploration = total_explored_blocks / total_blocks

        print(f"The HAP explored {percent_of_exploration * 100:.2f}% of the total area in {self.time_frames} hours")
        print(f"total_explored_blocks: {total_explored_blocks}")


if __name__ == "__main__":
    hap = Hap("local_files/wd1.nc")
    hap.run_exploration()
    hap.visualize_exploration()
    hap.print_exploration_result()
