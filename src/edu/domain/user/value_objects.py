from dataclasses import dataclass


@dataclass(slots=True)
class Name:
    name: str

    def __post_init__(self) -> None:
        ...


@dataclass(slots=True)
class Username:
    username: str

    def __post_init__(self) -> None:
        ...


@dataclass(slots=True)
class Email:
    email: str

    def __post_init__(self) -> None:
        ...
