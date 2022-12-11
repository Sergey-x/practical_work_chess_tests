from chess.board import ChessField
from chess.figures import Chessman
from chess.enums import ChessMoveTypes, ChessMoveNotation


class ChessMove:
    """Класс хода фигуры."""

    def __init__(
            self,
            move_types: ChessMoveTypes,
            figure: Chessman,
            start: ChessField,
            end: ChessField,
            move_number: int,
    ):
        self._move_number = move_number
        self._move_types = move_types
        self._figure = figure
        self._start = start
        self._end = end

    def __repr__(self) -> str:
        if self._move_types in (ChessMoveTypes.EMPTY_STEP, ChessMoveTypes.CAPTURE):
            return "".join((
                str(self._move_number),
                ". ",
                ChessMoveNotation[str(self._figure)],
                str(self._start),
                str(self._move_types),
                str(self._end),
            ))
        return str(self._move_number) + ". " + str(self._move_types)

    def __str__(self) -> str:
        return self.__repr__()
