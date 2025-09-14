from sqlalchemy import select, and_

from edu.application.common.pagination import Pagination
from edu.application.common.ports.repositories.user import IUserRepository
from edu.domain.user.entity import User
from edu.domain.user.value_objects import Username
from edu.infrastructure.persistence.repositories.base import SQLAlchemyBase


class UserRepository(SQLAlchemyBase, IUserRepository):

    async def get_all(self, pagination: Pagination) -> list[User] | list[None]:
        stmt = select(User).order_by(User.oid)

        if pagination.limit:
            stmt = stmt.limit(pagination.limit)
        if pagination.offset:
            stmt = stmt.offset(pagination.offset)

        result = await self._session.execute(stmt)
        return result.scalars().all()

    async def get_by_username(self, username: Username) -> User | None:
        result = await self._session.execute(
            select(User)
            .where(and_(User.username == username))
        )
        return result.scalar_one_or_none()

    async def add(self, user: User) -> None:
        self._session.add(user)
