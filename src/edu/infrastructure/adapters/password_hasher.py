import bcrypt

from edu.domain.common.ports.password_hasher import PasswordHasherProtocol


class PasswordHasher(PasswordHasherProtocol):

    def hash(self, password: str) -> bytes:
        salt = bcrypt.gensalt()
        encoded_password = password.encode()
        return bcrypt.hashpw(encoded_password, salt)

    def verify(self, password: str, hashed_password: bytes) -> bool:
        return bcrypt.checkpw(password.encode(), hashed_password)
