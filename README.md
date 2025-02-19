# README for HAP Exploration

https://github.com/user-attachments/assets/3f642119-d71e-42dd-8ee3-9d322bf81f03

## Overview

This project simulates an exploration process of a High-Altitude Platform (HAP) navigating a specific area while being influenced by wind data. The HAP follows a zigzag exploration strategy, adjusting its movement based on the current wind conditions at different pressure levels and making decisions in real-time.

The system leverages wind data for its movement strategy, adjusting its trajectory based on wind direction and speed at various pressure levels. The exploration continues until the target area is fully explored or a specified time limit is reached.

## Features

- **Wind Data Processing**: Utilizes U and V wind components to calculate wind speed and direction.
- **Exploration Strategy**: The exploration follows a zigzag pattern using a custom iterator.
- **Movement**: HAP's movement is influenced by wind conditions, allowing it to adjust direction and speed dynamically.
- **Visualization**: Displays the exploration progress visually as a matrix, highlighting the areas covered.

## Requirements

This project requires the following Python packages:

- `numpy`: For handling arrays and mathematical operations.
- `matplotlib`: For visualization.
- Any custom modules for data processing and calculations (e.g., `load_wind_data`, `expand_ndarrays`, etc.).

Ensure that the paths to required modules (like `data_processing` and `calculations`) are correctly set up.

## Files

- **Hap Class**: The main class that encapsulates the exploration process. It loads wind data, processes it, moves the HAP, and visualizes the results.
- **Main Script**: The script that runs the exploration when executed.
  
### `Hap Class`
The `Hap` class in `hap_exploration.py` contains:
- `__init__(self, wind_data_path, roi_shape_multiplier)`: Initializes the HAP with wind data and a region of interest (ROI) shape multiplier.
- `_load_data(self)`: Loads the wind data and initializes the exploration matrix.
- `_process_wind_data(self, u_timestamp, v_timestamp)`: Processes wind data for the specified timestamps.
- `_explore(self, u_data, v_data)`: Executes the exploration logic for the given wind data.
- `run_exploration(self)`: Runs the exploration for all wind data timestamps.
- `visualize_exploration(self)`: Visualizes the exploration progress on a matrix.
- `print_exploration_result(self)`: Prints the result of the exploration in terms of the area covered.

### `Main Script`
The main script, when executed, will create an instance of the `Hap` class, run the exploration, and visualize the results.

## Installation

1. Clone the repository or download the necessary files.
2. Install the required dependencies:
    ```bash
    pip install -r requirments.txt
    ```
3. Make sure to configure the wind data path correctly in the script or class initialization.

## Usage

### Running the Exploration

1. In the `main.py` file, specify the path to the wind data file and run the script:
   ```python
   hap = Hap("path/to/your/wind_data.nc")
   hap.run_exploration()
   hap.visualize_exploration()
   hap.print_exploration_result()


### Output

After running the exploration, the following results will be available:
## Classes and Methods

### `Hap` Class

The `Hap` class represents the High-Altitude Platform (HAP) and manages its exploration process. The class is responsible for loading wind data, processing it, navigating the exploration area, and visualizing the results.

#### `__init__(self, wind_data_path, roi_shape_multiplier)`
- **Purpose**: Initializes the HAP object with wind data and sets up the exploration area.
- **Parameters**:
  - `wind_data_path` (str): Path to the wind data file in NetCDF format.
  - `roi_shape_multiplier` (float, optional): Multiplier to adjust the region of interest (ROI) size. Defaults to `LAT_LON_MULTIPLIER`.

#### `_load_data(self)`
- **Purpose**: Loads wind data and initializes the exploration matrix, setting up the exploration area based on the wind data.
- **Description**: This method loads both U and V wind components and determines the dimensions of the exploration matrix based on the latitude and longitude values.

#### `_process_wind_data(self, u_timestamp, v_timestamp)`
- **Purpose**: Processes wind data for a given timestamp.
- **Parameters**:
  - `u_timestamp` (object): U-component wind data for the current timestamp.
  - `v_timestamp` (object): V-component wind data for the current timestamp.
- **Returns**: A list of tuples containing processed wind speed and direction for each pressure level.

#### `_explore(self, u_data, v_data)`
- **Purpose**: Performs the exploration logic, determining the HAP's movement at each step.
- **Parameters**:
  - `u_data` (array): U-component wind data for the current timestamp.
  - `v_data` (array): V-component wind data for the current timestamp.
- **Description**: This method moves the HAP according to the calculated wind speed and direction, updating the exploration matrix as the HAP covers new areas. It continues until the exploration matrix is fully explored or the time limit is reached.

#### `run_exploration(self)`
- **Purpose**: Runs the entire exploration process across all wind data timestamps.
- **Description**: This method iterates over the wind data and calls `_explore` for each timestamp to simulate the movement and exploration of the area.

#### `visualize_exploration(self)`
- **Purpose**: Visualizes the exploration progress.
- **Description**: This method plots the exploration matrix, highlighting the areas that have been explored by the HAP.

#### `print_exploration_result(self)`
- **Purpose**: Prints the results of the exploration, including the percentage of the area covered.
- **Description**: This method calculates the percentage of the area that was explored and prints the result, along with the total number of explored blocks.


1. **Exploration Progress**: 
   The matrix representing the explored area will be updated as the HAP moves. Each explored block will be marked, and the matrix will visually display the percentage of the area covered.

2. **Exploration Result**: 
   The percentage of the area explored and the total number of blocks explored will be printed.

### Example Output:
```bash
The HAP explored 75.32% of the total area in 24 hours
total_explored_blocks: 1500
```


## Algorithm Overview

This algorithm is designed to explore a region of interest (ROI) using a High Altitude Platform (HAP). The primary objective is to calculate the optimal path for the HAP to explore the ROI, accounting for both the HAP's capabilities and wind conditions at different altitudes.

### Key Concepts

- **Current Position & Target Position:** The algorithm always considers the current position of the HAP and the target position. The target position is decided based on the exploration strategy, in this case I opted to explore the grid in a simply Zig-Zag pattern to ensure exploring the hole grid, the algorithm calculates the angle between these two points(current and target) to determine the linear path, or in other words, the optimal path.

- **HAP Movement:** The HAP moves at a speed of 10 m/s, which is relatively slow compared to the wind speeds at higher altitudes (2-3 times faster). Therefore, we adjust the HAP's altitude to optimize its movement based on wind speed and direction.

- **Movement Vector Optimization:** The movement vector is calculated by combining the HAP's speed with the wind's force and direction. The result is the optimal direction for movement. The algorithm ensures that the HAP explores one of the eight neighboring squares at a time.

- **Exploration Process:** Every time the HAP moves or the wind changes (once per hour), the algorithm recalculates the angle between the current and target positions and selects the best altitude. This process is repeated, eventually covering the entire ROI.

### Algorithm Details

- **Exploration Grid:** The HAP explores one square at a time (150m x 150m), Although the real exploration grid is 10x1 (1500m x 150m), for simplicity, we assume the HAP can only explore one square at a time.

- **Time to Cover ROI:** The algorithm is slow and can take around 50 days to cover 100 km² of area, which corresponds to approximately 4444 blocks on the exploration grid.

- **Constraints:** The algorithm assumes that the HAP cannot go out of bounds, and thus creates invisible walls around the area to simplify the model.

- **Wind Impact:** The HAP's low power is compensated by the winds, which often propel the HAP faster. However, this dependence on the wind means the exploration process is slower, as the HAP's movement is not entirely autonomous.

### Future improvements

- **Algorithm:** this algorithm is not optimal as it doesnt count for strong winds that badly affect the desired path, we should implement a more flexible algorithm that will provide some flexibility to the HAP movement, maybe using centroids as targets instead of specific cells

- **Consider Specific Areas:** In reality not all the area received in the data is part of the ROI, for example, in this task we need to consider Brasil's borders, we should extend the functionality to make this possible

- **Multiple HAPS:** In reality we would like to allow multiple HAPS to explore the same exploration matrix

- **ROI distributions:** use area division algorithms to consider how many HAPS to use in some area

- **Data Analysis:** we should create data analysis functions to further understand the wind patterns, forces and directions in areas and months of interest

- **API:** Implement an api to allow getting real time wind data, making the model much more precise, currently we have only data once an hour

- **MOVEMENT LOGIC:** the current movement logic is not precise, we always assume that moving from one cell to another is a distance of 150m which is incorrect

- **Tests:** Implement tests
