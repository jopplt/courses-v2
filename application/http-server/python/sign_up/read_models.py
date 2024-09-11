import uuid
from dataclasses import dataclass


@dataclass
class ReadModel:
    id: uuid.UUID


@dataclass
class UserReadModel(ReadModel):
    username: str
    password: str
