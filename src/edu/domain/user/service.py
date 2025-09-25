from typing import cast

from edu.domain.common.ports.password_hasher import PasswordHasherProtocol
from edu.domain.tier.entity import TierID
from edu.domain.user import value_objects as vo
from edu.domain.user.entity import User, UserID


class UserService:
    def __init__(
            self,
            password_hasher: PasswordHasherProtocol
    ) -> None:
        self._password_hasher = password_hasher

    def create(
            self,
            oid: UserID,
            name: str,
            username: str,
            email: str,
            password: str,
            tier_id: TierID,
            profile_image_url: str = "profile/default.jpg/",
            is_deleted: bool = False,
            is_superuser: bool = False,
    ) -> User:
        hashed_password = self._password_hasher.hash(password)

        return User(
            oid=oid,
            name=vo.Name(name),
            username=vo.Username(username),
            email=vo.Email(email),
            hashed_password=hashed_password,
            profile_image_url=profile_image_url,

            is_deleted=is_deleted,
            is_superuser=is_superuser,
            created_at=cast("datetime", cast("object", None)),
            updated_at=None,
            deleted_at=None,
            tier_id=tier_id,
        )
