"""
fogos-2-aprs
Version: 1.0
Date: 2024-07-27
Description: Filters the incoming data from source URL.
"""

def filter_mato_data(data):
    filtered_features = [feature for feature in data['features'] if feature['properties']['Natureza'] == 'Mato']
    return {
        "type": "FeatureCollection",
        "features": filtered_features
    }
