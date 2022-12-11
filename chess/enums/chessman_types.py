from enum import Enum


class ChessmanType(str, Enum):
    PAWN = "PAWN"
    KNIGHT = "KNIGHT"
    KING = "KING"
    QUEEN = "QUEEN"
    ROOK = "ROOK"
    BISHOP = "BISHOP"
