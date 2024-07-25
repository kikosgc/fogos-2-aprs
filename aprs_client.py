"""
fogos-2-aprs
Version: 1.0
Date: 2024-07-25
Description: Manages APRS connection and packet creation.
"""

import aprs
from config import APRS_CALLSIGN, APRS_PASSWORD, APRS_SERVERS
from symbol_definitions import get_symbol

class APRSClient:
    def __init__(self):
        self.client = aprs.TCP(APRS_CALLSIGN, APRS_PASSWORD)

    def connect(self):
        for server in APRS_SERVERS:
            try:
                self.client.connect(server["host"], server["port"])
                return True
            except Exception as e:
                print(f"Failed to connect to {server['host']}: {e}")
        return False

    def send_packet(self, callsign, lat, lon, symbol, comment, status_comment):
        frame = aprs.APRSFrame(
            source=APRS_CALLSIGN,
            destination=callsign,
            path="APRS",
            info=f"{lat}/{lon}{symbol}{comment} {status_comment}"
        )
        self.client.send(frame)
