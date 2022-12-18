from __future__ import annotations
from dataclasses import dataclass
from custom_components.p1mon.utils import define_tariff, convert
from typing import Any

@dataclass
class SmartMeter:

    gas_consumption: float | None
    energy_tariff_period: str | None

    power_consumption: int | None
    energy_consumption_high: float | None
    energy_consumption_low: float | None

    power_production: int | None
    energy_production_high: float | None
    energy_production_low: float | None

    @staticmethod
    def process(fetched_data: dict[str, Any]) -> SmartMeter:
        return SmartMeter(
            gas_consumption=0,
            energy_tariff_period=define_tariff(fetched_data.get("TARIFF")),
            power_consumption=convert(fetched_data["CONSUMPTION_W_TODAY"]),
            energy_consumption_high=fetched_data["CONSUMPTION_KWH_HIGH"],
            energy_consumption_low=fetched_data["CONSUMPTION_KWH_LOW"],
            power_production=fetched_data["PRODUCTION_W_TODAY"],
            energy_production_high=fetched_data["PRODUCTION_KWH_HIGH"],
            energy_production_low=fetched_data["PRODUCTION_KWH_LOW"]
        )