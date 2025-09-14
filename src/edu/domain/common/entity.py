from dataclasses import dataclass
from typing import Generic, TypeVar

OID = TypeVar('OID')


@dataclass
class OIDEntity(Generic[OID]):
    oid: OID
