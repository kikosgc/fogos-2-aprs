"""
fogos-2-aprs
Version: 1.1
Date: 2024-07-26
Description: Configuration file for APRS server credentials and Fogos.pt API settings.
"""

APRS_SERVERS = [
    {"host": "193.137.237.12", "port": 14580},
    {"host": "ct1ejc.dynip.sapo.pt", "port": 14579},
    {"host": "euro.aprs2.net", "port": 14580},
    {"host": "rotate.aprs2.net", "port": 14580}
]

APRS_CALLSIGN = "YOUR_CALLSIGN"
APRS_PASSWORD = "YOUR_PASSWORD"

FOGOS_API_URL = "https://api.fogos.pt/v1/fires"
CHECK_INTERVAL = 120  # seconds
