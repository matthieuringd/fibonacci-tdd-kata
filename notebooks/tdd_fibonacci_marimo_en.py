import marimo

__generated_with = "0.25.0"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Fibonacci TDD Kata

    This notebook implements the Fibonacci sequence using Test-Driven Development.

    The Fibonacci sequence is defined by:

    - F(0) = 0
    - F(1) = 1
    - F(n) = F(n-1) + F(n-2)

    Use the widget below to calculate a Fibonacci number.
    """)


@app.function
def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    previous = 0
    current = 1
    for _ in range(2, n + 1):
        next_value = current + previous
        previous = current
        current = next_value
    return current


@app.cell
def _():
    def test_fibonacci_0():
        assert fibonacci(0) == 0

    def test_fibonacci_1():
        assert fibonacci(1) == 1

    def test_fibonacci_2():
        assert fibonacci(2) == 1

    def test_fibonacci_3():
        assert fibonacci(3) == 2

    def test_fibonacci_5():
        assert fibonacci(5) == 5

    def test_fibonacci_10():
        assert fibonacci(10) == 55

    def test_fibonacci_20():
        assert fibonacci(20) == 6765

    def test_fibonacci_30():
        assert fibonacci(30) == 832040

    def test_fibonacci_40():
        assert fibonacci(40) == 102334155


@app.cell
def _():

    import marimo as mo

    n_input = mo.ui.number(start=0, stop=30, step=1, value=10, label="Choose a Fibonacci index:")

    return mo, n_input


@app.cell
def _(mo, n_input):
    result = fibonacci(n_input.value)

    mo.md(
        f"""
        ### Result

        Fibonacci({n_input.value}) = **{result}**
        """
    )


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Fibonacci modulo for very large values

    For very large values of `n`, computing the complete Fibonacci number
    is inefficient and unnecessary.

    We want to compute:

    F(n) mod m

    with:

    - `m = 1,000,000,000`
    - `0 <= n <= 10^18`

    Because addition and multiplication are compatible with the modulo
    operation, we can apply the modulo during the computation instead of
    building the complete Fibonacci number.
    """)


@app.function
def fibonacci_mod(n: int, m: int = 1_000_000_000) -> int:
    """Return F(n) modulo m using the fast-doubling algorithm."""

    def compute_pair(n: int) -> tuple[int, int]:
        # Base case: F(0) = 0 and F(1) = 1
        if n == 0:
            return 0, 1

        # Compute Fibonacci values for n // 2
        fib_n, fib_next = compute_pair(n // 2)

        # Fast doubling formulas
        even_value = (fib_n * (2 * fib_next - fib_n)) % m
        odd_value = (fib_n * fib_n + fib_next * fib_next) % m

        if n % 2 == 0:
            return even_value, odd_value
        else:
            return odd_value, (even_value + odd_value) % m

    result = compute_pair(n)

    return result


@app.cell
def _():
    def test_fibonacci_mod_10():
        assert fibonacci_mod(10) == 55

    def test_fibonacci_mod_100():
        assert fibonacci_mod(100) == 261915075

    def test_fibonacci_mod_1000():
        assert fibonacci_mod(1000) == 849228875

    def test_fibonacci_mod_large():
        assert fibonacci_mod(10**18) == 560546875


if __name__ == "__main__":
    app.run()
