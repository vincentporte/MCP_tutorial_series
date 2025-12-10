import asyncio
import random

from datas import (
    PICKUP_TABLE,
    SHIPMENT_TABLE,
    USER_TABLE,
    Pickup,
    PickupId,
    Shipment,
    ShipmentId,
    ShipmentStatus,
    User,
    UserId,
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


@mcp.tool(
    name="Get user information",
    description="Retrieve the name, email and postal code of a user based on his ID",
    tags={"user", "get"},
)
async def get_user_info(user_id: UserId) -> str:
    await asyncio.sleep(random.random())
    user_info = USER_TABLE.get(user_id)
    if user_info:
        return f"{user_info['name']} ({user_info['email']}) lives next to {user_info['postal_code']}"
    return "user not found"


@mcp.tool(
    name="Get pickup information",
    description="Retrieve the pickup capacity and postal code based on its ID",
    tags={"pickup-point", "get"},
)
async def get_pickup_info(pickup_id: PickupId) -> Pickup | None:
    await asyncio.sleep(random.random())
    return PICKUP_TABLE.get(pickup_id, None)


@mcp.tool(
    name="List active shipments",
    description="Retrieve shipments with status awaiting deposit, awaiting pickup, in transit or awaiting withdraw",
    tags={"shipment", "list"},
)
async def get_active_shipment() -> dict[ShipmentId, Shipment]:
    await asyncio.sleep(random.random())
    return {k: v for k, v in SHIPMENT_TABLE.items() if v["status"].value <= ShipmentStatus.AWAITING_WITHDRAW.value}


if __name__ == "__main__":
    mcp.run(transport="http", port=8000)
