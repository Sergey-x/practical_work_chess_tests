from chess.exceptions.errors import GoOutOfBoardError
from chess.figures.chessman import ChessField
from chess.moves import ChessMove


class Board:
    _BOARD_SIZE_NUMBER = 8
    SMBLS: str = "abcdefgh"

    def __init__(self):
        """Создание шахматной доски.

        В словарь добавляется 64 клетки.
        """
        self._board: dict[str, ChessField] = {}
        self._moves: list[ChessMove] = []

        for a in self.SMBLS:
            for n in range(self._BOARD_SIZE_NUMBER):
                pos = f"{a}{n + 1}"
                self._board[pos] = ChessField(pos=pos)

    @property
    def moves(self) -> list[ChessMove]:
        return self._moves

    def print_moves(self):
        print("======= Начало партии =======")
        for move in self._moves:
            print(move)
        print("======= Партия завершена =======")

    def add_move(self, move: ChessMove) -> None:
        self._moves.append(move)

    def get_field(self, field: str) -> ChessField:
        """Получение клетки по её нотации [a-h][1-8]."""
        if len(field) != 2:
            raise GoOutOfBoardError()

        n = int(field[1])
        if n > self._BOARD_SIZE_NUMBER or n < 1:
            raise GoOutOfBoardError()

        return self._board[field]
