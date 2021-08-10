# Uses python3
import sys


def get_fibonacci_last_digit(n):
    fib_last_digits = [0, 1]

    for i in range(2, n+1):
        last_digit = (fib_last_digits[-2] + fib_last_digits[-1]) % 10
        fib_last_digits.append(last_digit)

    return fib_last_digits[n]


if __name__ == '__main__':
    n = int(input())
    print(get_fibonacci_last_digit(n))
