from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from edu.presentation.http.middlewares.asgi_auth import ASGIAuthMiddleware


def setup_middlewares(app: FastAPI) -> None:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"]
    )
    app.add_middleware(ASGIAuthMiddleware)
