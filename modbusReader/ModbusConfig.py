from modbus.ModbusDataType import ModbusDataType

modbus_wallbox_config = {
    "charge_mode":
        {
            "address": 40994,
            "type": ModbusDataType.UINT16,
            "resolution": 1,
            "digits_round": 0,
            "update_frequency": 0.5,
            "display_line": 0,
            "display_string": "Charge mode"
        },
    "wallbox_status_code":
        {
            "address": 49206,
            "type": ModbusDataType.UINT64,
            "resolution": 1,
            "digits_round": 2,
            "update_frequency": 0.5,
            "display_line": 1,
            "display_string": "Status",
            "unit": None
        },
    "active_power_charging":
        {
            "address": 49246,
            "type": ModbusDataType.UINT64,
            "resolution": 1,
            "digits_round": 2,
            "update_frequency": 1,
            "display_line": 2,
            "display_string": "Leistung",
            "unit": "kW",
            "division": 1000000,
            "division_round": 2
        },
    "current_session_energy":
        {
            "address": 49254,
            "type": ModbusDataType.UINT64,
            "resolution": 1,
            "digits_round": 2,
            "update_frequency": 1,
            "display_line": 3,
            "display_string": "Energie",
            "unit": "kWh",
            "division": 1000000,
            "division_round": 2
        },
    "current_session_duration":
        {
            "address": 49258,
            "type": ModbusDataType.UINT64,
            "resolution": 1,
            "digits_round": 2,
            "update_frequency": 30,
            "display_line": 4,
            "display_string": "Dauer",
            "unit": "min",
            "division": 60,
            "division_round": 0
        }
}

modbus_wallbox_status_codes = {
    1: "Nicht verb.",
    2: "Verbunden",
    3: "Pausiert",
    4: "Init",
    5: "Laden",
    6: "Fehler",
    7: "Service Mode",
}

modbus_wallbox_charge_mode = {
    0: "unknown",
    1: "Lock Mode",
    2: "Power Mode",
    3: "Solar Pure Mode",
    4: "Solar Mode Plus"
}
