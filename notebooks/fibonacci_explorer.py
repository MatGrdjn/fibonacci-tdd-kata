import marimo

__generated_with = "0.24.2"
app = marimo.App()


@app.cell
def _():
    import math

    import marimo as mo
    import matplotlib.pyplot as plt

    from fibonacci_kata import fibonacci

    return fibonacci, math, mo, plt


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Fibonacci Explorer

    Pick a number and see how the ratio `fibonacci(n)` / `fibonacci(n - 1)`
    converges towards $\varphi$, the golden ratio.
    This notebook consumes the fibonacci_kata package - it does not reimplement the function
    """)
    return


@app.cell
def _(mo):
    n = mo.ui.slider(5, 40, value=10, step=1, label="Rank n")
    n
    return (n,)


@app.cell
def _(fibonacci, math, n, plt):
    phi = (1 + math.sqrt(5)) / 2
    n_max = int(n.value)

    ranks = list(range(2, n_max + 1))
    ratios = [fibonacci(k) / fibonacci(k - 1) for k in ranks]

    fig, ax = plt.subplots(figsize=(9, 4))

    ax.plot(
        ranks,
        ratios,
        marker="o",
        label=r"$\frac{F(n)}{F(n-1)}$",
    )

    ax.axhline(
        phi,
        color="red",
        linestyle="--",
        label=rf"Limite $\varphi$ ({phi:.6f})",
    )

    ax.set_title("Convergence towards Golden ratio")
    ax.set_xlabel("n")
    ax.set_ylabel("Ratio")
    ax.legend()
    ax.grid()

    plt.show()
    return


if __name__ == "__main__":
    app.run()
