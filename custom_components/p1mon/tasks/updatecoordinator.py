from __future__ import annotations

from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
from homeassistant.const import CONF_HOST, CONF_PORT

from custom_components.p1mon.classes import ModuleData, p1mon

##############################################
# Define static values
##############################################
from custom_components.p1mon.const import (
    DOMAIN,
    UPDATE_INTERVAL,
    LOGGER,
    SERVICE_PHASES,
    SERVICE_SETTINGS,
    SERVICE_SMARTMETER
)

class ModuleDataUpdateCoordinator(DataUpdateCoordinator[ModuleData]):

    config_entry = ConfigEntry

    def __init__(
        self,
        hass: HomeAssistant,
    ) -> None:
        super().__init__(
            hass,
            logger=LOGGER,
            name=DOMAIN,
            update_interval=UPDATE_INTERVAL
        )

        self.p1mon = p1mon(
            self.config_entry.data[CONF_HOST], self.config_entry.data[CONF_PORT]
        )

    async def _async_update_data(self) -> ModuleData:
        """Fetch required data from module"""

        LOGGER.debug("Fetching data using p1mon")

        await self.p1mon.clear()

        data = {
            SERVICE_PHASES: await self.p1mon.phases(),
            SERVICE_SETTINGS: await self.p1mon.settings(),
            SERVICE_SMARTMETER: await self.p1mon.smartmeter()
        }

        # LOGGER.debug(data)

        return ModuleData(data)