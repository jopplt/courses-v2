import uuid
import time
from events import UserSignedUpV1, EventName
from hashlib import sha256
from commands import SignUpCommand
from event_store import EventStore


class SignUpCommandHandler:
    def __init__(self, event_store: EventStore):
        self.event_store = event_store

    def handle(self, command: SignUpCommand):
        encrypted_password = sha256(command.password.encode()).hexdigest()

        # Rule: username must be unique
        for event in self.event_store.events:
            if not event.event_name == EventName.USER_SIGNED_UP:
                continue

            is_same_username = event.payload["username"] == command.username
            is_same_password = event.payload["password"] == encrypted_password

            if is_same_username and is_same_password:
                return

            if is_same_username and not is_same_password:
                raise ValueError("Username already exists")

        event = UserSignedUpV1(
            event_uuid=uuid.uuid4(),
            auto_incrementing_id=1,
            aggregate_id=uuid.uuid4(),
            aggregate_version=1,
            aggregate_name="User",
            payload={"username": command.username, "password": encrypted_password},
            occurred_at=time.time_ns(),
            event_name=EventName.USER_SIGNED_UP,
        )

        self.event_store.commit_event(event)
