from dataclasses import dataclass
from typing import override

from edu.domain.common.exceptions import DomainError


@dataclass(slots=True)
class MinLengthError(DomainError):
    msg: str | None
    min_length: int

    @override
    @property
    def message(self) -> str:
        return self.msg or f"Length must be at least {self.min_length}"


@dataclass(slots=True)
class MaxLengthError(DomainError):
    msg: str | None
    max_length: int

    @override
    @property
    def message(self) -> str:
        return self.msg or f"Length must be at most {self.max_length}"


class UsernameError(DomainError):

    @override
    @property
    def message(self) -> str:
        return "Username must start with a letter and contain only [A-Za-z0-9_]"


class EmailError(DomainError):

    @override
    @property
    def message(self) -> str:
        return "Invalid email address"
