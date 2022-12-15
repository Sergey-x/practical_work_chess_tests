from chess.enums import ChessMoveTypes, ChessMoveNotation, ChessmanType


class ChessMove:
    """Класс хода фигуры."""

    def __init__(
            self,
            move_type: ChessMoveTypes,
            figure,
            start,
            end,
    ):
        self._move_type = move_type
        self._figure: ChessmanType = figure
        self._start = start
        self._end = end

    @property
    def figure(self):
        return self._figure

    @property
    def start(self):
        return self._start

    @property
    def end(self):
        return self._end

    def __repr__(self) -> str:
        if self._move_type in (ChessMoveTypes.EMPTY_STEP, ChessMoveTypes.CAPTURE):
            return "".join((
                ChessMoveNotation[str(self._figure.value)],
                str(self._start),
                str(self._move_type.value),
                str(self._end),
            ))
        return str(self._move_type.value)

    def __str__(self) -> str:
        return self.__repr__()
