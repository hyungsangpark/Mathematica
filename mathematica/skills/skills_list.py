from enum import Enum


class Skills(Enum):
    """
    An enum of skills available in Mathematica.

    Four skills are available: Addition, Subtraction, Multiplication, Division

    Each enum value holds a dictionary with two string keys: ``"operator"`` and ``"function"``.

    Use ``"operator"`` to receive a string operator of the respective skill (eg. + for addition)
    and use ``"function"`` to receive a lambda function of the respective skill.
    (eg. ``lambda a, b: a + b`` for addition)
    """

    ADDITION = {"operator": "+", "function": lambda a, b: a + b}
    SUBTRACTION = {"operator": "-", "function": lambda a, b: a - b}
    MULTIPLICATION = {"operator": "×", "function": lambda a, b: a * b}
    DIVISION = {"operator": "÷", "function": lambda a, b: a / b}
