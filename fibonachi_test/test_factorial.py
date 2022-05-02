import factorial
import pytest

"""Если не находит модуль factorial
python -m pytest test_factorial.py
"""

#
# Check valid inputs.
#
def test_fact_0():
    assert factorial.factorial(0) == 1


def test_fact_1():
    assert factorial.factorial(1) == 1


def test_fact_2():
    assert factorial.factorial(2) == 2


def test_fact_3():
    assert factorial.factorial(3) == 6


def test_fact_10():
    assert factorial.factorial(10) == 3628800


def test_fact_20():
    assert factorial.factorial(20) == 2432902008176640000


def test_fact_30():
    assert factorial.factorial(30) == 265252859812191058636308480000000


def test_fact_40():
    assert factorial.factorial(40) == \
           815915283247897734345611269596115894272000000000


def test_fact_50():
    assert factorial.factorial(50) == \
           30414093201713378043612608166064768844377641568960512000000000000


#
# Invalid input: exception is expected.
#
def test_fact_minus1():
    with pytest.raises(Exception):
        assert factorial.factorial(-1)