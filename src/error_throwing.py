"""error_throwing.py is used for generating the errors the game loop uses for the errors the user has to shoot."""
from dataclasses import dataclass
from enum import Enum
from random import randrange
from types import FunctionType, GeneratorType
from typing import Any


class ErrorThrower:
    """The class that generates 'errors' for the game to use with having the user shoot the bugs."""

    def __init__(self) -> None:
        """This function is defining instance attributes and does not have any arguments."""
        self.errors = (
            "AssertionError",
            "AttributeError",
            "EOFError",
            "FloatingPointError",
            "GeneratorExit",
            "ImportError",
            "IndexError",
            "KeyError",
            "KeyboardInterrupt",
            "MemoryError",
            "NameError",
            "NotImplementedError",
            "OSError",
            "OverflowError",
            "ReferenceError",
            "RuntimeError",
            "StopIteration",
            "SyntaxError",
            "IndentationError",
            "TabError",
            "SystemError",
            "SystemExit",
            "TypeError",
            "UnboundLocalError",
            "UnicodeError",
            "UnicodeEncodeError",
            "UnicodeDecodeError",
            "UnicodeTranslateError",
            "ValueError",
            "ZeroDivisionError",
        )

    def throw_errors(self, count: int = 1, name: str = "") -> FunctionType:
        """Returns the new function with the errors passed in."""

        def decorator(function: FunctionType) -> FunctionType:
            """
            Returns the wrapper and itself.

            Implements the brute of the decorator and does the 'lifting work' for this decorator.
            """

            def wrapper(*args: Any, **kwargs: Any) -> FunctionType:
                """Returns the new function with the 'errors' passed into the function."""
                errors = self._generate_errors(count)
                if name:
                    return function(*args, **{name: errors}, **kwargs)
                else:
                    return function(*args, errors, **kwargs)

            return wrapper

        return decorator

    def _generate_errors(self, count: int = 1) -> GeneratorType:
        """
        Returns errors to be passed back into the function as an argument.

        Pulls random errors from `self.errors` and puts into the Error class, for easy access to important attributes.
        """
        errors = (self.errors[randrange(0, len(self.errors))] for _ in range(count))
        # Hard coded to PYTHON for now
        errors = (Error(ErrorType.PYTHON, error_name, 100) for error_name in errors)
        return errors


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
    name: str
    health: float
