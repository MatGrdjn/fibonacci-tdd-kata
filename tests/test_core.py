import pytest
import time

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

def test_fibonacci_large_scale_performance():
    start = time.perf_counter()
    result = fibonacci(100_000)
    elapsed = time.perf_counter() - start

    assert result > 0
    assert elapsed < 0.5, f"Too slow : {elapsed:.3f}s"

@pytest.mark.timeout(5)
def test_fibonacci_extreme_scale():
    n = 10_000_000
    start = time.perf_counter()
    result = fibonacci(n)
    elapsed = time.perf_counter() - start

    assert result > 0
    assert elapsed < 5.0, f"Too slow for 10^7 : {elapsed:.3f}s"