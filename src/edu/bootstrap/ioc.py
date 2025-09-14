from typing import AsyncIterator

from dishka import Provider, Scope, from_context, provide, AnyOf, provide_all
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine, async_sessionmaker, AsyncSession
from starlette.requests import Request

from edu.application.commands.authentication.login import LoginCommand
from edu.application.commands.user.create_user import CreateUserCommand
from edu.application.common.ports.id_generator import IDGenerator
from edu.application.common.ports.jwt_processor import JWTProcessor
from edu.application.common.ports.repositories.user import IUserRepository
from edu.application.common.ports.request_manager import RequestManager
from edu.application.common.ports.uow import UoW
from edu.application.queries.user.get_all_users import GetAllUsers
from edu.application.queries.user.get_user_by_username import GetUserByUsername
from edu.bootstrap.config import JWTConfig, PostgresConfig
from edu.domain.common.ports.password_hasher import PasswordHasherProtocol
from edu.domain.user.service import UserService
from edu.infrastructure.adapters.id_generator import IDGeneratorImpl
from edu.infrastructure.adapters.jwt_processor import PyJWTProcessor
from edu.infrastructure.adapters.password_hasher import PasswordHasher
from edu.infrastructure.persistence.repositories.user import UserRepository
from edu.presentation.http.adapters.request_manager import CookieRequestManager


class ConfigProvider(Provider):
    scope = Scope.APP

    jwt_config = from_context(JWTConfig)
    postgres_config = from_context(PostgresConfig)


class DomainProvider(Provider):
    scope = Scope.REQUEST

    services = provide_all(
        UserService,
    )


class ApplicationProvider(Provider):
    scope = Scope.REQUEST

    user = provide_all(
        GetAllUsers,
        GetUserByUsername,
        CreateUserCommand
    )

    authentication = provide_all(
        LoginCommand,
    )


class InfrastructureProvider(Provider):
    scope = Scope.REQUEST

    password_hasher = provide(
        PasswordHasher,
        provides=PasswordHasherProtocol,
        scope=Scope.APP,
    )

    jwt_processor = provide(
        PyJWTProcessor,
        provides=JWTProcessor,
        scope=Scope.APP,
    )

    user_repository = provide(
        UserRepository,
        provides=IUserRepository,
    )

    id_generator = provide(
        IDGeneratorImpl,
        provides=IDGenerator
    )


class PresentationProvider(Provider):
    scope = Scope.REQUEST

    request = from_context(Request)

    request_manager = provide(
        CookieRequestManager,
        provides=RequestManager,
    )


class DBProvider(Provider):
    scope = Scope.REQUEST

    @provide(scope=Scope.APP)
    async def get_engine(self, config: PostgresConfig) -> AsyncIterator[AsyncEngine]:
        engine = create_async_engine(
            config.url,
            pool_size=15,
            max_overflow=15,
        )
        yield engine
        await engine.dispose()

    @provide(scope=Scope.APP)
    async def get_sessionmaker(
            self, engine: AsyncEngine
    ) -> async_sessionmaker[AsyncSession]:
        return async_sessionmaker(
            bind=engine,
            autocommit=False,
            autoflush=False,
            expire_on_commit=False,
        )

    @provide(scope=Scope.REQUEST)
    async def get_session(
            self,
            async_factory: async_sessionmaker[AsyncSession],
    ) -> AsyncIterator[AnyOf[UoW, AsyncSession]]:
        async with async_factory() as session:
            yield session


def get_providers() -> list[Provider]:
    return [
        ConfigProvider(),
        DomainProvider(),
        ApplicationProvider(),
        InfrastructureProvider(),
        PresentationProvider(),
        DBProvider(),
    ]
