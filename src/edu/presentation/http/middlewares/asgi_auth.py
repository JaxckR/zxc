from http.cookies import SimpleCookie
from typing import Literal

from fastapi import FastAPI
from starlette.datastructures import MutableHeaders
from starlette.requests import Request
from starlette.types import Message, Receive, Scope, Send

from edu.presentation.http.common.cookie_schema import CookieData


class ASGIAuthMiddleware:
    def __init__(self, app: FastAPI):
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return

        request: Request = Request(scope)

        async def modify_cookies(message: Message) -> None:
            if message["type"] != "http.response.start":
                await send(message)
                return

            headers: MutableHeaders = MutableHeaders(scope=message)

            self._set_refresh_cookie(request, headers)
            self._delete_refresh_cookie(request, headers)

            await send(message)

        await self.app(scope, receive, modify_cookies)

    def _set_refresh_cookie(
            self,
            request: Request,
            headers: MutableHeaders,
    ) -> None:
        cookie_data: CookieData[str] | None = getattr(request.state, "refresh_token", None)

        if cookie_data is None or cookie_data.value is None:
            return

        max_age: int = cookie_data.max_age

        is_cookie_secure: bool = cookie_data.secure
        cookie_samesite: Literal["strict", "lax"] | None = cookie_data.samesite

        cookie = SimpleCookie()

        cookie["refresh_token"] = cookie_data.value
        cookie["refresh_token"]["path"] = "/"
        cookie["refresh_token"]["httponly"] = True
        cookie["refresh_token"]["max-age"] = max_age

        if is_cookie_secure:
            cookie["refresh_token"]["secure"] = True

        if cookie_samesite is not None:
            cookie["refresh_token"]["samesite"] = cookie_samesite

        headers.append("Set-Cookie", cookie.output(header="").strip())

    def _delete_refresh_cookie(self, request: Request, headers: MutableHeaders) -> None:
        is_delete_id: bool = getattr(request.state, "delete_refresh_token", False)
        if not is_delete_id:
            return

        cookie: SimpleCookie = SimpleCookie()

        cookie["refresh_token"] = ""
        cookie["refresh_token"]["path"] = "/"
        cookie["refresh_token"]["httponly"] = True
        cookie["refresh_token"]["max-age"] = 0

        headers.append("Set-Cookie", cookie.output(header="").strip())
