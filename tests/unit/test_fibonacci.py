import pytest
from task_4 import find_fibonacci


@pytest.mark.parametrize('input_number, expected_output', [
    (0, 1),
    (1, 1),
    (2, 3),
    (5, 8),
    (21, 34),
])
def test_find_fibonacci(input_number, expected_output):
    assert find_fibonacci(input_number) == expected_output
