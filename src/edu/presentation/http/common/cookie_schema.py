from dataclasses import dataclass
from typing import TypeVar, Generic, Literal

T = TypeVar("T")


@dataclass(slots=True)
class CookieData(Generic[T]):
    value: T
    max_age: int = 1
    secure: bool = True
    samesite: Literal["strict", "lax"] | None = "strict"
