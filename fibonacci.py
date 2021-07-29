import sys


# Method: Recursion
# Runtime = O(2^n)
def fib_recursive(n):
    if n == 0 or n == 1:
        return n

    return fib_recursive(n - 1) + fib_recursive(n - 2)


# Method: Top-down dynamic programming (memoization)
# Runtime = O(n)
def fib_memoization(n):
    memo = [0 for i in range(n + 1)]

    return fib_memoization_helper(n, memo)


def fib_memoization_helper(i, memo):
    if i == 0 or i == 1:
        return i

    # if fib value for n hasn't been calculated yet, calculate it and store it in the cache
    if memo[i] == 0:
        memo[i] = fib_memoization_helper(i - 1, memo) + fib_memoization_helper(i - 2, memo)

    return memo[i]


# Method: Bottom-up dynamic programming
# Runtime = O(n)
def fib_dp(n):
    if n == 0 or n == 1:
        return n

    memo = [0, 1]   # initialize with base cases

    for i in range(2, n + 1):
        memo.append(memo[i - 1] + memo[i - 2])

    return memo[n]


# Method: Bottom-up dynamic programming
# Runtime = O(n)
# Uses less memory than the fib_dp function, because we don't store all of the numbers in the memo array
def fib_dp_improved(n):
    if n == 0:
        return 0

    a = 0
    b = 1

    for i in range(2, n + 1):
        c = a + b
        a = b
        b = c

    return c


if __name__ == '__main__':
    n = int(sys.stdin.read())
    # print(fib_recursive(n))
    # print(fib_memoization(n))
    # print(fib_dp(n))
    print(f1ib_dp_improved(n))