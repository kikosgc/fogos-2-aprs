"""
fogos-2-aprs
Version: 2.2
Date: 2026-05-21
Description: Manages APRS connection and packet creation.
             The client maintains a persistent connection and only
             reconnects when the existing connection has been lost.
"""

import logging
import aprslib
from config import (
    APRS_CALLSIGN,
    APRS_PASSWORD,
    APRS_SERVERS,
    POSITION_LAT,
    POSITION_LON,
    POSITION_COMMENT,
)
from symbol_definitions import get_symbol
from datetime import datetime


class APRSClient:
    def __init__(self):
        self.client = None
        self.connected = False

    def connect(self):
        """Attempt to connect to each configured APRS-IS server in order.
        Returns True on success, False if all servers are unreachable.
        """
        for server in APRS_SERVERS:
            try:
                self.client = aprslib.IS(APRS_CALLSIGN, passwd=APRS_PASSWORD)
                self.connected = False  # Reset before attempting
                self.client.connect(server['host'], server['port'])
                self.connected = True
                logging.info(f"Connected to {server}")
                return True
            except Exception as e:
                logging.error(f"Failed to connect to {server}: {e}")
        return False

    def ensure_connected(self):
        """Reconnect only if the client is not currently connected."""
        if not self.connected or self.client is None:
            logging.info("Not connected — attempting to connect to APRS server.")
            return self.connect()
        return True

    def send_packet(self, object_id, lat, lon, estado, operacionais, mterrestres, maero):
        if not self.ensure_connected():
            logging.error("Cannot send packet: not connected to any APRS server.")
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
        packet = (
            f"{APRS_CALLSIGN}>APFOGO,TCPIP*:"
            f";{object_name}*{timestamp}"
            f"{lat_str}{symbol_table}{lon_str}{symbol}"
            f"Estado - {estado}, {operacionais} Operacionais, "
            f"{mterrestres} Meios Terrestres e {maero} Meios Aéreos"
        )

        logging.debug(f"APRS Packet Preview: {packet}")
        logging.info(f"Sending packet: {packet}")
        try:
            self.client.sendall(packet)
            logging.info(f"Packet sent: {packet}")
        except Exception as e:
            logging.error(f"Failed to send packet: {e}")
            self.connected = False  # Mark as disconnected so next call reconnects

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
        if not self.ensure_connected():
            logging.error("Cannot send position report: not connected to any APRS server.")
            return

        positionreport = (
            f"{APRS_CALLSIGN}>APFOGO,TCPIP*:"
            f"!{POSITION_LAT}/{POSITION_LON}o"
            f"{POSITION_COMMENT}"
        )

        logging.debug(f"APRS Position Report Preview: {positionreport}")
        logging.info(f"Sending Position Report: {positionreport}")
        try:
            self.client.sendall(positionreport)
            logging.info(f"Position Report sent: {positionreport}")
        except Exception as e:
            logging.error(f"Failed to send Position Report: {e}")
            self.connected = False

    def send_statusreport(self):
        if not self.ensure_connected():
            logging.error("Cannot send status report: not connected to any APRS server.")
            return

        statusreport = (
            f"{APRS_CALLSIGN}>APFOGO,TCPIP*,ANEPC:"
            f"> ► fogos-2-aprs | Project powered by F4VSE / CT7AJM"
        )

        logging.debug(f"APRS Status Report Preview: {statusreport}")
        logging.info(f"Sending Status: {statusreport}")
        try:
            self.client.sendall(statusreport)
            logging.info(f"Status sent: {statusreport}")
        except Exception as e:
            logging.error(f"Failed to send Status: {e}")
            self.connected = False
