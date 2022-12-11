from enum import Enum


class ChessMoveNotation(str, Enum):
    PAWN = ""
    KNIGHT = "N"
    KING = "K"
    QUEEN = "Q"
    ROOK = "R"
    BISHOP = "B"
