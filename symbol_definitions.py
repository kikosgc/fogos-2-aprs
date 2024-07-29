"""
fogos-2-aprs
Version: 1.2
Date: 2024-07-29
Description: Symbol definitions for APRS packets based on incident status.
"""

def get_symbol(status):
    # Add more status-symbol mappings as needed -
    symbol_map = {
        "Despacho de 1º Alerta": "\c",
        "Chegada ao TO": "/f",
        "Em Curso": "/:",
        "Em resolução": "/:",
        "Em conclusão": "/d",
        "Vigilância": "/z",
        "Encerrada": "\c"
    }
    return symbol_map.get(status, "/d")  # Default to "/d" if status is not defined
