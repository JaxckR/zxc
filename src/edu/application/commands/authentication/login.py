from dataclasses import dataclass

from edu.application.common.exceptions.authentication import AuthenticationError
from edu.application.common.exceptions.user import UserNotFoundError
from edu.application.common.ports.jwt_processor import JWTProcessor, JWTPayload
from edu.application.common.ports.repositories.user import IUserRepository
from edu.application.common.ports.request_manager import RequestManager
from edu.domain.common.ports.password_hasher import PasswordHasherProtocol
from edu.domain.user.entity import User
from edu.domain.user.value_objects import Username


@dataclass(slots=True)
class LoginRequest:
    username: str
    password: str


@dataclass(slots=True)
class LoginResponse:
    access_token: str


class LoginCommand:

    def __init__(
            self,
            user_repository: IUserRepository,
            jwt_processor: JWTProcessor,
            password_hasher: PasswordHasherProtocol,
            request_manager: RequestManager,
    ) -> None:
        self._user_repository = user_repository
        self._jwt_processor = jwt_processor
        self._password_hasher = password_hasher
        self._request_manager = request_manager

    async def __call__(self, data: LoginRequest) -> LoginResponse:
        user: User = await self._user_repository.get_by_username(Username(data.username))

        if not user:
            raise UserNotFoundError

        verify: bool = self._password_hasher.verify(data.password, user.hashed_password)

        if not verify:
            raise AuthenticationError

        payload = JWTPayload(oid=user.oid)

        refresh_token = self._jwt_processor.encode(
            payload,
            token_type="refresh",
        )
        self._request_manager.add_refresh_token(refresh_token)

        access_token = self._jwt_processor.encode(
            payload,
            token_type="access",
        )

        return LoginResponse(access_token=access_token)
