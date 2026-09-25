import pytest

from fibonacci_kata import fibonacci

@pytest.mark.parametrize(
    ("n", "expected"),
    [
        (0, 0),
        (1, 1),
        (2, 1),
        (5, 5)
    ],
)
def test_fibonacci_suscess(n, expected):
    assert fibonacci(n) == expected