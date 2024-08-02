"""
fogos-2-aprs
Version: 1.5
Date: 2024-08-02
Description: Symbol definitions for APRS packets based on incident status.
"""

def get_symbol(status):
    # Add more status-symbol mappings as needed
    symbol_map = {
        "Despacho de 1.º Alerta": ("\\", "!"),
        "Chegada ao TO": ("/", "f"),
        "Em Curso": ("/", ":"),
        "Em resolução": ("/", ":"),
        "Conclusão": ("/", "d"),
        "Vigilância": ("\\", "c"),
        "Encerrada": ("\\", "f")
    }
    return symbol_map.get(status, ("/", ":"))  # Default to ("/", "d")
    