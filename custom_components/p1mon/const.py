
from datetime import timedelta
from typing import Final, Literal
import logging
from homeassistant.const import Platform

NAME_LONG = "P1 Monitor (Custom module)"
NAME_SHORT = "P1MON"
DOMAIN = "p1mon"
VERSION = 1.0
LOGGER = logging.getLogger(__package__)
UPDATE_INTERVAL = timedelta(seconds=300)

MANUFACTURER="2MuchLag4You"

PACKAGE_NAME = "custom_components.{DOMAIN}"

PLATFORMS = [Platform.SENSOR]

SERVICE_SMARTMETER: Final = "smartmeter"
SERVICE_PHASES: Final = "phases"
SERVICE_SETTINGS: Final = "settings"

SERVICES: dict[str, str] = {
    SERVICE_SMARTMETER: "SmartMeter",
    SERVICE_PHASES: "Phases",
    SERVICE_SETTINGS: "Settings",
}

SERVICE_OBJECTS = Literal["smartmeter", "phases", "settings"]