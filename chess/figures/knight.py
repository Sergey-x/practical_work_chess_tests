from chess.enums import ChessmanSide, ChessmanType
from .chessman import Chessman, ChessField
from ..exceptions.exceptions import InvalidStepException


class Knight(Chessman):
    def __init__(self, chess_field: ChessField, chessman_side: ChessmanSide = None):
        super().__init__(chessman_type=ChessmanType.KNIGHT, chessman_side=chessman_side, chess_field=chess_field)

    def go_to_position(self, position: ChessField, board):
        d_col: int = abs(ord(self.chess_field.col) - ord(position.col))
        d_row: int = abs(self.chess_field.row - position.row)

        # Проверка, что ход коня верный
        if not ((d_col == 1 and d_row == 2) or (d_col == 2 and d_row == 1)):
            raise InvalidStepException()

        super().go_to_position(position, board=board)
