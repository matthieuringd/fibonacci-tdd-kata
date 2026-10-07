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


def fibonacci_mod(n, m=1_000_000_000):
    
    """Return F(n) modulo m using the fast-doubling algorithm."""
    
    def compute_pair(n):
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