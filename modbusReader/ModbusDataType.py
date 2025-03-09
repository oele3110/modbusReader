from enum import Enum


class ModbusDataType(Enum):
    UINT16 = 1
    INT16 = 2
    UINT32 = 3
    INT32 = 4
    UINT64 = 5
    INT64 = 6
    STRING8 = 7
    STRING16 = 8
    STRING32 = 9
