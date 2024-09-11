from events import Event, EventName
from projection_store import ProjectionStore
from read_models import UserReadModel


class ProjectionHandler:
    def project(self, event: Event):
        pass


class UserReadModelProjectionHandler(ProjectionHandler):
    def __init__(self, projection_store: ProjectionStore):
        self.projection_store = projection_store

    def project(self, event: Event):
        match event.event_name:
            case EventName.USER_SIGNED_UP:
                user_read_model = UserReadModel(
                    id=event.aggregate_id,
                    username=event.payload["username"],
                    password=event.payload["password"],
                )
                self.projection_store.store(user_read_model)
            case _:
                pass
