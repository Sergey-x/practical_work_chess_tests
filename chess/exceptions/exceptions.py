class BaseChessException(Exception):
    pass


class InvalidStepException(BaseChessException):
    pass


class InvalidPromotionException(BaseChessException):
    pass


class BasePassentException(BaseChessException):
    pass


class InvalidPassentException(BasePassentException):
    pass


class ExpiredPassentException(BasePassentException):
    pass


class CaptureKingException(InvalidStepException):
    """Попытка взятия короля."""
    pass


class GoOverOwnFigureException(InvalidStepException):
    """Попытка взять свою фигуру."""
    pass


class OpenKingException(InvalidStepException):
    """Ход с открытием короля для шаха."""
    pass


class PromotionToKingException(InvalidPromotionException):
    """Превращение пешки в короля."""
    pass


class PromotionOnBadLineException(InvalidPromotionException):
    """Превращение пешки не в конце доски."""
    pass
