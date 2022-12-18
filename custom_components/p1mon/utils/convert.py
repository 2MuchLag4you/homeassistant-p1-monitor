from __future__ import annotations

def convert(input) -> float | None:
    if input == None: 
        conversion = None
    else:
        conversion = float(input * 1000)
    return conversion 