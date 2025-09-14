class DomainError(Exception):

    @property
    def message(self) -> str:
        return "Domain error occurred"

    def __str__(self) -> str:
        return self.message
