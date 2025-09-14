import asyncio
import sys
from contextlib import asynccontextmanager
from typing import AsyncIterator

import uvicorn
from dishka import make_async_container
from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from edu.bootstrap.config import config, JWTConfig, PostgresConfig
from edu.bootstrap.ioc import get_providers
from edu.bootstrap.logging import setup_logging
from edu.infrastructure.persistence.models.setup import map_tables
from edu.presentation.http.common.exception_handler import setup_exceptions
from edu.presentation.http.middlewares.setup import setup_middlewares
from edu.presentation.http.routes.setup import setup_routes


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    yield


def get_app() -> FastAPI:
    app = FastAPI(
        title="P2P edu",
        description="P2P education backend implementation",
        version="1.0.0",
        default_response_class=ORJSONResponse,
        lifespan=lifespan,
        root_path="/api"
    )
    setup_logging()

    container = make_async_container(
        *get_providers(),
        context={
            JWTConfig: config.jwt,
            PostgresConfig: config.db,
        }
    )
    setup_dishka(container, app)

    map_tables()

    setup_middlewares(app)
    setup_exceptions(app)
    setup_routes(app)

    return app


if __name__ == "__main__":
    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    uvicorn.run(
        "main:get_app",
        host="0.0.0.0",
        port=8000,
        factory=True
    )
