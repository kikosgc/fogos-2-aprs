"""
fogos-2-aprs
Version: 2.0
Date: 2024-07-29
Description: Manages APRS connection and packet creation.
"""

import logging
import aprslib
from config import APRS_CALLSIGN, APRS_PASSWORD, APRS_SERVERS

class APRSClient:
    def __init__(self):
        self.client = aprslib.IS(APRS_CALLSIGN, passwd=APRS_PASSWORD)
        self.connected = False

    def connect(self):
        for server in APRS_SERVERS:
            try:
                self.client.connect(server)
                self.connected = True
                logging.info(f"Connected to {server}")
                return True
            except Exception as e:
                logging.error(f"Failed to connect to {server}: {e}")
        return False

    def send_packet(self, callsign, lat, lon, symbol, comment, status_comment):
        if not self.connected:
            logging.error("Not connected to APRS server.")
            return

        # Construct the APRS packet using aprslib's expected format
        info = f"{lat:.2f}/{lon:.2f}{symbol} {comment} {status_comment}"
        packet = f"{APRS_CALLSIGN}>{callsign}: {info}"
        
        # Output a preview of the APRS packet
        print(f"APRS Packet Preview: {packet}")

        logging.info(f"Sending packet: {packet}")
        try:
            # Use the correct method to send the packet
            self.client.sendall(packet)
            logging.info(f"Packet sent: {packet}")
        except Exception as e:
            logging.error(f"Failed to send packet: {e}")
