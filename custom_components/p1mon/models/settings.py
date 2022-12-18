from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Settings:
    gas_consumption_price: float | None

    energy_consumption_price_high: float | None
    energy_consumption_price_low: float | None

    energy_production_price_high: float | None
    energy_production_price_low: float | None

    def process(data: dict) -> Settings:
        return Settings(
            gas_consumption_price=0,
            energy_consumption_price_high=0,
            energy_consumption_price_low=0,
            energy_production_price_high=0,
            energy_production_price_low=0
        )