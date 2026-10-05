import asyncio
from asyncua import Server

async def main():
    server = Server()
    await server.init()
    server.set_endpoint("opc.tcp://localhost:4840/freeopcua/server/")

    uri = "http://mining-equipment-monitor"
    idx = await server.register_namespace(uri)

    objects = server.get_objects_node()
    equipment = await objects.add_object(idx, "CV-101")
    temperature = await equipment.add_variable(idx, "Temperature", 87.5)
    await temperature.set_writable()

    print("Starting OPC UA server...")
    async with server:
        while True:
            await asyncio.sleep(1)

asyncio.run(main())