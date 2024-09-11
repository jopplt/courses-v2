import uuid
from read_models import UserReadModel


class ProjectionStore[T]:
    def __init__(self):
        self.db: dict[uuid.UUID, T] = {}

    def store(self, read_model: T) -> None:
        self.db[read_model.id] = read_model


class UsersStore(ProjectionStore[UserReadModel]):
    def find_by_username(self, username: str) -> UserReadModel | None:
        for user in self.db.values():
            if user.username == username:
                return user
        return None
