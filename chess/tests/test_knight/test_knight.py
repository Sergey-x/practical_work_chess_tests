import pytest

from chess.board import Board, ChessField
from chess.enums import ChessmanSide
from chess.exceptions.common import GoOverOwnFigureException
from chess.exceptions.errors import GoOutOfBoardError
from chess.figures import Knight


class TestKnight:
    """Тестирование возможных ходов шахматной фигуры коня."""

    def test_step_to_busy_position(self, board: Board):
        """Попытка хода на позицию, занятую фигурой своего цвета."""
        e4: ChessField = board.get_field("e4")

        # ставим фигуру на e4
        _ = Knight(chess_field=e4)

        # ставим коня на c3
        knight = Knight(chess_field=board.get_field("c3"))

        # ходим конем на e4
        with pytest.raises(GoOverOwnFigureException):
            knight.go_to_position(e4)

    def test_step_out_of_board(self, board: Board):
        """Попытка хода за пределы шахматной доски."""
        # ставим коня на b7
        knight = Knight(chess_field=board.get_field("b7"))

        # попытка выхода за пределы доски на a9
        with pytest.raises(GoOutOfBoardError):
            knight.go_to_position(board.get_field("a9"))

    def test_step(self, board: Board):
        """Допустимый ход."""
        knight = Knight(chess_field=board.get_field("b1"))
        knight.go_to_position(board.get_field("a3"))
        assert True

    def test_capture(self, board: Board):
        """Взятие фигуры противника."""
        c3 = board.get_field("c3")
        b1 = board.get_field("b1")
        _black_knight = Knight(chessman_side=ChessmanSide.BLACK, chess_field=c3)
        white_knight = Knight(chessman_side=ChessmanSide.WHITE, chess_field=b1)
        white_knight.go_to_position(c3)
        assert True

    def test_king_capture(self, board: Board):
        """Взятие короля противника."""
        pass

    def test_step_with_exposing_king(self, board: Board):
        """Ход с открытием своего короля для шаха."""
        pass
