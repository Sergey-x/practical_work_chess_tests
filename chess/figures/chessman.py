from __future__ import annotations

import abc

from chess.enums import ChessmanSide, ChessmanType, ChessMoveTypes
from chess.exceptions.errors import KingCaptureError
from chess.exceptions.exceptions import GoOverOwnFigureException
from chess.moves import ChessMove


class BaseChessman(abc.ABC):
    @abc.abstractmethod
    def get_position(self) -> ChessField:
        pass

    @abc.abstractmethod
    def go_to_position(self, position: ChessField, board) -> None:
        pass


class Chessman(BaseChessman, abc.ABC):
    def __init__(self,
                 chessman_type: ChessmanType,
                 chess_field: ChessField,
                 chessman_side: ChessmanSide = ChessmanSide.WHITE):
        self._chessman_type: ChessmanType = chessman_type
        self._chessman_side: ChessmanSide = chessman_side
        self._is_active: bool = True
        self._chess_field: ChessField = chess_field
        self._chess_field.set_figure(figure=self)

    @property
    def chess_field(self) -> ChessField:
        return self._chess_field

    def get_position(self) -> ChessField:
        return self._chess_field

    def go_to_position(self, position: ChessField, board) -> None:
        """Ограничения для всех фигур.

        Проверки: выход за пределы поля; взятие короля; взятие фигуры своего цвета.

        """
        captured_figure = position.is_busy()
        move_type: ChessMoveTypes = ChessMoveTypes.EMPTY_STEP

        # проверяем, есть ли в клетке чужая фигура, если есть, то съедаем её
        if captured_figure is not None:
            if captured_figure._chessman_side == self._chessman_side:
                raise GoOverOwnFigureException()

            # короля есть нельзя
            if captured_figure._chessman_type == ChessmanType.KING:
                raise KingCaptureError()

            captured_figure._is_active = False
            move_type = ChessMoveTypes.CAPTURE

        # заносим ход в историю партии
        move: ChessMove = ChessMove(figure=self._chessman_type,
                                    start=self._chess_field,
                                    end=position,
                                    move_type=move_type,
                                    )
        board.add_move(move)

        # убираем фигуру с позиции
        self._chess_field.drop_figure()

        # ставим фигуру в клетку
        self._chess_field = position

    def __str__(self) -> str:
        return self._chessman_type


class ChessField:
    def __init__(self, pos: str):
        self._pos = pos
        self._figure: Chessman | None = None

    @property
    def row(self) -> int:
        return int(self._pos[1])

    @property
    def col(self) -> str:
        return self._pos[0]

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
