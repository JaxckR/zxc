from dataclasses import dataclass
from datetime import datetime
from typing import NewType

from edu.domain.common.entity import OIDEntity

TierID = NewType('TierID', int)


@dataclass
class Tier(OIDEntity[TierID]):
    name: str

    created_at: datetime
    updated_at: datetime | None
