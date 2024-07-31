import time
import logging
import requests
from aprs_client import APRSClient
from data_processing import fetch_fire_data
from data_filter import filter_fire_data
from symbol_definitions import get_symbol

CHECK_INTERVAL = 60  # Interval between checks, in seconds

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

def process_and_send_data(client, data):
    for incident in data:
        properties = incident["properties"]
        geometry = incident["geometry"]
        callsign = properties["OBJECTID"]
        lat = geometry["coordinates"][1]
        lon = geometry["coordinates"][0]
        status = properties["EstadoOcorrencia"]
        comment = properties.get("Operacionais", "")  # ADD MORE IF NEEDED
        symbol = get_symbol(status)
        
        try:
            client.send_packet(callsign, lat, lon, symbol, comment, status)
        except Exception as e:
            logging.error(f"Failed to send packet for {callsign}: {e}")

def main():
    client = APRSClient()
    if not client.connect():
        logging.error("Failed to connect to any APRS server.")
        return

    while True:
        try:
            data = fetch_fire_data()
            filtered_data = filter_fire_data(data)
            process_and_send_data(client, filtered_data)
        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching fire data: {e}")
        except Exception as e:
            logging.error(f"Error: {e}")
        
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()
