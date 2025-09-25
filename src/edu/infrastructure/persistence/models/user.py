import sqlalchemy as sa
from sqlalchemy.orm import composite

from edu.domain.user import value_objects as vo
from edu.domain.user.entity import User
from edu.infrastructure.persistence.models.base import mapper_registry

users_table = sa.Table(
    "users",
    mapper_registry.metadata,
    sa.Column("id", sa.UUID, primary_key=True, nullable=False, unique=True),
    sa.Column("name", sa.String(30), nullable=False),
    sa.Column("username", sa.String(20), unique=True, nullable=False),
    sa.Column("email", sa.String(255), unique=True, nullable=False),
    sa.Column("hashed_password", sa.LargeBinary, nullable=False),
    sa.Column("profile_image_url", sa.String, nullable=False, default="profile/default.jpg/"),

    sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
    sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
    sa.Column("deleted_at", sa.DateTime(timezone=True), nullable=True),
    sa.Column("is_superuser", sa.Boolean, nullable=False, default=False),
)


def map_users_table() -> None:
    mapper_registry.map_imperatively(
        User,
        users_table,
        properties={
            "oid": users_table.c.id,
            "name": composite(vo.Name, users_table.c.name),
            "username": composite(vo.Username, users_table.c.username),
            "email": composite(vo.Email, users_table.c.email),
            "hashed_password": users_table.c.hashed_password,
            "profile_image_url": users_table.c.profile_image_url,

            "created_at": users_table.c.created_at,
            "updated_at": users_table.c.updated_at,
            "deleted_at": users_table.c.deleted_at,
            "is_superuser": users_table.c.is_superuser,
        },
        column_prefix="_"
    )
