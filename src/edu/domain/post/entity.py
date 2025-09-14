from dataclasses import dataclass
from datetime import datetime
from typing import NewType
from uuid import UUID

from edu.domain.common.entity import OIDEntity
from edu.domain.user.entity import UserID

PostID = NewType('PostID', UUID)


@dataclass
class Post(OIDEntity[PostID]):
    title: str
    text: str
    media_url: str | None
    created_by_user_id: UserID

    created_at: datetime
    updated_at: datetime | None
    deleted_at: datetime | None
    is_deleted: bool

