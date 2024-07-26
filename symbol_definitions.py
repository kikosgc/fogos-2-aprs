"""
fogos-2-aprs
Version: 1.1
Date: 2024-07-26
Description: Symbol definitions for APRS packets based on incident status.
"""

SYMBOLS = {
    "Despacho de 1º Alerta": "\c",
    "Chegada ao TO": "/f",
    "Em Curso": "/:",
    "Em resolução": "/:",
    "Em conclusão": "/d",
    "Vigilância": "/z",
    "Encerrada": "\c"
    # Add more status-symbol mappings as needed
}

def get_symbol(status):
    return SYMBOLS.get(status, "/d")  # Default to "/d" if status is not defined
