class InvalidInputException(Exception):
    def __init__(self, message="Invalid input"):
        self.message = message
        super().__init__(self.message)


class InvalidTypeException(Exception):
    def __init__(self, message="Invalid type"):
        self.message = message
        super().__init__(self.message)


class EmptyInputException(Exception):
    def __init__(self, message="Empty input"):
        self.message = message
        super().__init__(self.message)


class InvalidDateException(Exception):
    def __init__(self, message="Invalid date"):
        self.message = message
        super().__init__(self.message)


class InvalidRangeException(Exception):
    def __init__(self, message="Invalid range"):
        self.message = message
        super().__init__(self.message)
