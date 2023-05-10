import pytest
from task_5_3 import calculate_square_root


@pytest.mark.parametrize("a, x, expected", [
    (4, 2, 2.0),
    (9, 3, 3.0),
    (16, 1, 4.0),
    (25, 5, 5.0)
])
def test_calculate_square_root(a, x, expected):
    result = calculate_square_root(a, x)
    assert result == expected

if __name__ == '__main__':
    pytest.main()