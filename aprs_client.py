"""
fogos-2-aprs
Version: 2.1
Date: 2024-07-31
Description: Manages APRS connection and packet creation.
"""

import logging
import aprslib
from config import APRS_CALLSIGN, APRS_PASSWORD, APRS_SERVERS
from datetime import datetime

class APRSClient:
    def __init__(self):
        self.client = aprslib.IS(APRS_CALLSIGN, passwd=APRS_PASSWORD)
        self.connected = False

    def connect(self):
        for server in APRS_SERVERS:
            try:
                self.client.connect(server['host'], server['port'])
                self.connected = True
                logging.info(f"Connected to {server}")
                return True
            except Exception as e:
                logging.error(f"Failed to connect to {server}: {e}")
        return False

    def send_packet(self, object_id, lat, lon, estado, operacionais, mterrestres, maero):
        if not self.connected:
            logging.error("Not connected to APRS server.")
            return

        # Ensure the object ID is exactly 9 characters
        object_name = f"{object_id:<9}"[:9]

        # Format the latitude and longitude in degrees and decimal minutes
        lat_str = self.format_coordinates(lat, True)
        lon_str = self.format_coordinates(lon, False)

        # Generate a timestamp in the format DDHHMMz
        timestamp = datetime.utcnow().strftime("%d%H%Mz")

        # Construct the APRS Object packet using the raw format
        packet = f"{APRS_CALLSIGN}>APFOGO,TCPIP*:;{object_name}*{timestamp}{lat_str}/{lon_str}:Estado - {estado}, {operacionais} Operacionais, {mterrestres} Meios Terrestre e {maero} Meios Aéreos"
        
        # Output a preview of the APRS packet
        print(f"APRS Packet Preview: {packet}")

        logging.info(f"Sending packet: {packet}")
        try:
            # Use the correct method to send the packet
            self.client.sendall(packet)
            logging.info(f"Packet sent: {packet}")
        except Exception as e:
            logging.error(f"Failed to send packet: {e}")

    def format_coordinates(self, coord, is_latitude):
        """
        Converts a coordinate to APRS format in degrees and decimal minutes.
        coord: The coordinate to format.
        is_latitude: Boolean indicating if the coordinate is latitude.
        """
        degrees = int(abs(coord))
        minutes = (abs(coord) - degrees) * 60
        if is_latitude:
            suffix = 'N' if coord >= 0 else 'S'
            return f"{degrees:02d}{minutes:05.2f}{suffix}"
        else:
            suffix = 'E' if coord >= 0 else 'W'
            return f"{degrees:03d}{minutes:05.2f}{suffix}"
