import pytest

from chess.board.board import Board
from chess.enums.chessman_side import ChessmanSide
from chess.enums.chessman_types import ChessmanType
from chess.exceptions.errors import KingCaptureError
from chess.exceptions.exceptions import PromotionToKingException, InvalidStepException, PromotionOnBadLineException
from chess.figures.king import King
from chess.figures.knight import Knight
from chess.figures.pawn import Pawn


class TestPawn:

    def test_one_step(self, board: Board):
        """Первый ход пешки на одну позицию вперед."""
        e2 = board.get_field("e2")
        e3 = board.get_field("e3")
        pawn = Pawn(chess_field=e2)
        pawn.go_to_position(e3, board=board)
        assert True

    def test_two_steps(self, board: Board):
        """Первый ход пешки на две позиции вперед."""
        e2 = board.get_field("e2")
        e4 = board.get_field("e4")
        pawn = Pawn(chess_field=e2)
        pawn.go_to_position(e4, board=board)
        assert True

    def test_two_steps_from_non_start_pos(self, board: Board):
        """Ход пешки на две позиции вперед не с начальной позиции."""
        e4 = board.get_field("e4")
        e6 = board.get_field("e6")
        pawn = Pawn(chess_field=e4)
        with pytest.raises(InvalidStepException):
            pawn.go_to_position(e6, board=board)

    def test_two_steps_in_blocked(self, board: Board):
        """Ход пешки на две позиции вперед с фигурой впереди."""
        e2 = board.get_field("e2")
        e3 = board.get_field("e3")
        e4 = board.get_field("e4")
        white_pawn = Pawn(chess_field=e2)
        _black_pawn = Pawn(chessman_side=ChessmanSide.BLACK, chess_field=e3)
        with pytest.raises(InvalidStepException):
            white_pawn.go_to_position(e4, board=board)

    def test_promotion(self, board: Board):
        """Превращение пешки."""
        white_pawn: Pawn = Pawn(chess_field=board.get_field("e8"))
        white_pawn.promote(ChessmanType.KNIGHT)
        assert True

    def test_king_promotion(self, board: Board):
        """Превращение пешки в короля."""
        white_pawn: Pawn = Pawn(chess_field=board.get_field("e8"))
        with pytest.raises(PromotionToKingException):
            white_pawn.promote(ChessmanType.KING)

    def test_promotion_on_bad_line(self, board: Board):
        """Превращение пешки не на последней линии."""
        white_pawn: Pawn = Pawn(chess_field=board.get_field("e6"))
        with pytest.raises(PromotionOnBadLineException):
            white_pawn.promote(ChessmanType.PAWN)

    def test_passent(self, board: Board):
        """Взятие на проходе."""

        e5 = board.get_field("e5")
        d5 = board.get_field("d5")
        d6 = board.get_field("d6")
        d7 = board.get_field("d7")
        white_pawn: Pawn = Pawn(chess_field=e5)
        black_pawn: Pawn = Pawn(chess_field=d7)
        black_pawn.go_to_position(position=d5, board=board)
        # white_pawn.passent(d6)

    #
    # def test_passent_over_steps(self, board: Board):
    #     """Взятие на проходе через несколько ходов."""
    #     pass

    def test_capture(self, board: Board):
        """Взятие фигуры противника."""
        d3 = board.get_field("d3")
        e4 = board.get_field("e4")
        white_pawn = Pawn(chess_field=d3)
        _black_knight = Knight(chessman_side=ChessmanSide.BLACK, chess_field=e4)
        # съедаем черного коня пешкой
        white_pawn.go_to_position(e4, board=board)

    def test_bad_capture(self, board: Board):
        """Взятие фигуры противника перед пешкой."""
        d3 = board.get_field("d3")
        d4 = board.get_field("d4")
        white_pawn = Pawn(chess_field=d3)
        _black_pawn = Pawn(chess_field=d4, chessman_side=ChessmanSide.BLACK)
        # попытаемся взять чужую пешку ходом вперед
        with pytest.raises(InvalidStepException):
            white_pawn.go_to_position(d4, board=board)

    def test_king_capture(self, board: Board):
        """Взятие короля противника."""
        d3 = board.get_field("d3")
        c2 = board.get_field("c2")

        _black_king: King = King(chess_field=d3)
        white_pawn: Pawn = Pawn(chess_field=c2)
        with pytest.raises(KingCaptureError):
            white_pawn.go_to_position(d3, board=board)

    #
    # def test_step_with_exposing_king(self, board: Board):
    #     """Ход с открытием своего короля для шаха."""
    #     pass
