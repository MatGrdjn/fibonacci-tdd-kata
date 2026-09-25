import marimo

__generated_with = "0.24.2"
app = marimo.App()


@app.cell
def _():
    import pytest
    import marimo as mo
    import time

    return mo, pytest, time


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Kata TDD - Fibonacci Sequence

    This notebook illustrates the Fibonacci sequence implementation following the TDD cycle.

    ### Mathematical definition :
    - $F(0) = 0$
    - $F(1) = 1$
    - $F(n) = F(n-1) + F(n-2)$ for $n \ge 2$
    """)
    return


@app.function
def fibonacci(n: int) -> int:
    """
    Compute the n-th term of the Fibonacci sequence (recursively)

    Args:
        n (int): Index of the desired term (must be a positive integer or zero)

    Returns: 
        int: Value of F(n)

    Raises:
        TypeError: If n is not an integer or a boolean
        ValueError: If n is negative
    """

    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n must be an int")
    if n < 0:
        raise ValueError("n must be positive or null")

    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return fibonacci(n-1) + fibonacci(n-2)


@app.cell
def _(pytest):
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

    return


@app.cell
def _(pytest):
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

    return


@app.cell
def _(time):
    def test_fibonacci_large_n():
        start = time.perf_counter()
        res = fibonacci(100_000)
        duration = time.perf_counter() - start

        assert res > 0
        assert duration < 1.0  

    return


@app.cell
def _(mo):
    n_input = mo.ui.slider(start=0, stop=30, step=1, value=0, label="n")
    n_input
    return (n_input,)


@app.cell
def _(mo, n_input):
    try:
        result = fibonacci(int(n_input.value))
        output = mo.md(f"`fibonacci({n_input.value})` → **{result}**")
    except ValueError as e:
        output = mo.md(f"⚠️ Error: {e}")
    output
    return


if __name__ == "__main__":
    app.run()
