"""
fogos-2-aprs
Version: 1.0
Date: 2024-07-25
Description: Configuration file for APRS server credentials and Fogos.pt API settings.
"""

APRS_SERVERS = [
    {"host": "rotate.aprs2.net", "port": 14580},
    {"host": "second.server.net", "port": 14580}
]

APRS_CALLSIGN = "YOUR_CALLSIGN"
APRS_PASSWORD = "YOUR_PASSWORD"

FOGOS_API_URL = "https://api.fogos.pt/v1/fires"
CHECK_INTERVAL = 120  # seconds
