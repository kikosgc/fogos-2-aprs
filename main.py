"""
fogos-2-aprs
Version: 2.0
Date: 2024-07-27
Description: Main entry point for the fogos-2-aprs service.
"""

import time
from data_fetch import fetch_data
from data_filter import filter_mato_data
from aprs_client import APRSClient, get_symbol

DATA_URL = 'URL_TO_YOUR_JSON_DATA_SOURCE'
CHECK_INTERVAL = 60  # Check interval in seconds

def fetch_fire_data():
    data = fetch_data(DATA_URL)
    filtered_data = filter_mato_data(data)
    return filtered_data['features']

def process_and_send_data(client, data):
    for incident in data:
        properties = incident["properties"]
        geometry = incident["geometry"]
        callsign = properties["OBJECTID"]
        lat = geometry["coordinates"][1]
        lon = geometry["coordinates"][0]
        status = properties["EstadoOcorrencia"]
        comment = properties.get("Operacionais", "")
        symbol = get_symbol(status)
        
        client.send_packet(callsign, lat, lon, symbol, comment, status)

def main():
    client = APRSClient()
    if not client.connect():
        print("Failed to connect to any APRS server.")
        return

    while True:
        try:
            data = fetch_fire_data()
            process_and_send_data(client, data)
        except Exception as e:
            print(f"Error: {e}")
        
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()
