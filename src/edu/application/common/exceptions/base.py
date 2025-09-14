class ApplicationError(Exception):

    @property
    def message(self) -> str:
        return "Application error is occurred"

    def __str__(self) -> str:
        return self.message
