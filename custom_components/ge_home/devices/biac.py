import logging
from typing import List

from homeassistant.helpers.entity import Entity
from gehomesdk.erd import ErdCode, ErdApplianceType

from .base import ApplianceApi
from ..entities import GeSacClimate, GeErdSensor, GeErdSwitch, ErdOnOffBoolConverter, GeErdBinarySensor


_LOGGER = logging.getLogger(__name__)


class BiacApi(ApplianceApi):
    """API class for Built-In AC objects"""
    APPLIANCE_TYPE = ErdApplianceType.BUILT_IN_AIR_CONDITIONER

    def get_all_entities(self) -> List[Entity]:
        base_entities = super().get_all_entities()

        sac_entities = [
            GeSacClimate(self),
            GeErdSensor(self, ErdCode.AC_TARGET_TEMPERATURE),
            GeErdSensor(self, ErdCode.AC_AMBIENT_TEMPERATURE),
            GeErdSensor(self, ErdCode.AC_FAN_SETTING, icon_override="mdi:fan"),
            GeErdSensor(self, ErdCode.AC_OPERATION_MODE),
            GeErdSwitch(self, ErdCode.AC_POWER_STATUS, bool_converter=ErdOnOffBoolConverter(), icon_on_override="mdi:power-on", icon_off_override="mdi:power-off"),
            GeErdBinarySensor(self, ErdCode.AC_FILTER_STATUS, device_class_override="problem"),
            GeErdSensor(self, ErdCode.WAC_DEMAND_RESPONSE_STATE),
            GeErdSensor(self, ErdCode.WAC_DEMAND_RESPONSE_POWER, uom_override="kW"),
        ]

        entities = base_entities + sac_entities
        return entities

