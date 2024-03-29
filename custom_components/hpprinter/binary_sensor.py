"""
Support for HP Printer binary sensors.
For more details about this platform, please refer to the documentation at
https://home-assistant.io/components/binary_sensor.hp_printer/
"""
from __future__ import annotations

import logging

from homeassistant.components.binary_sensor import (
    BinarySensorDeviceClass,
    BinarySensorEntity,
)
from homeassistant.core import HomeAssistant

from .helpers.const import *
from .models.base_entity import HPPrinterEntity, async_setup_base_entry
from .models.entity_data import EntityData

_LOGGER = logging.getLogger(__name__)


CURRENT_DOMAIN = DOMAIN_BINARY_SENSOR


def get_binary_sensor(hass: HomeAssistant, integration_name: str, entity: EntityData):
    binary_sensor = HPPrinterBinarySensor()
    binary_sensor.initialize(hass, integration_name, entity, CURRENT_DOMAIN)

    return binary_sensor


async def async_setup_entry(hass: HomeAssistant, entry, async_add_entities):
    """Set up HP Printer based off an entry."""
    await async_setup_base_entry(
        hass, entry, async_add_entities, CURRENT_DOMAIN, get_binary_sensor
    )


async def async_unload_entry(_hass, config_entry):
    _LOGGER.info(f"async_unload_entry {CURRENT_DOMAIN}: {config_entry}")

    return True


class HPPrinterBinarySensor(BinarySensorEntity, HPPrinterEntity):
    """Representation a binary sensor that is updated by HP Printer."""

    @property
    def is_on(self):
        """Return true if the binary sensor is on."""
        return bool(self.entity.state)

    @property
    def device_class(self) -> BinarySensorDeviceClass | str | None:
        """Return the class of this sensor."""
        return self.entity.binary_sensor_device_class

    async def async_added_to_hass_local(self):
        _LOGGER.info(f"Added new {self.name}")

    def _immediate_update(self, previous_state: bool):
        if previous_state != self.entity.state:
            _LOGGER.debug(
                f"{self.name} updated from {previous_state} to {self.entity.state}"
            )

        super()._immediate_update(previous_state)
