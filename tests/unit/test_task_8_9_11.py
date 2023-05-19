import pytest
from task_8_9_11 import decimal_to_binary, binary_to_decimal, validate_binary_input

@pytest.mark.parametrize('decimal, expected_binary', [
    (1, '1'),
    (255, '11111111')
])
def test_decimal_to_binary(decimal, expected_binary):
    assert decimal_to_binary(decimal) == expected_binary

@pytest.mark.parametrize('binary, expected_decimal', [
    ('0', 0),
    ('11111111', 255)
])
def test_binary_to_decimal(binary, expected_decimal):
    assert binary_to_decimal(binary) == expected_decimal

