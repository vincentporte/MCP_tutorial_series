import asyncio
import random

from datas import (
    User,
)
from fastmcp import FastMCP


mcp = FastMCP(name="HTTP Server", instructions="Use of LLM not implemented yet")


@mcp.resource(
    uri="resource://user-list",
    name="List users",
    description="Retrieve the full list of known users with their IDs",
    tags={"user", "list"},
)
async def list_users() -> list[User]:
    await asyncio.sleep(random.random())
    return USER_TABLE


if __name__ == "__main__":
    mcp.run(transport="http", port=8000)
