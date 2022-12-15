from enum import Enum


class ChessMoveTypes(str, Enum):
    EMPTY_STEP = "-"
    CAPTURE = "x"
    SHAH = "+"
    DOUBLE_SHAH = "++"
