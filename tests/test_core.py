
from fibonacci_kata.core import fibonacci, fibonacci_mod


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






def test_fibonacci_mod_10():
    assert fibonacci_mod(10) == 55


def test_fibonacci_mod_100():
    assert fibonacci_mod(100) == 261915075


def test_fibonacci_mod_1000():
    assert fibonacci_mod(1000) == 849228875


def test_fibonacci_mod_large():
    assert fibonacci_mod(10**18) == 560546875
