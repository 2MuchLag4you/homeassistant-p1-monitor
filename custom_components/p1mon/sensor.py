from __future__ import annotations

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntityDescription,
    SensorStateClass
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import (
    CURRENCY_EURO,
    ELECTRIC_CURRENT_AMPERE,
    ELECTRIC_POTENTIAL_VOLT,
    ENERGY_KILO_WATT_HOUR,
    POWER_WATT,
    VOLUME_CUBIC_METERS
)
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from custom_components.p1mon.entity import P1MonSensorEntity
from custom_components.p1mon.const import (
    DOMAIN,
    SERVICE_PHASES,
    SERVICE_SETTINGS,
    SERVICE_SMARTMETER,
    SERVICES
)

from custom_components.p1mon.const import SERVICE_OBJECTS

SENSORS : dict [
    SERVICE_OBJECTS, tuple[SensorEntityDescription, ...]
] = {
    SERVICE_SMARTMETER: (
        SensorEntityDescription(
            key="gas_consumption",
            name="Gas Consumption",
            entity_registry_enabled_default=False,
            native_unit_of_measurement=VOLUME_CUBIC_METERS,
            device_class=SensorDeviceClass.GAS,
            state_class=SensorStateClass.TOTAL_INCREASING,
        ),
        SensorEntityDescription(
            key="power_consumption",
            name="Power Consumption",
            native_unit_of_measurement=POWER_WATT,
            device_class=SensorDeviceClass.POWER,
            state_class=SensorStateClass.MEASUREMENT,
        ),
        SensorEntityDescription(
            key="energy_consumption_high",
            name="Energy Consumption - High Tariff",
            native_unit_of_measurement=ENERGY_KILO_WATT_HOUR,
            device_class=SensorDeviceClass.ENERGY,
            state_class=SensorStateClass.TOTAL_INCREASING,
        ),
        SensorEntityDescription(
            key="energy_consumption_low",
            name="Energy Consumption - Low Tariff",
            native_unit_of_measurement=ENERGY_KILO_WATT_HOUR,
            device_class=SensorDeviceClass.ENERGY,
            state_class=SensorStateClass.TOTAL_INCREASING,
        ),
        SensorEntityDescription(
            key="power_production",
            name="Power Production",
            native_unit_of_measurement=POWER_WATT,
            device_class=SensorDeviceClass.POWER,
            state_class=SensorStateClass.MEASUREMENT,
        ),
        SensorEntityDescription(
            key="energy_production_high",
            name="Energy Production - High Tariff",
            native_unit_of_measurement=ENERGY_KILO_WATT_HOUR,
            device_class=SensorDeviceClass.ENERGY,
            state_class=SensorStateClass.TOTAL_INCREASING,
        ),
        SensorEntityDescription(
            key="energy_production_low",
            name="Energy Production - Low Tariff",
            native_unit_of_measurement=ENERGY_KILO_WATT_HOUR,
            device_class=SensorDeviceClass.ENERGY,
            state_class=SensorStateClass.TOTAL_INCREASING,
        ),
        SensorEntityDescription(
            key="energy_tariff_period",
            name="Energy Tariff Period",
            icon="mdi:calendar-clock",
        ),
    ),
    SERVICE_PHASES: (
        SensorEntityDescription(
            key="voltage_phase_l1",
            name="Voltage Phase L1",
            native_unit_of_measurement=ELECTRIC_POTENTIAL_VOLT,
            device_class=SensorDeviceClass.VOLTAGE,
            state_class=SensorStateClass.MEASUREMENT,
        ),
        SensorEntityDescription(
            key="voltage_phase_l2",
            name="Voltage Phase L2",
            entity_registry_enabled_default=False,
            native_unit_of_measurement=ELECTRIC_POTENTIAL_VOLT,
            device_class=SensorDeviceClass.VOLTAGE,
            state_class=SensorStateClass.MEASUREMENT,
        ),
        SensorEntityDescription(
            key="voltage_phase_l3",
            name="Voltage Phase L3",
            entity_registry_enabled_default=False,
            native_unit_of_measurement=ELECTRIC_POTENTIAL_VOLT,
            device_class=SensorDeviceClass.VOLTAGE,
            state_class=SensorStateClass.MEASUREMENT,
        ),
        SensorEntityDescription(
            key="current_phase_l1",
            name="Current Phase L1",
            native_unit_of_measurement=ELECTRIC_CURRENT_AMPERE,
            device_class=SensorDeviceClass.CURRENT,
            state_class=SensorStateClass.MEASUREMENT,
        ),
        SensorEntityDescription(
            key="current_phase_l2",
            name="Current Phase L2",
            entity_registry_enabled_default=False,
            native_unit_of_measurement=ELECTRIC_CURRENT_AMPERE,
            device_class=SensorDeviceClass.CURRENT,
            state_class=SensorStateClass.MEASUREMENT,
        ),
        SensorEntityDescription(
            key="current_phase_l3",
            name="Current Phase L3",
            entity_registry_enabled_default=False,
            native_unit_of_measurement=ELECTRIC_CURRENT_AMPERE,
            device_class=SensorDeviceClass.CURRENT,
            state_class=SensorStateClass.MEASUREMENT,
        ),
        SensorEntityDescription(
            key="power_consumed_phase_l1",
            name="Power Consumed Phase L1",
            native_unit_of_measurement=POWER_WATT,
            device_class=SensorDeviceClass.POWER,
            state_class=SensorStateClass.MEASUREMENT,
        ),
        SensorEntityDescription(
            key="power_consumed_phase_l2",
            name="Power Consumed Phase L2",
            entity_registry_enabled_default=False,
            native_unit_of_measurement=POWER_WATT,
            device_class=SensorDeviceClass.POWER,
            state_class=SensorStateClass.MEASUREMENT,
        ),
        SensorEntityDescription(
            key="power_consumed_phase_l3",
            name="Power Consumed Phase L3",
            entity_registry_enabled_default=False,
            native_unit_of_measurement=POWER_WATT,
            device_class=SensorDeviceClass.POWER,
            state_class=SensorStateClass.MEASUREMENT,
        ),
        SensorEntityDescription(
            key="power_produced_phase_l1",
            name="Power Produced Phase L1",
            native_unit_of_measurement=POWER_WATT,
            device_class=SensorDeviceClass.POWER,
            state_class=SensorStateClass.MEASUREMENT,
        ),
        SensorEntityDescription(
            key="power_produced_phase_l2",
            name="Power Produced Phase L2",
            entity_registry_enabled_default=False,
            native_unit_of_measurement=POWER_WATT,
            device_class=SensorDeviceClass.POWER,
            state_class=SensorStateClass.MEASUREMENT,
        ),
        SensorEntityDescription(
            key="power_produced_phase_l3",
            name="Power Produced Phase L3",
            entity_registry_enabled_default=False,
            native_unit_of_measurement=POWER_WATT,
            device_class=SensorDeviceClass.POWER,
            state_class=SensorStateClass.MEASUREMENT,
        ),
    ),
    SERVICE_SETTINGS: (
        SensorEntityDescription(
            key="gas_consumption_price",
            name="Gas Consumption Price",
            entity_registry_enabled_default=False,
            state_class=SensorStateClass.MEASUREMENT,
            native_unit_of_measurement=f"{CURRENCY_EURO}/{VOLUME_CUBIC_METERS}",
        ),
        SensorEntityDescription(
            key="energy_consumption_price_low",
            name="Energy Consumption Price - Low",
            state_class=SensorStateClass.MEASUREMENT,
            native_unit_of_measurement=f"{CURRENCY_EURO}/{ENERGY_KILO_WATT_HOUR}",
        ),
        SensorEntityDescription(
            key="energy_consumption_price_high",
            name="Energy Consumption Price - High",
            state_class=SensorStateClass.MEASUREMENT,
            native_unit_of_measurement=f"{CURRENCY_EURO}/{ENERGY_KILO_WATT_HOUR}",
        ),
        SensorEntityDescription(
            key="energy_production_price_low",
            name="Energy Production Price - Low",
            state_class=SensorStateClass.MEASUREMENT,
            native_unit_of_measurement=f"{CURRENCY_EURO}/{ENERGY_KILO_WATT_HOUR}",
        ),
        SensorEntityDescription(
            key="energy_production_price_high",
            name="Energy Production Price - High",
            state_class=SensorStateClass.MEASUREMENT,
            native_unit_of_measurement=f"{CURRENCY_EURO}/{ENERGY_KILO_WATT_HOUR}",
        ),
    )
}

async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback
) -> None:
    async_add_entities(
        P1MonSensorEntity(
            coordinator=hass.data[DOMAIN][entry.entry_id],
            description=description,
            service_key=service_key,
            name=entry.title,
            service=SERVICES[service_key],
        )
        for service_key, service_sensors in SENSORS.items()
        for description in service_sensors
    )
