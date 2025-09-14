from abc import abstractmethod
from typing import Protocol


class PasswordHasherProtocol(Protocol):

    @abstractmethod
    def hash(self, password: str) -> bytes: ...

    @abstractmethod
    def verify(self, password: str, hashed_password: bytes) -> bool: ...
