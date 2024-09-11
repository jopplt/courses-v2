from dataclasses import dataclass


@dataclass
class SignUpRequest:
    username: str
    password: str


@dataclass
class CanISignInWithTheseCredentials:
    username: str
    password: str