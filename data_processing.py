"""
fogos-2-aprs
Version: 2.0
Date: 2024-07-29
Description: Fecht data from source URL.
"""

import requests

def fetch_fire_data():
    # Replace this with the actual API endpoint and parsing logic
    url = 'https://api.example.com/fire-data'
    response = requests.get(url)
    response.raise_for_status()
    return response.json()
