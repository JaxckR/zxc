from typing import override

from edu.application.common.exceptions.base import ApplicationError


class AuthenticationError(ApplicationError):

    @override
    @property
    def message(self) -> str:
        return "Invalid username or password"
