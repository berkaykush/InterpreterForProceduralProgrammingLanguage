class Error(Exception):
    def __init__(self, error_message=None):
        self.__message = f"{self.__class__.__name__}: {error_message}"

    @property
    def message(self):
        return self.__message


class LexerError(Error):
    pass
