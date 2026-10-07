# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo",
#     "matplotlib",
# ]
# ///

import marimo

__generated_with = "0.25.0"
app = marimo.App(width="medium")

with app.setup:
    import marimo as mo
    import matplotlib.pyplot as plt

    from fibonacci_kata import fibonacci, fibonacci_mod


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    # Fibonacci Explorer

    Choose a range of indices and explore the Fibonacci sequence
    interactively.

    This notebook uses the installed `fibonacci_kata` package —
    it does not reimplement the Fibonacci algorithms.
    """)
    return


@app.cell
def _():
    start = mo.ui.slider(
        0,
        40,
        value=0,
        label="Range start",
    )

    end = mo.ui.slider(
        0,
        40,
        value=20,
        label="Range end",
    )

    modulus = mo.ui.dropdown(
        options=[10, 100, 1_000, 1_000_000, 1_000_000_000],
        value=1_000_000_000,
        label="Modulo",
    )

    mo.hstack([start, end, modulus])
    return end, modulus, start


@app.cell
def _(end, modulus, start):
    lo, hi = sorted((start.value, end.value))

    indices = list(range(lo, hi + 1))

    fibonacci_values = [fibonacci(n) for n in indices]

    modulo_values = [fibonacci_mod(n, modulus.value) for n in indices]
    return fibonacci_values, indices, modulo_values


@app.cell
def _(fibonacci_values, indices, modulo_values, modulus):
    fig, ax = plt.subplots()

    ax.plot(
        indices,
        fibonacci_values,
        marker="o",
        label="Fibonacci",
    )

    ax.plot(
        indices,
        modulo_values,
        marker="o",
        label=f"Fibonacci mod {modulus.value}",
    )

    ax.set_xlabel("n")
    ax.set_ylabel("F(n)")
    ax.set_title("Fibonacci sequence over the selected range")
    ax.legend()
    ax.grid()

    fig
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ## Large Fibonacci values

    For very large indices, computing the full Fibonacci number is not practical.

    Use the fast-doubling `fibonacci_mod` function below to compute
    `F(n) mod m` efficiently.
    """)
    return


@app.cell
def _():
    large_n = mo.ui.number(
        value=10**18,
        start=0,
        label="Large n",
    )

    large_modulus = mo.ui.number(
        value=1_000_000_000,
        start=1,
        label="Modulo",
    )

    mo.hstack([large_n, large_modulus])
    return large_modulus, large_n


@app.cell
def _(large_modulus, large_n):
    large_result = fibonacci_mod(
        large_n.value,
        large_modulus.value,
    )

    mo.md(
        f"""
        ### Result

        `F({large_n.value}) mod {large_modulus.value} = {large_result}`
        """
    )
    return


if __name__ == "__main__":
    app.run()
