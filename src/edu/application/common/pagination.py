from dataclasses import dataclass


@dataclass(slots=True)
class Pagination:
    limit: int | None = None
    offset: int | None = None
