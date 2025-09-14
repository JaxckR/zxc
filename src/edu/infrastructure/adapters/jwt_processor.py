from datetime import datetime, timezone, timedelta
from typing import Literal

import jwt

from edu.application.common.ports.jwt_processor import JWTProcessor, JWTPayload
from edu.bootstrap.config import JWTConfig


class PyJWTProcessor(JWTProcessor):

    def __init__(self, config: JWTConfig) -> None:
        self._config = config

    def encode(
            self,
            raw_payload: JWTPayload,
            token_type: Literal["access", "refresh"]
    ) -> str:
        now = datetime.now(timezone.utc)
        if token_type == "access":
            expires = now + timedelta(minutes=self._config.access_minutes_expires)
        else:
            expires = now + timedelta(days=self._config.refresh_days_expires)

        payload = {
            "sub": str(raw_payload.oid),
            "iat": now,
            "exp": expires,
        }
        result = jwt.encode(
            payload=payload,
            key=self._config.secret_key,
            algorithm=self._config.algorithm,
        )
        return result

    def decode(self, token: str | bytes) -> dict:
        result = jwt.decode(
            token,
            key=self._config.secret_key,
            algorithms=[self._config.algorithm],
        )
        return result
