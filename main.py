"""
fogos-2-aprs
Version: 3.0
Date: 2024-07-29
Description: Main entry point for the fogos-2-aprs service.
"""

import time
from aprs_client import APRSClient
from data_processing import fetch_fire_data
from data_filter import filter_fire_data
from symbol_definitions import get_symbol

CHECK_INTERVAL = 120  # Check interval in seconds

def process_and_send_data(client, data):
    for incident in data:
        properties = incident["properties"]
        geometry = incident["geometry"]
        callsign = properties["OBJECTID"]
        lat = geometry["coordinates"][1]
        lon = geometry["coordinates"][0]
        status = properties["EstadoOcorrencia"]
        comment = properties.get("Operacionais") #A DD MORE IF NEEDED
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
            filtered_data = filter_fire_data(data)
            process_and_send_data(client, filtered_data)
        except Exception as e:
            print(f"Error: {e}")
        
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()
