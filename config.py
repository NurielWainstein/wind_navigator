# config.py

HAP_SPEED_DAY = 10

LAT_LON_RES = 31000 # resolution of dataset unit in meters - read "Spatial grid" in ERA5 documentation
UNIT_DISTANCE = 150 # desired resolution

LAT_LON_MULTIPLIER = int(LAT_LON_RES/UNIT_DISTANCE)
