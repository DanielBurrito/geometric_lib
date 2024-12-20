import pytest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from calculate import calc, figs, funcs

# Моки для circle и square
class MockCircle:
    @staticmethod
    def area(radius):
        return 3.14 * radius**2

    @staticmethod
    def perimeter(radius):
        return 2 * 3.14 * radius


class MockSquare:
    @staticmethod
    def area(side):
        return side**2

    @staticmethod
    def perimeter(side):
        return 4 * side


# Моки подключаем перед тестами
import sys
sys.modules['circle'] = MockCircle
sys.modules['square'] = MockSquare


@pytest.mark.parametrize("fig, func, size, expected", [
    ("circle", "area", [3], 28.26),        # Тест площади круга
    ("circle", "perimeter", [3], 18.84),  # Тест периметра круга
    ("square", "area", [4], 16),          # Тест площади квадрата
    ("square", "perimeter", [4], 16),     # Тест периметра квадрата
])
def test_calc(fig, func, size, expected):
    # Arrange
    assert fig in figs  # Убедимся, что фигура допустима
    assert func in funcs  # Убедимся, что функция допустима

    # Act
    result = calc(fig, func, size)

    # Assert
    assert result == pytest.approx(expected, 0.01)
