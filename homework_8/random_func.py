import random
from typing import Optional


def random_value(value_type: str) -> Optional[int | float]:
    """function return float or int value by request

    Args:
        value_type (str): 'int' or 'float'

    Raises:
        ValueError: not correct value, must be 'int' or 'float', but got: {value_type}

    Returns:
        Optional[int|float]: 1 or 0.1
    """
    match value_type:
        case "int":
            return random.randint(0, 100)
        case "float":
            return random.random()

    raise ValueError(f"not correct value, must be 'int' or 'float', but got: {value_type}")
