from __future__ import annotations
from custom_components.p1mon.classes import EnergyTariff

def define_tariff(tariff_type) -> str:
    """Get high-low tariff cycle"""
    if tariff_type == 2:
        return EnergyTariff.HIGH
    return EnergyTariff.LOW