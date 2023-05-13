import pytest
from task_5_2 import count_digits

def test_count_digits():
    assert count_digits(5) == 1
    assert count_digits(12345) == 5
    assert count_digits(-987654321) == 9

