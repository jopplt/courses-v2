import secrets
from hashlib import sha256

from queries import CanISignInWithTheseCredentials
from projection_store import UsersStore


class QueryHandler[T]:
    def __init__(self, projection_store: T):
        self.projection_store = projection_store


class CredentialsQueryHandler(QueryHandler[UsersStore]):

    def handle(self, query: CanISignInWithTheseCredentials) -> str | None:
        found_read_model = self.projection_store.find_by_username(query.username)

        if found_read_model is None or found_read_model.password != sha256(query.password.encode()).hexdigest():
            return None

        return secrets.token_hex()  # TODO: Outsource token generation to a separate authz service
