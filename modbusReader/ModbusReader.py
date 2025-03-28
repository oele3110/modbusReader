from pyModbusTCP.client import ModbusClient

from modbusReader.ModbusDataType import ModbusDataType


class ModbusReader:
    def __init__(self, host, port=502):
        print("Initialize Modbus Client")
        self.modbus_client = ModbusClient(host=host, port=port, unit_id=1, auto_open=True)

    def __shutdown__(self):
        print("Shutdown Modbus Client")
        self.modbus_client.close()

    def read_modbus(self, modbus_config):
        result = -1
        if modbus_config["type"] == ModbusDataType.UINT16:
            register = self.modbus_client.read_holding_registers(modbus_config["address"], 1)
            if register:
                result = read_int16(register, signed=False, factor=modbus_config["resolution"], digits_round=modbus_config["digits_round"])
        elif modbus_config["type"] == ModbusDataType.INT16:
            register = self.modbus_client.read_holding_registers(modbus_config["address"], 1)
            if register:
                result = read_int16(register, signed=True, factor=modbus_config["resolution"], digits_round=modbus_config["digits_round"])
        elif modbus_config["type"] == ModbusDataType.UINT32:
            register = self.modbus_client.read_holding_registers(modbus_config["address"], 2)
            if register:
                result = read_int32(register, signed=False, factor=modbus_config["resolution"], digits_round=modbus_config["digits_round"])
        elif modbus_config["type"] == ModbusDataType.INT32:
            register = self.modbus_client.read_holding_registers(modbus_config["address"], 2)
            if register:
                result = read_int32(register, signed=True, factor=modbus_config["resolution"], digits_round=modbus_config["digits_round"])
        elif modbus_config["type"] == ModbusDataType.UINT64:
            register = self.modbus_client.read_holding_registers(modbus_config["address"], 4)
            if register:
                result = read_int64(register, signed=False, factor=modbus_config["resolution"], digits_round=modbus_config["digits_round"])
        elif modbus_config["type"] == ModbusDataType.INT64:
            register = self.modbus_client.read_holding_registers(modbus_config["address"], 4)
            if register:
                result = read_int64(register, signed=True, factor=modbus_config["resolution"], digits_round=modbus_config["digits_round"])
        elif modbus_config["type"] == ModbusDataType.STRING8:
            register = self.modbus_client.read_holding_registers(modbus_config["address"], 4)
            if register:
                result = read_string(register)
        elif modbus_config["type"] == ModbusDataType.STRING16:
            register = self.modbus_client.read_holding_registers(modbus_config["address"], 8)
            if register:
                result = read_string(register)
        elif modbus_config["type"] == ModbusDataType.STRING32:
            register = self.modbus_client.read_holding_registers(modbus_config["address"], 16)
            if register:
                result = read_string(register)
        return result


def read_string(register):
    byte_array = bytearray()
    for value in register:
        byte_array += value.to_bytes(2, byteorder='big')
    decoded_string = byte_array.decode('utf-8').rstrip('\x00')
    return decoded_string


def read_int16(register, signed, factor=1., digits_round=2):
    int16_value = register[0]
    int16_value *= factor
    if signed and int16_value >= 0x8000:
        # convert into signed 16-bit Int
        int16_value -= 0x10000
    if digits_round > 0:
        return round(int16_value, digits_round)
    else:
        return int(int16_value)


def read_int32(register, signed, factor=1., digits_round=2):
    high_register = register[0]
    low_register = register[1]
    int32_value = (high_register << 16) + low_register
    int32_value *= factor
    if signed and int32_value >= 0x80000000:
        # convert into signed 32-bit Int
        int32_value -= 0x100000000
    if digits_round > 0:
        return round(int32_value, digits_round)
    else:
        return int(int32_value)


def read_int64(register, signed, factor=1., digits_round=2):
    high_high_register = register[0]
    high_low_register = register[1]
    low_high_register = register[2]
    low_low_register = register[3]
    int64_value = (high_high_register << 48) + (high_low_register << 32) + (low_high_register << 16) + low_low_register
    int64_value *= factor
    if signed and int64_value >= 0x8000000000000000:
        # convert into signed 64-bit Int
        int64_value -= 0x10000000000000000
    if digits_round > 0:
        return round(int64_value, digits_round)
    else:
        return int(int64_value)
