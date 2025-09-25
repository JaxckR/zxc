from edu.application.common.dto import UserDTO
from edu.application.common.exceptions.user import UserNotFoundError
from edu.application.common.ports.repositories.user import IUserRepository
from edu.domain.user.value_objects import Username


class GetUserByUsername:

    def __init__(
            self,
            user_repository: IUserRepository,
    ):
        self._user_repository = user_repository

    async def __call__(self, username: Username) -> UserDTO:
        r = await self._user_repository.get_by_username(username)

        if r is None:
            raise UserNotFoundError

        result = UserDTO(
            id=r.oid,
            name=r.name.name,
            username=r.username.username,
            email=r.email.email,
            profile_image_url=r.profile_image_url,

            created_at=r.created_at,
            updated_at=r.updated_at,
            deleted_at=r.deleted_at,
            is_superuser=r.is_superuser,
        )
        return result
