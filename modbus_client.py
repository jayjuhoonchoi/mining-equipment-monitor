from pymodbus.client import ModbusTcpClient

client = ModbusTcpClient("localhost", port=5020)
client.connect()

result = client.read_holding_registers(0, count=2)
print("Raw values:", result.registers)

temperature = result.registers[0] / 10
vibration = result.registers[1] / 10

print("Temperature:", temperature)
print("Vibration:", vibration)

client.close()