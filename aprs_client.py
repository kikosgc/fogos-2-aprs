"""
fogos-2-aprs
Version: 2.0
Date: 2024-07-29
Description: Manages APRS connection and packet creation.
"""

import aprslib
from config import APRS_CALLSIGN, APRS_PASSWORD, APRS_SERVERS
from symbol_definitions import get_symbol

class APRSClient:
    def __init__(self):
        self.client = aprslib.IS(APRS_CALLSIGN, passwd=APRS_PASSWORD)
        self.connected = False

    def connect(self):
        for server in APRS_SERVERS:
            try:
                self.client.connect(server)
                self.connected = True
                return True
            except Exception as e:
                print(f"Failed to connect to {server}: {e}")
        return False

    def send_packet(self, callsign, lat, lon, symbol, comment, status_comment):
        if not self.connected:
            print("Not connected to APRS server.")
            return

        packet = {
            'from': APRS_CALLSIGN,
            # ??? MSG ??? 'to': callsign,
            'path': 'APRS',
            'lat': lat,
            'lng': lon,  # Note: aprslib uses 'lng' instead of 'lon'
            'symbol': symbol,
            'comment': f"{comment} {status_comment}"
        }
        try:
            self.client.sendall(packet)
        except Exception as e:
            print(f"Failed to send packet: {e}")
