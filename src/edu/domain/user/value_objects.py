from dataclasses import dataclass
from re import compile
from typing import Final, Pattern

from edu.domain.user.exceptions import MinLengthError, MaxLengthError, UsernameError, EmailError

USER_REGEX: Final[Pattern[str]] = compile(r"^[A-Za-z][A-Za-z0-9_]*$")
EMAIL_REGEX: Final[Pattern[str]] = compile(r"^[a-zA-Z]+[\w._]+@[\w.]+\.[a-zA-Z]+$")


@dataclass(slots=True)
class Name:
    name: str

    def __post_init__(self) -> None:
        MIN_LENGTH: Final[int] = 2
        MAX_LENGTH: Final[int] = 64
        if len(self.name) < MIN_LENGTH:
            raise MinLengthError("Name is too short", MIN_LENGTH)

        if len(self.name) > MAX_LENGTH:
            raise MaxLengthError("Name is too long", MAX_LENGTH)


@dataclass(slots=True)
class Username:
    username: str

    def __post_init__(self) -> None:
        MIN_LENGTH: Final[int] = 2
        MAX_LENGTH: Final[int] = 64

        if len(self.username) < MIN_LENGTH:
            raise MinLengthError("Username is too short", MIN_LENGTH)

        if len(self.username) > MAX_LENGTH:
            raise MaxLengthError("Username is too long", MAX_LENGTH)

        if not USER_REGEX.match(self.username):
            raise UsernameError


@dataclass(slots=True)
class Email:
    email: str

    def __post_init__(self) -> None:
        if not EMAIL_REGEX.match(self.email):
            raise EmailError


@dataclass(slots=True)
class RawPassword:
    password: str

    def __post_init__(self) -> None:
        MIN_LENGTH: Final[int] = 8

        if len(self.password) < MIN_LENGTH:
            raise MinLengthError("Password is too short", MIN_LENGTH)
