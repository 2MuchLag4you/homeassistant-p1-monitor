from typing import TypedDict
from custom_components.p1mon.models import Phases, Settings, SmartMeter

class ModuleData(TypedDict):
    """Class for defining data in module"""
    phases: Phases
    settings: Settings
    smartmeter: SmartMeter