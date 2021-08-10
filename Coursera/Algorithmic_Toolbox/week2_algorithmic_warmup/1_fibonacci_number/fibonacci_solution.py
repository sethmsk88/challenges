# Uses python3
def calc_fib(n):
    fibs = [0, 1]

    for i in range(2, n+1):
        fibs.append(fibs[-2] + fibs[-1])

    return fibs[n]


n = int(input())
print(calc_fib(n))