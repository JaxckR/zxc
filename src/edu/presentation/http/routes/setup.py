import logging
from typing import Final

from fastapi import FastAPI, APIRouter

from .authentication import router as authentication_router
from .classwork import router as classwork_router
from .healthcheck import router as healthcheck_router
from .posts import router as posts_router
from .tier import router as tier_router
from .users import router as user_router

logger = logging.getLogger(__name__)

ROUTES_LIST: Final[list[APIRouter]] = [
    posts_router,
    classwork_router,
    authentication_router,
    tier_router,
    user_router,
    healthcheck_router
]


def setup_routes(app: FastAPI) -> None:
    router = APIRouter(prefix="/v1")

    for route in ROUTES_LIST:
        router.include_router(route)

    app.include_router(router)

    logger.info("Routes setup complete")
