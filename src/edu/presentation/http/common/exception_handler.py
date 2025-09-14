import logging
from functools import partial
from typing import Final

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from starlette import status
from starlette.requests import Request

from edu.application.common.exceptions.authentication import AuthenticationError
from edu.application.common.exceptions.user import UserNotFoundError
from edu.presentation.http.common.schemas import ErrorResponse

logger = logging.getLogger(__name__)

EXCEPTIONS: Final[dict] = {
    UserNotFoundError: status.HTTP_404_NOT_FOUND,

    AuthenticationError: status.HTTP_401_UNAUTHORIZED,
}


async def validate(_: Request, exception: Exception, code: int) -> ORJSONResponse:
    return ORJSONResponse(
        status_code=code, content=ErrorResponse(detail=str(exception)).model_dump()
    )


async def internal_error(_: Request, exception: Exception) -> ORJSONResponse:
    logger.exception("ERROR", exc_info=exception)
    return ORJSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content=ErrorResponse(detail="Internal server error").model_dump(),
    )


def setup_exceptions(app: FastAPI) -> None:
    for exc, code in EXCEPTIONS.items():
        app.add_exception_handler(exc, partial(validate, code=code))

    app.add_exception_handler(Exception, internal_error)

    logger.info("Exception handlers setup")
