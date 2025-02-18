# vector_calculations.py
import math

def calculate_vector2_direction_and_length(vector1_direction, vector1_length, vector2_length, target_direction):
    vector1_direction_rad = math.radians(vector1_direction)
    target_direction_rad = math.radians(target_direction)

    vector1_x = vector1_length * math.cos(vector1_direction_rad)
    vector1_y = vector1_length * math.sin(vector1_direction_rad)

    target_x = (vector1_length * math.cos(vector1_direction_rad)) + (vector2_length * math.cos(target_direction_rad))
    target_y = (vector1_length * math.sin(vector1_direction_rad)) + (vector2_length * math.sin(target_direction_rad))

    vector2_x = target_x - vector1_x
    vector2_y = target_y - vector1_y

    vector2_direction_rad = math.atan2(vector2_y, vector2_x)
    vector2_direction = math.degrees(vector2_direction_rad)

    final_x = vector1_x + vector2_x
    final_y = vector1_y + vector2_y
    final_length = math.sqrt(final_x ** 2 + final_y ** 2)

    final_direction_rad = math.atan2(final_y, final_x)
    final_direction = math.degrees(final_direction_rad)

    return final_length, final_direction
