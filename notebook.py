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
    return


@app.function
def fibonacci(n:int) -> int:
    if n<=1:
        return n
    previous=0
    current=1
    for _ in range(2, n+1):
        next_value=current + previous
        previous=current
        current=next_value
    return current


@app.cell
def _():
    def test_fibonacci_0():
        assert fibonacci(0)==0

    def test_fibonacci_1():
        assert fibonacci(1)==1

    def test_fibonacci_2():
        assert fibonacci(2)==1

    def test_fibonacci_3():
        assert fibonacci(3)==2

    def test_fibonacci_5():
        assert fibonacci(5)==5

    def test_fibonacci_10():
        assert fibonacci(10)==55

    def test_fibonacci_20():
        assert fibonacci(20) == 6765


    def test_fibonacci_30():
        assert fibonacci(30) == 832040


    def test_fibonacci_40():
        assert fibonacci(40) == 102334155

    return


@app.cell
def _():
    import marimo as mo 

    n_input = mo.ui.number(
        start=0,
        stop=30,
        step=1,
        value=10,
        label="Choose a Fibonacci index:"
    )

    n_input
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
    return


if __name__ == "__main__":
    app.run()
