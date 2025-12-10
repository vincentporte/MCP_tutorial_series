import asyncio

from fastmcp import Client


client = Client("http://localhost:8000/mcp")


async def main():
    async with client:
        resources = await client.list_resources()
        print("\nYour server has the following resources:")
        for resource in resources:
            print(f"{resource.name}: {resource.description} (URI: {resource.uri})")


if __name__ == "__main__":
    asyncio.run(main())
