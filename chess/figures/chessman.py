import abc

from chess.enums import ChessmanSide, ChessmanType
from chess.exceptions.common import GoOverOwnFigureException
from chess.exceptions.errors import KingCaptureError


class BaseChessman(abc.ABC):
    @abc.abstractmethod
    def get_position(self):
        pass

    @abc.abstractmethod
    def go_to_position(self, position):
        pass


class Chessman(BaseChessman, abc.ABC):
    def __init__(self,
                 chessman_type: ChessmanType,
                 chess_field,
                 chessman_side: ChessmanSide = ChessmanSide.WHITE):
        self._chessman_type = chessman_type
        self._chessman_side = chessman_side
        self._chess_field = chess_field
        self._chess_field.set_figure(figure=self)
        self._is_active = True

    def get_position(self):
        return self._chess_field

    def go_to_position(self, position, board=None):
        captured_figure = position.is_busy()

        # проверяем, есть ли в клетке чужая фигура, если есть, то съедаем её
        # print(f"{captured_figure._chessman_side=}")
        print(f"{self._chessman_side=}")
        if captured_figure is not None:
            if captured_figure._chessman_side == self._chessman_side:
                raise GoOverOwnFigureException()

            # короля есть нельзя
            if captured_figure._chessman_type == ChessmanType.KING:
                raise KingCaptureError()

            captured_figure._is_active = False

        # убираем фигуру с позиции
        self._chess_field.drop_figure()

        # ставим фигуру в клетку
        self._chess_field = position
