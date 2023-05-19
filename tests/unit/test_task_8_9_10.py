import pytest
from task_8_9_10 import determine_square_color, validate_input


@pytest.mark.parametrize('position', [('a1'), ('h8')])
def test_determine_square_color_black(position):
    assert determine_square_color(position) == 'black'


@pytest.mark.parametrize('position', [('a2'), ('b1')])
def test_determine_square_color_white(position):
    assert determine_square_color(position) == 'white'


@pytest.mark.parametrize('position', [('a0'), ('h9'), ('',), ('a',)])
def test_validate_input_invalid(position):
    assert validate_input(position) == False


@pytest.mark.parametrize('position', [('a1')])
def test_validate_input_valid(position):
    assert validate_input(position) == True
