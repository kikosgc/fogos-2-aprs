"""
fogos-2-aprs
Version: 2.0
Date: 2024-07-29
Description: Fecht data from source URL.
"""

import requests
import time
import logging

API_URL = "API URL GOES HERE"

def fetch_fire_data():
    max_retries = 5
    backoff_factor = 1  # Exponential backoff factor

    for attempt in range(max_retries):
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            response = requests.get(API_URL, headers=headers, timeout=10)
            response.raise_for_status()  # Raise an HTTPError on bad status
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching fire data: {e}")
            if attempt < max_retries - 1:
                sleep_time = backoff_factor * (2 ** attempt)
                logging.info(f"Retrying in {sleep_time} seconds...")
                time.sleep(sleep_time)
            else:
                logging.error("Max retries reached. Exiting.")
                raise
