from commands import SignUpCommand
from requests import SignUpRequest, CanISignInWithTheseCredentials
from command_handlers import SignUpCommandHandler
from query_handlers import CredentialsQueryHandler


class SignUpEndpoint:
    def __init__(self, command_handler: SignUpCommandHandler):
        self.command_handler = command_handler

    def handle_request(self, request: SignUpRequest):
        command = SignUpCommand(
            username=request.username,
            password=request.password
        )

        self.command_handler.handle(command)


class SignInEndpoint:
    def __init__(self, query_handler: CredentialsQueryHandler):
        self.query_handler = query_handler

    def handle_request(self, request: CanISignInWithTheseCredentials):
        token = self.query_handler.handle(request)
        return token
