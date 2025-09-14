import sqlalchemy as sa
from sqlalchemy.orm import relationship

from edu.domain.tier.entity import Tier
from edu.infrastructure.persistence.models.base import mapper_registry

tiers_table = sa.Table(
    "tiers",
    mapper_registry.metadata,
    sa.Column("id", sa.BigInteger, primary_key=True, autoincrement=True),
    sa.Column("name", sa.String, nullable=False, unique=True),

    sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
    sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
)


def map_tiers_table() -> None:
    mapper_registry.map_imperatively(
        Tier,
        tiers_table,
        properties={
            "oid": tiers_table.c.id,
            "name": tiers_table.c.name,

            "created_at": tiers_table.c.created_at,
            "updated_at": tiers_table.c.updated_at,

            "users": relationship(
                "User",
                back_populates="tier",
            )
        },
        column_prefix="_",
    )
