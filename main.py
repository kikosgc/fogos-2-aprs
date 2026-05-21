"""
fogos-2-aprs
Version: 2.2
Date: 2026-05-21
Description: Main entry point for the fogos-2-aprs service.
"""

import time
import logging
import requests
from aprs_client import APRSClient
from data_processing import fetch_fire_data
from data_filter import filter_fire_data
from symbol_definitions import get_symbol

CHECK_INTERVAL = 600  # Interval between checks, in seconds

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')


def process_and_send_data(client, data):
    for incident in data:
        properties = incident["properties"]
        geometry = incident["geometry"]
        object_id = str(properties["ID_oc"])
        lat = geometry["coordinates"][1]
        lon = geometry["coordinates"][0]
        estado = properties["EstadoOcorrencia"]
        operacionais = properties["Operacionais"]
        mterrestres = properties["NumeroMeiosTerrestresEnvolvidos"]
        maero = properties["NumeroMeiosAereosEnvolvidos"]

        try:
            client.send_packet(object_id, lat, lon, estado, operacionais, mterrestres, maero)
        except Exception as e:
            logging.error(f"Failed to send packet for {object_id}: {e}")


def main():
    client = APRSClient()

    # Establish the initial connection before entering the main loop.
    if not client.connect():
        logging.error("Failed to connect to any APRS server on startup. Exiting.")
        return

    while True:
        try:
            # ensure_connected() will reconnect silently if the link dropped.
            if not client.ensure_connected():
                logging.error("Failed to reconnect to any APRS server. Retrying next cycle.")
                time.sleep(CHECK_INTERVAL)
                continue

            data = fetch_fire_data()
            filtered_data = filter_fire_data(data)
            process_and_send_data(client, filtered_data)

            time.sleep(30)   # Wait before sending position report
            client.send_positionreport()

            time.sleep(30)   # Wait before sending status
            client.send_statusreport()

        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching fire data: {e}")
        except Exception as e:
            logging.error(f"Error: {e}")

        time.sleep(CHECK_INTERVAL)


if __name__ == "__main__":
    main()
