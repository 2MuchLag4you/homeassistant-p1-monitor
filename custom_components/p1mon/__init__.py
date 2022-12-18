
from __future__ import annotations
from typing import Any

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from custom_components.p1mon.operational import (
    p1mon_ui_setup
)
from custom_components.p1mon.const import DOMAIN, PLATFORMS

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry):
    """Configure intergration using UI"""
    config_entry.add_update_listener(async_reload_entry)
    return await p1mon_ui_setup(hass, config_entry)

async def async_unload_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> bool:
    unload_ok = await hass.config_entries.async_unload_platforms(config_entry, PLATFORMS)
    if unload_ok:
        del hass.data[DOMAIN][config_entry.entry_id]
    return unload_ok

async def async_reload_entry(hass: HomeAssistant, config_entry: ConfigEntry) -> None:
    await async_unload_entry(hass, config_entry)
    await async_setup_entry(hass, config_entry)