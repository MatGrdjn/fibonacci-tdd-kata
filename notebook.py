import marimo

__generated_with = "0.24.2"
app = marimo.App()


@app.cell
def _():
    import pytest
    import marimo as mo

    return


@app.function
def fibonacci(n: int) -> int:
    ...


if __name__ == "__main__":
    app.run()
