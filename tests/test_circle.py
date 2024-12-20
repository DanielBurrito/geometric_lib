import math
import pytest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
from circle import area, perimeter

def test_area():

    r = 2
    expected_area = math.pi * 4


    result = area(r)


    assert result == pytest.approx(expected_area, rel=1e-2), f"Expected {expected_area}, but got {result}"

def test_perimeter():

    r = 3
    expected_perimeter = math.pi * 6

    result = perimeter(r)

    assert result == pytest.approx(expected_perimeter, rel=1e-2), f"Expected {expected_perimeter}, but got {result}"

