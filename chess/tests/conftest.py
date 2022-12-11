import pytest

from chess.board import Board


@pytest.fixture(scope="function")
def board() -> Board:
    """Пустая шахматная доска."""
    return Board()
