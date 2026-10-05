from pymodbus.server import StartTcpServer
from pymodbus.datastore import ModbusSequentialDataBlock, ModbusServerContext, ModbusDeviceContext

block = ModbusSequentialDataBlock(1, [875, 420])

device_context = ModbusDeviceContext(co=block, di=block, hr=block, ir=block)
context = ModbusServerContext(devices=device_context, single=True)

print("Starting Modbus server on port 5020...")
StartTcpServer(context=context, address=("localhost", 5020))