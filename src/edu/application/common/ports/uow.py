from typing import Protocol
from abc import abstractmethod


class UoW(Protocol):

    @abstractmethod
    async def commit(self) -> None:
        ...

    @abstractmethod
    async def flush(self) -> None:
        ...