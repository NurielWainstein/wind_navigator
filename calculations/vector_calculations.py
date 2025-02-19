# vector_calculations.py
import math

def calculate_resultant_vector_length_and_direction(
    first_vector_direction, first_vector_length, second_vector_length, target_direction
):
    # Convert angles to radians
    first_vector_direction_rad = math.radians(first_vector_direction)
    target_direction_rad = math.radians(target_direction)

    # Calculate the components (x, y) of the first vector
    first_vector_x = first_vector_length * math.cos(first_vector_direction_rad)
    first_vector_y = first_vector_length * math.sin(first_vector_direction_rad)

    # Calculate the components (x, y) of the second vector based on the target direction
    second_vector_x = second_vector_length * math.cos(target_direction_rad)
    second_vector_y = second_vector_length * math.sin(target_direction_rad)

    # Calculate the target position after combining both vectors
    total_x = first_vector_x + second_vector_x
    total_y = first_vector_y + second_vector_y

    # Calculate the resulting vector length and direction
    resultant_length = math.sqrt(total_x ** 2 + total_y ** 2)
    resultant_direction_rad = math.atan2(total_y, total_x)
    resultant_direction = math.degrees(resultant_direction_rad)

    return resultant_length, resultant_direction
