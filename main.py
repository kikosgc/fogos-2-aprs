import time
import logging
import requests
from aprs_client import APRSClient
from data_processing import fetch_fire_data
from data_filter import filter_fire_data
from symbol_definitions import get_symbol

CHECK_INTERVAL = 300  # Interval between checks, in seconds

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

def process_and_send_data(client, data):
    for incident in data:
        properties = incident["properties"]
        geometry = incident["geometry"]
        object_id = str(properties["ID_oc"])
        lat = geometry["coordinates"][1]
        lon = geometry["coordinates"][0]
        estado = properties["EstadoOcorrencia"]  # Customize as needed
        operacionais = properties["Operacionais"]
        mterrestres = properties["NumeroMeiosTerrestresEnvolvidos"]
        maero = properties["NumeroMeiosAereosEnvolvidos"]

        try:
            client.send_packet(object_id, lat, lon, estado, operacionais, mterrestres, maero)
        except Exception as e:
            logging.error(f"Failed to send packet for {object_id}: {e}")

def main():
    client = APRSClient()

    while True:
        try:
            if not client.connect():
                logging.error("Failed to connect to any APRS server.")
                return
            data = fetch_fire_data()
            filtered_data = filter_fire_data(data)
            process_and_send_data(client, filtered_data)
            time.sleep(60) # WAITS 60 seconds BEFORE SENDING POSITION REPORT
            client.send_positionreport()
            time.sleep(60) # WAITS 60 seconds BEFORE SENDING STATUS
            client.send_statusreport()
        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching fire data: {e}")
        except Exception as e:
            logging.error(f"Error: {e}")
        
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()
