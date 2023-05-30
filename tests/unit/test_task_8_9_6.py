import pytest
from task_8_9_6 import validate_input, is_leap_year

@pytest.mark.parametrize("input_str, expected", [("42", 42), ("0", 0)])
def test_validate_input_positive_integer(input_str, expected):
    assert validate_input(input_str) == expected

@pytest.mark.parametrize("year", [2020, 2000])
def test_is_leap_year_leap_year(year):
    assert is_leap_year(year) == True

@pytest.mark.parametrize("year", [2021, 1900])
def test_is_leap_year_non_leap_year(year):
    assert is_leap_year(year) == False

#def test_validate_input_invalid_input():
#    input_str = "abc"  # Некорректный ввод: не является целым числом
#    with pytest.raises(ValueError):
#        validate_input(input_str)
