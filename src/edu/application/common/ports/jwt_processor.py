from abc import abstractmethod
from typing import Protocol, Literal
from dataclasses import dataclass

from edu.domain.user.entity import UserID


@dataclass(slots=True)
class JWTPayload:
    oid: UserID


class JWTProcessor(Protocol):

    @abstractmethod
    def encode(self, raw_payload: JWTPayload, token_type: Literal["access", "refresh"]) -> str:
        ...

    @abstractmethod
    def decode(self, token: str | bytes) -> dict:
        ...