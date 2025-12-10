import asyncio

from fastmcp import FastMCP


mcp = FastMCP(name="HTTP Server", instructions="Use of LLM not implemented yet")


if __name__ == "__main__":
    mcp.run(transport="http", port=8000)
