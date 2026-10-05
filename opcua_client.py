import asyncio
from asyncua import Client

async def main():
    url = "opc.tcp://localhost:4840/freeopcua/server/"
    async with Client(url=url) as client:
        objects = client.get_objects_node()
        children = await objects.get_children()
        print("Found nodes:", children)

        equipment = await objects.get_child(["2:CV-101"])
        temperature_node = await equipment.get_child(["2:Temperature"])
        value = await temperature_node.read_value()

        print("Temperature:", value)

asyncio.run(main())