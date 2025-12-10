from datetime import datetime
from enum import Enum
from typing import TypedDict


PersonId = str
PickUpPointId = str
ShippingId = str


class Person(TypedDict):
    name: str
    email: str
    postal_code: str


class PickUpPoint(TypedDict):
    postal_code: str
    available_capacity: int


class Shipping(TypedDict):
    sender_id: PersonId
    deposit_pickup_point_id: PickUpPointId | None
    recipient_id: PersonId
    withdrawal_pickup_point_id: PickUpPointId | None
    status: ShippingStatus
    updated_at: datetime


class ShippingStatus(Enum):
    AWAITING_DEPOSIT = 0
    PENDING_PICKUP = 1
    IN_TRANSIT = 2
    PENDING_WITHDRAW = 3
    WITHDRAWN = 4
    CANCELLED = 5
    RETURNED = 6


PEOPLE_TABLE: dict[PersonId, Person] = {
    "pe01": {
        "name": "Alice Johnson",
        "email": "alice@fastshipping.com",
        "postal_code": "FR-14000",
    },
    "pe02": {
        "name": "Jeanne Blackwood",
        "email": "jeanne@fastshipping.com",
        "postal_code": "FR-76000",
    },
    "pe03": {
        "name": "Sophie Brown",
        "email": "sophie@fastshipping.com",
        "postal_code": "FR-05100",
    },
}

PICKUP_POINT_TABLE: dict[PickUpPointId, PickUpPoint] = {
    "pp01": {
        "postal_code": "FR-14000",
        "available_capacity": 5,
    },
    "pp02": {
        "postal_code": "FR-76000",
        "available_capacity": 0,
    },
    "pp03": {
        "postal_code": "FR-05100",
        "available_capacity": 2,
    },
    "pp04": {
        "postal_code": "FR-54000",
        "available_capacity": 8,
    },
    "pp05": {
        "postal_code": "FR-94130",
        "available_capacity": 0,
    },
}

SHIPPING_TABLE: dict[ShippingId, Shipping] = {
    "sh01": {
        "sender_id": "pe03",
        "deposit_pickup_point_id": "pp03",
        "recipient_id": "pe01",
        "withdrawal_pickup_point_id": "pp01",
        "status": ShippingStatus.WITHDRAWN,
        "updated_at": datetime.fromisoformat("2025-12-01T12:00:00"),
    },
    "sh02": {
        "sender_id": "pe02",
        "deposit_pickup_point_id": "pp04",
        "recipient_id": "pe03",
        "withdrawal_pickup_point_id": "pp03",
        "status": ShippingStatus.PENDING_WITHDRAW,
        "updated_at": datetime.fromisoformat("2025-12-02T10:00:00"),
    },
    "sh03": {
        "sender_id": "pe01",
        "deposit_pickup_point_id": "pp01",
        "recipient_id": "pe02",
        "withdrawal_pickup_point_id": "pp02",
        "status": ShippingStatus.IN_TRANSIT,
        "updated_at": datetime.fromisoformat("2025-12-03T14:00:00"),
    },
    "sh04": {
        "sender_id": "pe01",
        "deposit_pickup_point_id": "pp01",
        "recipient_id": "pe03",
        "withdrawal_pickup_point_id": "pp03",
        "status": ShippingStatus.AWAITING_DEPOSIT,
        "updated_at": datetime.fromisoformat("2025-12-04T15:00:00"),
    },
    "sh05": {
        "sender_id": "pe03",
        "deposit_pickup_point_id": "pp03",
        "recipient_id": "pe02",
        "withdrawal_pickup_point_id": "pp02",
        "status": ShippingStatus.IN_TRANSIT,
        "updated_at": datetime.fromisoformat("2025-12-05T15:00:00"),
    },
    "sh06": {
        "sender_id": "pe03",
        "deposit_pickup_point_id": None,
        "recipient_id": "pe01",
        "withdrawal_pickup_point_id": None,
        "status": ShippingStatus.CANCELLED,
        "updated_at": datetime.fromisoformat("2025-12-04T18:00:00"),
    },
}
