"""
fogos-2-aprs
Version: 2.0
Date: 2026-05-21
Description: Filters the incoming data from source URL.
             The filter type is controlled by NATUREZA_FILTER in config.py.
             Set NATUREZA_FILTER to None (or unset the env var) to forward
             all incident types.
"""

from config import NATUREZA_FILTER


def filter_fire_data(data):
    features = data['features']
    if NATUREZA_FILTER is None or NATUREZA_FILTER == "":
        return features
    return [
        feature for feature in features
        if feature['properties']['Natureza'] == NATUREZA_FILTER
    ]
