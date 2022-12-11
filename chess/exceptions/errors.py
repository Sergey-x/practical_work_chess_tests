class ChessError(Exception):
    pass


class GoOutOfBoardError(ChessError):
    """Попытка выходя за пределы доски."""
    pass


class KingPromotionError(ChessError):
    """Попытка превращения в короля."""
    pass


class KingCaptureError(ChessError):
    """Попытка превращения в короля."""
    pass
