"""
fogos-2-aprs
Version: 1.0
Date: 2024-07-25
Description: Symbol definitions for APRS packets based on incident status.
"""

SYMBOLS = {
    "Despacho de 1º Alerta": "#/",
    "Em Curso": "/!",
    # Add more status-symbol mappings as needed
}

def get_symbol(status):
    return SYMBOLS.get(status, "/-")  # Default to "/-" if status is not defined
