import time
from dataclasses import dataclass
from functools import cached_property
from os import getenv
from pathlib import Path
from typing import Literal

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parents[2]


@dataclass(slots=True, frozen=True)
class PostgresConfig:
    user: str = getenv("POSTGRES_USER")
    password: str = getenv("POSTGRES_PASSWORD")
    host: str = getenv("POSTGRES_HOST")
    port: int = int(getenv("POSTGRES_PORT"))
    database: str = getenv("POSTGRES_DB")

    @property
    def url(self) -> str:
        return f"postgresql+psycopg://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"


@dataclass(frozen=True)
class RedisConfig:
    host: str = getenv("REDIS_HOST")
    port: int = int(getenv("REDIS_PORT"))
    db: int = int(getenv("REDIS_DB"))

    @property
    def url(self) -> str:
        return f"redis://{self.host}:{self.port}/{self.db}"


@dataclass(frozen=True)
class JWTConfig:
    algorithm: Literal[
        "HS256",
        "HS384",
        "HS512",
        "RS256",
        "RS384",
        "RS512",
    ] = getenv("JWT_ALGORITHM")
    access_minutes_expires: int = int(getenv("JWT_ACCESS_MINUTES_EXPIRES"))
    refresh_days_expires: int = int(getenv("JWT_REFRESH_DAYS_EXPIRES"))

    @cached_property
    def secret_key(self) -> str:
        key_path = BASE_DIR.parent / "jwt_certs" / "private.pem"
        with open(key_path, "r") as f:
            return f.read()

    @cached_property
    def public_key(self) -> str:
        key_path = BASE_DIR.parent / "jwt_certs" / "public.pem"
        with open(key_path, "r") as f:
            return f.read()


@dataclass(frozen=True)
class Config:
    db: PostgresConfig
    redis: RedisConfig
    jwt: JWTConfig


config = Config(
    db=PostgresConfig(),
    redis=RedisConfig(),
    jwt=JWTConfig(),
)
