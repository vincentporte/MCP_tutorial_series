import asyncio

from fastmcp import Client


client = Client("http://localhost:8000/mcp")


async def main():
    async with client:
        tools = await client.list_tools()
        print("\nYour server has the following tools:")
        for tool in tools:
            print(f"{tool.name}: {tool.description}")

        resources = await client.list_resources()
        print("\nYour server has the following resources:")
        for resource in resources:
            print(f"{resource.name}: {resource.description} (URI: {resource.uri})")

        prompts = await client.list_prompts()
        print("\nYour server has the following prompts:")
        for prompt in prompts:
            print(f"{prompt.name}: {prompt.description}")


if __name__ == "__main__":
    asyncio.run(main())
