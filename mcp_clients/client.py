import asyncio

from fastmcp import Client


client = Client("http://localhost:8000/mcp")


async def read_resource(uri: str):
    async with client:
        res = await client.read_resource(uri)
        print(res)


if __name__ == "__main__":
    asyncio.run(read_resource("resource://user-list"))
