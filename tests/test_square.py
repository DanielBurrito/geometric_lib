import pytest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
from square import area, perimeter  


def test_area():
    
    a = 2  
    
    result = area(a)
    
    expected = a * a 
    assert result == expected 

def test_perimeter():
    a = 2  
    
    result = perimeter(a)

    expected = 4 * a 
    assert result == expected  

