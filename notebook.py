import marimo

__generated_with = "0.25.0"
app = marimo.App(width="medium")


@app.function
def fibonacci(n:int) -> int:
    if n<=1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


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
