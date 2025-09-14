from uuid_extensions import uuid7

from edu.application.common.ports.id_generator import IDGenerator
from edu.domain.user.entity import UserID


class IDGeneratorImpl(IDGenerator):

    def generate_user_id(self) -> UserID:
        return UserID(uuid7())