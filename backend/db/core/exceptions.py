class EmailAlreadyExistsError(Exception):
    """Email is already registered exception"""
    pass

class DatabaseConstraintError(Exception):
    pass

class UnexpectedError(Exception):
    pass