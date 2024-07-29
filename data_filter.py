"""
fogos-2-aprs
Version: 1.2
Date: 2024-07-29
Description: Filters the incoming data from source URL.
"""

def filter_fire_data(data):
    filtered_features = [feature for feature in data['features'] if feature['properties']['Natureza'] == 'Mato']
    return filtered_features
