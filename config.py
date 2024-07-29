"""
fogos-2-aprs
Version: 1.3
Date: 2024-07-29
Description: Configuration file for APRS server and credentials.
"""
APRS_CALLSIGN = "CALLSIGN"
APRS_PASSWORD = "PASSWORD"
APRS_SERVERS = [
    {"host": "193.137.237.12", "port": 14580},
    {"host": "ct1ejc.dynip.sapo.pt", "port": 14579},
    {"host": "euro.aprs2.net", "port": 14580},
    {"host": "rotate.aprs2.net", "port": 14580}
]
