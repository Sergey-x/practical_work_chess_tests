from chess.enums import ChessmanSide, ChessmanType
from .chessman import Chessman, ChessField
from ..exceptions.exceptions import PromotionToKingException, PromotionOnBadLineException, InvalidStepException


class Pawn(Chessman):
    def __init__(self, chess_field: ChessField, chessman_side: ChessmanSide = ChessmanSide.WHITE):
        super().__init__(chessman_type=ChessmanType.PAWN, chessman_side=chessman_side, chess_field=chess_field)

    def go_to_position(self, position: ChessField, board=None) -> None:
        d_row: int = abs(self._chess_field.row - position.row)
        d_col: int = abs(ord(self._chess_field.col) - ord(position.col))

        is_step_captured: bool = (d_row == 1) and (d_col == 1)
        is_step_empty: bool = (d_row == 1) and (d_col == 0)
        is_double_step_empty: bool = (d_row == 2) and (d_col == 0)

        # фигура перед пешкой
        next_field: ChessField = position

        if is_double_step_empty:
            if position.row - self._chess_field.row < 0:
                next_field = board.get_field(f"{self._chess_field.col}{self._chess_field.row - 1}")
            else:
                next_field = board.get_field(f"{self._chess_field.col}{self._chess_field.row + 1}")

        is_next_pos_free: bool = not bool(next_field.is_busy())

        # некорректный ход пешкой
        if not (is_step_empty or is_double_step_empty or is_step_captured):
            raise InvalidStepException()

        if is_double_step_empty:
            # ход пешкой на две клетки не со стартовой позиции
            if self._chess_field.row not in (2, 7):
                raise InvalidStepException()
            # ход пешкой на две клетки, если клетка впереди занята
            if not is_next_pos_free:
                raise InvalidStepException()

        if not is_next_pos_free and (is_step_empty or is_double_step_empty):
            raise InvalidStepException()

        super().go_to_position(position, board=board)

    def promote(self, chessman_type: ChessmanType):
        """Превращение пешки в фигуру."""
        # в короля превращаться нельзя
        if chessman_type == ChessmanType.KING:
            raise PromotionToKingException()

        # превращаться нельзя не на последних линиях
        if self.chess_field.row not in (1, 8):
            raise PromotionOnBadLineException()

        self._chessman_type = chessman_type

    def passent(self, target_pos: ChessField):
        """Взятие на проходе."""
        pass
