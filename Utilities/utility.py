import numpy as n
from typing import Any

def is_equal_unordered(value_a: [Any], value_b: [Any]):
    narr1 = n.array([value_a])
    narr2 = n.array([value_b])

    return (narr1 == narr2).all()