from abc import abstractmethod
from typing import Protocol

from edu.domain.user.entity import UserID


class IDGenerator(Protocol):

    @abstractmethod
    def generate_user_id(self) -> UserID:
        ...
