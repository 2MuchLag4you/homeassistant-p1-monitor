from __future__ import annotations

from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.exceptions import ConfigEntryNotReady

from typing import Any

from custom_components.p1mon.tasks import ModuleDataUpdateCoordinator
from custom_components.p1mon.const import (
    DOMAIN,
    PLATFORMS
)


async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool:
    """Setup action components"""

    update_coordinator = ModuleDataUpdateCoordinator(hass)
    try:
        await update_coordinator.async_config_entry_first_refresh()
    except ConfigEntryNotReady:
        raise

    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][config_entry.entry_id] = update_coordinator

    await hass.config_entries.async_forward_entry_setups(config_entry, PLATFORMS)
    # Return successful initialization
    return True