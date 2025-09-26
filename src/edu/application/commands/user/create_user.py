from dataclasses import dataclass

from edu.application.common.ports.id_generator import IDGenerator
from edu.application.common.ports.repositories.user import IUserRepository
from edu.application.common.ports.uow import UoW
from edu.domain.user.entity import User
from edu.domain.user.service import UserService
from edu.domain.user import value_objects as vo


@dataclass(slots=True)
class CreateUserDTO:
    name: str
    username: str
    email: str
    password: str


class CreateUserCommand:

    def __init__(
            self,
            user_repository: IUserRepository,
            user_service: UserService,
            uow: UoW,
            id_generator: IDGenerator,
    ):
        self._user_repository = user_repository
        self._user_service = user_service
        self._uow = uow
        self._id_generator = id_generator

    async def __call__(self, data: CreateUserDTO) -> None:
        user: User = self._user_service.create(
            oid=self._id_generator.generate_user_id(),
            name=vo.Name(data.name),
            username=vo.Username(data.username),
            email=vo.Email(data.email),
            raw_password=vo.RawPassword(data.password),
        )
        await self._user_repository.add(user)
        await self._uow.commit()
