from edu.application.common.dto import UserDTO
from edu.application.common.pagination import Pagination
from edu.application.common.ports.repositories.user import IUserRepository


class GetAllUsers:

    def __init__(
            self,
            user_repository: IUserRepository,
    ):
        self._user_repository = user_repository

    async def __call__(self, pagination: Pagination) -> list[UserDTO] | list[None]:
        raw_result = await self._user_repository.get_all(pagination)

        result = []
        for user in raw_result:
            result.append(
                UserDTO(
                    id=user.oid,
                    name=user.name.name,
                    username=user.username.username,
                    email=user.email.email,
                    profile_image_url=user.profile_image_url,

                    created_at=user.created_at,
                    updated_at=user.updated_at,
                    deleted_at=user.deleted_at,
                    is_superuser=user.is_superuser,
                )
            )

        return result
