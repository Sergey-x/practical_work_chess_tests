from enum import Enum


class ChessMoveTypes(str, Enum):
    EMPTY_STEP = "-"
    CAPTURE = "x"
    SHORT_CASTLING = "O-O"
    LONG_CASTLING = "O-O-O"
    SHAH = "+"
    DOUBLE_SHAH = "++"
    CHECKMATE = "#"
