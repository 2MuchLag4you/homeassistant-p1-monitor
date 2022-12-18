from __future__ import annotations


from homeassistant.components.sensor import (
    DOMAIN as SENSOR_DOMAIN,
    SensorEntity,
    SensorEntityDescription
)

from homeassistant.helpers.device_registry import DeviceEntryType
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.typing import StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from custom_components.p1mon.tasks import ModuleDataUpdateCoordinator
from custom_components.p1mon.const import (
    DOMAIN, 
    MANUFACTURER,
    SERVICE_OBJECTS
)

class P1MonSensorEntity(CoordinatorEntity, SensorEntity):
    """Defines an P1 Monitor sensor."""

    coordinator: ModuleDataUpdateCoordinator

    def __init__(
        self,
        *,
        coordinator: ModuleDataUpdateCoordinator,
        description: SensorEntityDescription,
        service_key: SERVICE_OBJECTS,
        name: str,
        service: str,
    ) -> None:
        """Initialize P1 Monitor sensor."""
        super().__init__(coordinator=coordinator)
        self._service_key = service_key

        self.entity_id = f"{SENSOR_DOMAIN}.{name}_{description.key}"
        self.entity_description = description
        self._attr_unique_id = (
            f"{coordinator.config_entry.entry_id}_{service_key}_{description.key}"
        )

        self._attr_device_info = DeviceInfo(
            entry_type=DeviceEntryType.SERVICE,
            identifiers={
                (DOMAIN, f"{coordinator.config_entry.entry_id}_{service_key}")
            },
            manufacturer=MANUFACTURER,
            name=service,
        )

    @property
    def native_value(self) -> StateType:
        """Return the state of the sensor."""
        value = getattr(
            self.coordinator.data[self._service_key], self.entity_description.key
        )
        if isinstance(value, str):
            return value.lower()
        return value
