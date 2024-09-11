import uuid
from enum import Enum
from dataclasses import dataclass, field
from typing import TypedDict


class EventName(Enum):
    USER_SIGNED_UP = "UserSignedUp"


@dataclass
class Event:
    event_uuid: uuid.UUID
    auto_incrementing_id: int
    aggregate_id: uuid.UUID
    aggregate_version: int
    # unique index: aggregate_id, aggregate_version
    aggregate_name: str
    event_name: EventName
    payload: dict
    occurred_at: int
    metadata: dict = field(default_factory=dict)
    correlation_id: str | None = None
    causation_event_uuid: uuid.UUID | None = None


@dataclass
class UserSignedUpV1(Event):
    event_name = EventName.USER_SIGNED_UP
    payload: TypedDict("UserSignedUpV1Payload", {"username": str, "password": str})
