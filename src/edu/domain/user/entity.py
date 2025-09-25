from dataclasses import dataclass
from datetime import datetime
from typing import NewType
from uuid import UUID

from edu.domain.common.entity import OIDEntity
from edu.domain.user import value_objects as vo

UserID = NewType('UserID', UUID)


@dataclass
class User(OIDEntity[UserID]):
    name: vo.Name
    username: vo.Username
    email: vo.Email
    hashed_password: bytes
    profile_image_url: str

    created_at: datetime
    updated_at: datetime | None
    deleted_at: datetime | None
    is_superuser: bool
