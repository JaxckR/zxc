from abc import abstractmethod
from typing import Protocol

from edu.application.common.pagination import Pagination
from edu.domain.user.entity import User
from edu.domain.user.value_objects import Username


class IUserRepository(Protocol):

    @abstractmethod
    async def get_all(self, pagination: Pagination) -> list[User] | list[None]:
        ...

    @abstractmethod
    async def get_by_username(self, username: Username) -> User | None:
        ...

    @abstractmethod
    async def add(self, user: User) -> None:
        ...
