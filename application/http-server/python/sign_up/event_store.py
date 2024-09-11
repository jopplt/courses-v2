from events import Event
from projection_handlers import ProjectionHandler


class EventStore:
    def __init__(self):
        self.events: list[Event] = []
        self.subscribers: list[ProjectionHandler] = []
        self.internal_counter = 0

    def subscribe(self, subscriber: ProjectionHandler):
        self.subscribers.append(subscriber)

    def commit_event(self, event: Event) -> Event:
        try:
            # TODO: implement simple lock for aggregate stream
            event.auto_incrementing_id = self.internal_counter + 1
            self.events.append(event)
            self.internal_counter += 1

            for subscriber in self.subscribers:
                subscriber.project(event)

            return event
        except Exception as e:
            raise e
