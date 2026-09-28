import marimo

__generated_with = "0.25.0"
app = marimo.App(width="medium")


@app.function
def fibonnacci(n:int) -> int:
    if n<=1:
        return n
    else:
        return fibonnacci(n-1) + fibonnacci(n-2)


@app.cell
def _():
    def test_fibonnacci_0():
        assert fibonnacci(0)==0

    def test_fibonnacci_1():
        assert fibonnacci(1)==1

    def test_fibonnacci_2():
        assert fibonnacci(2)==1

    def test_fibonnacci_3():
        assert fibonnacci(3)==2

    def test_fibonnacci_5():
        assert fibonnacci(5)==5

    def test_fibonnacci_10():
        assert fibonnacci(10)==55

    return


if __name__ == "__main__":
    app.run()
