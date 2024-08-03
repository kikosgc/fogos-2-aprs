"""
fogos-2-aprs
Version: 2.1
Date: 2024-07-31
Description: Manages APRS connection and packet creation.
"""

import logging
import aprslib
from config import APRS_CALLSIGN, APRS_PASSWORD, APRS_SERVERS
from symbol_definitions import get_symbol
from datetime import datetime

class APRSClient:
    def __init__(self):
        pass
        
    def connect(self):
        for server in APRS_SERVERS:
            try:
                self.client = aprslib.IS(APRS_CALLSIGN, passwd=APRS_PASSWORD)
                self.connected = False
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

        # Get the symbol table and symbol from the status
        symbol_table, symbol = get_symbol(estado)
    

        # Construct the APRS Object packet using the raw format
        packet = f"{APRS_CALLSIGN}>APFOGO,TCPIP*:;{object_name}*{timestamp}{lat_str}{symbol_table}{lon_str}{symbol}Estado - {estado}, {operacionais} Operacionais, {mterrestres} Meios Terrestres e {maero} Meios Aéreos"
        
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
        
    def send_positionreport(self):
        if not self.connected:
            logging.error("Not connected to APRS server.")
            return

        positionreport = f"{APRS_CALLSIGN}>APFOGO,TCPIP*:=3843.23N/00914.18WoANEPC - Autoridade Nacional de Emergência e Proteção Civil"
        
        logging.info(f"Sending Position Report: {positionreport}")
        try:
            self.client.sendall(positionreport)
            logging.info(f"Position Report sent: {positionreport}")
        except Exception as e:
            logging.error(f"Failed to send Position Report: {e}")

