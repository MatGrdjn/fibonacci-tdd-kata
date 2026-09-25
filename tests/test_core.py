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

@pytest.mark.parametrize(
    ("input", "expected_exception", "expected_message"),
    [
        (-1, ValueError, "n must be positive or null"),
        ("1", TypeError, "n must be an int"),
        (1.5, TypeError, "n must be an int"),
        (True, TypeError, "n must be an int"),
    ],
)
def test_fibonacci_errors(input, expected_exception, expected_message):
    with pytest.raises(expected_exception, match=expected_message):
        fibonacci(input)