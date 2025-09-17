# 1. Recursion of Fibonacci
# 2. Yes
# 3. O(2^n)
def fib_memo(n, memo={}):

    if n in memo:  # Check if result is already computed

        return memo[n]

    if n == 0 or n == 1:

        return n

    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)

    return memo[n]