from homeassistant.components.water_heater import WaterHeaterEntityFeature

ATTR_DOOR_STATUS = "door_status"
GE_FRIDGE_SUPPORT = (WaterHeaterEntityFeature.OPERATION_MODE | WaterHeaterEntityFeature.TARGET_TEMPERATURE)

HEATER_TYPE_FRIDGE = "fridge"
HEATER_TYPE_FREEZER = "freezer"
HEATER_TYPE_DISPENSER = "dispenser"

# Fridge/Freezer
OP_MODE_OFF = "Off"
OP_MODE_K_CUP = "K-Cup Brewing"
OP_MODE_NORMAL = "Normal"
OP_MODE_SABBATH = "Sabbath Mode"
OP_MODE_TURBO_COOL = "Turbo Cool"
OP_MODE_TURBO_FREEZE = "Turbo Freeze"
