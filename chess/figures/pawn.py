from chess.enums import ChessmanSide, ChessmanType
from .chessman import Chessman
from ..exceptions.common import PromotionToKingException, PromotionOnBadLineException, InvalidStepException


class Pawn(Chessman):
    def __init__(self, chess_field, chessman_side: ChessmanSide = ChessmanSide.WHITE):
        super().__init__(chessman_type=ChessmanType.PAWN, chessman_side=chessman_side, chess_field=chess_field)

    def go_to_position(self, position, board):
        # validate step
        d_col: int = abs(int(self._chess_field.col) - int(position.col))
        if d_col > 2:
            raise InvalidStepException()
        if d_col == 2 and self._chess_field.col not in (2, 7):
            raise InvalidStepException()

        f = board.get_field(f"{self._chess_field.row}{self._chess_field.col+1}").is_busy()
        if d_col == 2 and f is not None:
            raise InvalidStepException()

        super().go_to_position(position)

    def promote(self, figure_type: ChessmanType):
        if figure_type == ChessmanType.KING:
            raise PromotionToKingException()
        if (self._chessman_side == ChessmanSide.WHITE and self._chess_field.col != 8) or \
                (self._chessman_side == ChessmanSide.BLACK and self._chess_field.col != 1):
            raise PromotionOnBadLineException()
