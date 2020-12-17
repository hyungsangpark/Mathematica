from enum import Enum


class Skills(Enum):

    ADDITION = ("+", lambda a, b: a + b)
    SUBTRACTION = ("-", lambda a, b: a - b)
    MULTIPLICATION = ("*", lambda a, b: a * b)
    DIVISION = ("÷", lambda a, b: a / b)
