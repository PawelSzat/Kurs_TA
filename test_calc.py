import pytest
import subprocess
from calc import Calculator

def test_add():
    calc = Calculator()
    assert calc.add(2, 3) == 5

def test_sub():
    calc = Calculator()
    assert calc.sub(5, 3) == 2

test_data = [
    ('a', 2, ValueError),
    (2, 'b', ValueError),
    (2.5, 3, TypeError),
]

@pytest.mark.parametrize("a, b, expected", [
    ('a', 2, ValueError),
    (2, 'b', ValueError),
    (2.5, 3, TypeError),
])
def test_non_numeric_input(a, b, expected):
    calc = Calculator()
    with pytest.raises(expected):
        calc.add(a, b)
#nie zgłasza jako błąd
def test_div_by_zero():
    calc = Calculator()
    with pytest.raises(ZeroDivisionError):
        calc.div(5, 0)
