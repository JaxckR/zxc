from dataclasses import dataclass
from datetime import datetime

from edu.domain.user.entity import UserID


@dataclass(slots=True)
class UserDTO:
    id: UserID
    name: str
    username: str
    email: str
    profile_image_url: str

    created_at: datetime
    updated_at: datetime | None
    deleted_at: datetime | None
    is_superuser: bool
