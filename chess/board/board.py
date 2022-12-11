from chess.exceptions.errors import GoOutOfBoardError
from chess.figures import Chessman


class ChessField:
    def __init__(self, pos: str):
        self._pos = pos
        self._figure: Chessman | None = None

    @property
    def row(self) -> str:
        return self._pos[0]

    @property
    def col(self) -> int:
        return int(self._pos[1])

    def set_figure(self, figure: Chessman) -> None:
        self._figure = figure

    def drop_figure(self) -> None:
        self._figure = None

    def is_busy(self) -> Chessman | None:
        return self._figure

    def __repr__(self) -> str:
        return self._pos

    def __str__(self) -> str:
        return self.__repr__()


class Board:
    _BOARD_SIZE_NUMBER = 8

    def __init__(self):
        self._board = {}

        for a in range(ord('a'), ord('h')):
            for n in range(self._BOARD_SIZE_NUMBER):
                pos = f"{chr(a)}{n + 1}"
                self._board[pos] = ChessField(pos=pos)

    def get_field(self, field: str) -> ChessField:
        n = int(field[1])
        if n > self._BOARD_SIZE_NUMBER:
            raise GoOutOfBoardError()
        return self._board[field]
