from __future__ import annotations
from custom_components.p1mon.utils import convert
from dataclasses import dataclass

@dataclass
class Phases: 
    voltage_phase_l1: float | None
    voltage_phase_l2: float | None
    voltage_phase_l3: float | None

    current_phase_l1: float | None
    current_phase_l2: float | None
    current_phase_l3: float | None

    power_consumed_phase_l1: float | None
    power_consumed_phase_l2: float | None
    power_consumed_phase_l3: float | None

    power_produced_phase_l1: float | None
    power_produced_phase_l2: float | None
    power_produced_phase_l3: float | None

    @staticmethod
    def process(data: dict) -> Phases:
        return Phases(
            power_consumed_phase_l1=convert(data["power_consumed_phase_l1"]),
            power_consumed_phase_l2=convert(data["power_consumed_phase_l2"]),
            power_consumed_phase_l3=convert(data["power_consumed_phase_l3"]),
            power_produced_phase_l1=convert(data["power_produced_phase_l1"]),
            power_produced_phase_l2=convert(data["power_produced_phase_l2"]),
            power_produced_phase_l3=convert(data["power_produced_phase_l3"]),
            voltage_phase_l1=data["voltage_phase_l1"],
            voltage_phase_l2=data["voltage_phase_l2"],
            voltage_phase_l3=data["voltage_phase_l3"],
            current_phase_l1=data["current_phase_l1"],
            current_phase_l2=data["current_phase_l2"],
            current_phase_l3=data["current_phase_l3"]
        )


