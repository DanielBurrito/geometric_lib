import pytest
import math
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
from triangle import area, perimeter

def test_area():
    
    a, b, c = 5, 12, 13
    expected_area = 30

    result = area(a, b, c)

    assert result == pytest.approx(expected_area), f"Expected {expected_area}, but got {result}"

def test_perimeter():
    
    a, b, c = 1, 2, 3
    expected_perimeter = 6

    result = perimeter(a, b, c)

    assert result == expected_perimeter
