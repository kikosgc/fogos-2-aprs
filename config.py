"""
fogos-2-aprs
Version: 2.0
Date: 2026-05-21
Description: Configuration file for APRS server and credentials.
             Credentials and sensitive values are loaded from environment
             variables. Copy .env.example to .env and fill in your values.
"""

import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env if present

APRS_CALLSIGN = os.environ.get("APRS_CALLSIGN", "CALLSIGN")
APRS_PASSWORD = os.environ.get("APRS_PASSWORD", "PASSWORD")

APRS_SERVERS = [
    {"host": "euro.aprs2.net", "port": 14580}
]

# Filter: only incidents whose 'Natureza' matches this value are forwarded.
# Set to None to forward all incident types.
NATUREZA_FILTER = os.environ.get("NATUREZA_FILTER", "Mato")

# Position report coordinates for the beacon (APRS format strings).
# Default: ANEPC headquarters in Carnaxide, Portugal.
POSITION_LAT = os.environ.get("POSITION_LAT", "3843.23N")
POSITION_LON = os.environ.get("POSITION_LON", "00914.18W")
POSITION_COMMENT = os.environ.get(
    "POSITION_COMMENT",
    "ANEPC - Autoridade Nacional de Emergência e Proteção Civil"
)
