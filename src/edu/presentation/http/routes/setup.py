import logging
from typing import Final

from fastapi import FastAPI, APIRouter

from .authentication import router as authentication_router
from .healthcheck import router as healthcheck_router
from .users import router as user_router

logger = logging.getLogger(__name__)

ROUTES_LIST: Final[list[APIRouter]] = [
    authentication_router,
    user_router,
]


def setup_routes(app: FastAPI) -> None:
    router = APIRouter(prefix="/v1")

    for route in ROUTES_LIST:
        router.include_router(route)

    app.include_router(healthcheck_router)
    app.include_router(router)

    logger.info("Routes setup complete")
