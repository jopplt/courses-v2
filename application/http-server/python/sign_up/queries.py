from dataclasses import dataclass


@dataclass
class CanISignInWithTheseCredentials:
    username: str
    password: str
