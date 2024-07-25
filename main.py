"""
fogos-2-aprs
Version: 1.0
Date: 2024-07-25
Description: Main entry point for the fogos-2-aprs service.
"""

import time
from data_fetcher import fetch_fire_data
from aprs_client import APRSClient
from symbol_definitions import get_symbol
from config import CHECK_INTERVAL

def process_and_send_data(client, data):
    for incident in data:
        callsign = incident["id"]
        lat = incident["latitude"]
        lon = incident["longitude"]
        status = incident["status"]
        comment = incident.get("meios", "")
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
