from dataclasses import dataclass


@dataclass
class SignUpCommand:
    username: str
    password: str
