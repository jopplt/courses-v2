from event_store import EventStore
from projection_store import UsersStore
from endpoints import SignInEndpoint, SignUpEndpoint
from command_handlers import SignUpCommandHandler
from query_handlers import CredentialsQueryHandler
from projection_handlers import UserReadModelProjectionHandler
from requests import SignUpRequest, CanISignInWithTheseCredentials

event_store = EventStore()
users_read_store = UsersStore()

auth_read_model_projection_handler = UserReadModelProjectionHandler(users_read_store)

event_store.subscribe(auth_read_model_projection_handler)

sign_up_command_handler = SignUpCommandHandler(event_store)
sign_in_query_handler = CredentialsQueryHandler(users_read_store)

sign_in_endpoint = SignInEndpoint(sign_in_query_handler)
sign_up_endpoint = SignUpEndpoint(sign_up_command_handler)


def do_sign_up(username: str, password: str):
    print(f"Trying to sign up with ('{username}', '{password}')")
    request = SignUpRequest(username=username, password=password)
    try:
        sign_up_endpoint.handle_request(request)
        print("OK")
    except ValueError as e:
        print(e)


def do_sign_in(username: str, password: str) -> str:
    print(f"Trying to sign in with ('{username}', '{password}')")
    request = CanISignInWithTheseCredentials(username=username, password=password)
    token = sign_in_endpoint.handle_request(request)

    if token is None:
        print("Invalid credentials")
    else:
        print(f"Welcome {request.username}!")
        print(f"Token: {token}")
    return token


do_sign_up(username="test", password="test")  # Should succeed
do_sign_up(username="test", password="test")  # Idempotent, should not create a new user
do_sign_up(username="test", password="test2")  # Should fail, username already exists
assert len(event_store.events) == 1
assert len(users_read_store.db) == 1

token1 = do_sign_in(username="test", password="test")  # Should succeed
token2 = do_sign_in(username="test", password="wrong password")  # Should fail
token3 = do_sign_in(username="anonymous", password="")  # Should fail
assert token1 is not None
assert token2 is None
assert token3 is None

