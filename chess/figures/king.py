from chess.enums import ChessmanSide, ChessmanType
from .chessman import Chessman, ChessField


class King(Chessman):
    def __init__(self, chess_field: ChessField, chessman_side: ChessmanSide = None):
        super().__init__(chessman_type=ChessmanType.KING, chessman_side=chessman_side, chess_field=chess_field)

    def go_to_position(self, position: ChessField, board):
        pass
