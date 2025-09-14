from starlette.requests import Request

from edu.application.common.ports.request_manager import RequestManager
from edu.bootstrap.config import JWTConfig
from edu.presentation.http.common.cookie_schema import CookieData


class CookieRequestManager(RequestManager):

    def __init__(
            self,
            request: Request,
            config: JWTConfig,
    ) -> None:
        self._request = request
        self._config = config

    def get_refresh_token(self) -> str | None:
        return self._request.cookies.get("refresh_token", None)

    def add_refresh_token(self, token: str) -> None:
        cookie = CookieData(
            value=token,
            max_age=60 * 60 * 24 * self._config.refresh_days_expires,
            samesite="lax",
            secure=True,
        )
        self._request.state.refresh_token = cookie

    def remove_refresh_token(self) -> None:
        self._request.state.delete_refresh_token = True
