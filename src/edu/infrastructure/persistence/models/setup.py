import logging

from edu.infrastructure.persistence.models.tier import map_tiers_table
from edu.infrastructure.persistence.models.user import map_users_table

logger = logging.getLogger(__name__)


def map_tables() -> None:
    map_users_table()
    map_tiers_table()

    logger.info("Tables mapping complete")
