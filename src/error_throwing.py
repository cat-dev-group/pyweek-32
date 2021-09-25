"""error_throwing.py is used for generating the errors the game loop uses for the errors the user has to shoot."""
from dataclasses import dataclass
from enum import Enum
from random import choice, randrange


def generate_error() -> "Error":
    """
    Returns an error to be passed back into the function as an argument."""
    choice_mapping = {
        ErrorType.PYTHON: (randrange(80, 100), choice((0.15, 0.17, 0.19, 0.2))),
        ErrorType.STDLIB: (randrange(101, 120), choice((0.2, 0.23, 0.27, 0.3))),
        ErrorType.EXTERNAL: (randrange(125, 150), choice((0.32, 0.35, 0.37, 0.4))),
    }

    type_of_error = choice((ErrorType.PYTHON, ErrorType.STDLIB, ErrorType.EXTERNAL))
    health = choice_mapping[type_of_error][0]
    scale = choice_mapping[type_of_error][-1]
    type_of_error = Error(type_of_error, health, scale)
    return type_of_error


class ErrorType(Enum):
    """
    This is an `Enum` subclass that defines the type of errors.

    This has three different 'types':
        - PYTHON, with a value of "python", represents the errors for plain Python code.
        - STDLIB, with a value of "stdlib", represents errors for Python's inbuilt libraries.
        - EXTERNAL, with a value of "extrenal", represents errors from external third-party libraries.
    """

    PYTHON = "python"
    STDLIB = "stdlib"
    EXTERNAL = "external"


@dataclass(repr=True)
class Error:
    """
    This is the class that stores the 'bugs' that the game will use for the user to shoot.

    The bugs are chosen randomly, and right now, are hardcoded to errors from plain Python code.
    """

    error_type: ErrorType
    health: int
    scale: float
