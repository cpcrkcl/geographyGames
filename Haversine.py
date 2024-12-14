import math 
import numpy as np

def get_cardinal_direction(bearing):
    directions = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
    index = int(bearing / 45) % 8
    return directions[index]

def calculate_distance_and_bearing(start_lat, start_lon, target_lat, target_lon):
    if np.isnan(start_lat) or np.isnan(start_lon) or np.isnan(target_lat) or np.isnan(target_lon):
        raise ValueError("Coordinates contain NaN values")
    
    # Calculate bearing
    lat1_rad = math.radians(start_lat)
    lat2_rad = math.radians(target_lat)
    lon_diff_rad = math.radians(target_lon - start_lon)
    
    x = math.sin(lon_diff_rad) * math.cos(lat2_rad)
    y = math.cos(lat1_rad) * math.sin(lat2_rad) - math.sin(lat1_rad) * math.cos(lat2_rad) * math.cos(lon_diff_rad)
    bearing = math.degrees(math.atan2(x, y))
    bearing = (bearing + 360) % 360  # Normalize to 0-360
    
    # Calculate distance using Haversine formula
    R = 6371  # Earth's radius in kilometers
    dlat = math.radians(target_lat - start_lat)
    dlon = math.radians(target_lon - start_lon)
    a = math.sin(dlat/2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = R * c
    
    return distance, get_cardinal_direction(bearing)



