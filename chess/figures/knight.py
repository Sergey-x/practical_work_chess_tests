from chess.enums import ChessmanSide, ChessmanType
from .chessman import Chessman


class Knight(Chessman):
    def __init__(self, chess_field, chessman_side: ChessmanSide = None):
        super().__init__(chessman_type=ChessmanType.KNIGHT, chessman_side=chessman_side, chess_field=chess_field)

    def go_to_position(self, position, board=None):
        # validate step
        super().go_to_position(position, board)
