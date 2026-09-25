import marimo

__generated_with = "0.24.2"
app = marimo.App()


@app.cell
def _():
    import pytest
    import marimo as mo

    return (pytest,)


@app.function
def fibonacci(n: int) -> int:

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


if __name__ == "__main__":
    app.run()
