import pytest

from homework_8 import random_value


@pytest.mark.parametrize("value", ["int", "float"])
def test_random_value_success(value):
    got_value = random_value(value)

    if value == "int":
        assert isinstance(got_value, int)
    else:
        assert isinstance(got_value, float)


@pytest.mark.parametrize("value", ["tuple", "lol", "list"])
def test_random_value_value_error(value):
    with pytest.raises(ValueError, match=f"not correct value, must be 'int' or 'float', but got: {value}"):
        random_value(value)
