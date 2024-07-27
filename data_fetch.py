"""
fogos-2-aprs
Version: 1.0
Date: 2024-07-27
Description: Fecht data from source URL.
"""

import requests

def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()
