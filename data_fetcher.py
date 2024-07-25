"""
fogos-2-aprs
Version: 1.0
Date: 2024-07-25
Description: Fetches data from the Fogos.pt API.
"""

import requests
from config import FOGOS_API_URL

def fetch_fire_data():
    response = requests.get(FOGOS_API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}")
