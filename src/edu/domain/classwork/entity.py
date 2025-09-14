from dataclasses import dataclass
from datetime import datetime
from typing import NewType
from uuid import UUID

from edu.domain.common.entity import OIDEntity
from edu.domain.user.entity import UserID

ClassworkID = NewType('ClassworkID', UUID)


@dataclass
class Classwork(OIDEntity[ClassworkID]):
    created_by_user_id: UserID
    title: str
    comment: str
    file_path: str
    file_name: str
    file_size: int

    created_at: datetime
    updated_at: datetime | None
    deleted_at: datetime | None
    is_deleted: bool

