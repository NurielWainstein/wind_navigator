# movement.py
import math


def calculate_angle(current_point, target_point):
    x1, y1 = current_point
    x2, y2 = target_point
    angle_rad = math.atan2(y2 - y1, x2 - x1)
    angle_deg = math.degrees(angle_rad)

    if angle_deg < 0:
        angle_deg += 360

    return angle_deg


def move_in_direction(current_point, angle_deg):
    angle_deg = angle_deg % 360
    angles = [0, 45, 90, 135, 180, 225, 270, 315]
    sector_size = 360 / 8
    index = int((angle_deg + sector_size / 2) // sector_size) % 8
    normalized_angle_deg = angles[index]

    movement_map = {
        0: (1, 0), 45: (1, 1), 90: (0, 1), 135: (-1, 1),
        180: (-1, 0), 225: (-1, -1), 270: (0, -1), 315: (1, -1)
    }

    delta_x, delta_y = movement_map[normalized_angle_deg]
    new_point = (current_point[0] + delta_x, current_point[1] + delta_y)
    return new_point
