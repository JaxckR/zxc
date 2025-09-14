from typing import override

from edu.application.common.exceptions.base import ApplicationError


class UserNotFoundError(ApplicationError):

    @override
    @property
    def message(self) -> str:
        return "User not found"
