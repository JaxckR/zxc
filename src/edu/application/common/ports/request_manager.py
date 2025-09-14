from abc import abstractmethod
from typing import Protocol


class RequestManager(Protocol):

    @abstractmethod
    def get_refresh_token(self) -> str | None:
        ...

    @abstractmethod
    def add_refresh_token(self, token: str) -> None:
        ...

    @abstractmethod
    def remove_refresh_token(self) -> None:
        ...