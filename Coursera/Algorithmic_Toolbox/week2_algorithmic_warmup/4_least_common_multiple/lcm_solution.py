# Uses python3
import sys


def lcm(a, b):
    return int((a * b) / gcd(a, b))


def gcd(a, b):
    if a == 0:
        return b

    return gcd(b % a, a)


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm(a, b))

