import pytest
from task_5_2 import count_digits


@pytest.mark.parametrize("num, expected_count", [(5, 1), (12345, 5), (-987654321, 9)])
def test_count_digits(num, expected_count):
    assert count_digits(num) == expected_count
