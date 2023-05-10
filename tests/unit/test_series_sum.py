import math
import pytest
from task_5_1 import series_sum


def test_sum():
    x = 1
    precision = 4
    expected_result = 13.9487
    result = round(series_sum(x, precision), precision)
    assert result == expected_result

if __name__ == '__main__':
    pytest.main()