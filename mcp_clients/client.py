import asyncio

from fastmcp import Client


client = Client("http://localhost:8000/mcp")


async def read_resource(uri: str):
    async with client:
        res = await client.read_resource(uri)
        print(res)


async def call_get_user_info_tool(id: str):
    async with client:
        res = await client.call_tool("Get user information", {"user_id": id})
        print(res.structured_content)


async def call_get_pickup_info_tool(id: str):
    async with client:
        res = await client.call_tool("Get pickup information", {"pickup_id": id})
        print(res.structured_content)


async def call_get_active_shipments():
    async with client:
        res = await client.call_tool("List active shipments")
        print(res.structured_content)


async def call_make_prompt(email: str):
    async with client:
        res = await client.get_prompt("Get information about shipments a user is waiting for", {"email": email})
        print(res.messages)


if __name__ == "__main__":
    asyncio.run(read_resource("resource://user-list"))
    asyncio.run(call_get_user_info_tool("pe02"))
    asyncio.run(call_get_pickup_info_tool("pp03"))
    asyncio.run(call_get_pickup_info_tool("pp13"))
    asyncio.run(call_get_active_shipments())
    asyncio.run(call_make_prompt("alice@fastshipping.com"))
