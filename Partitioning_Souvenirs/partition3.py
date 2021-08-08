# Uses python3
import sys
import itertools

def dpPartition3(A):
    sumOfItemValues = sum(A)

    # print("Sum = " + str(sumOfItemValues))

    if sumOfItemValues == 0:
        return 1

    # Check to see if sum of all items is divisible by 3
    if sumOfItemValues % 3 > 0:
        return 0    # cannot partition evenly

    n = len(A)  # number of items

    T = [[0 for c in range((sumOfItemValues // 3) + 1)] for r in range(n + 1)]

    for r in range(1, n + 1):
        for c in range(1, (sumOfItemValues // 3) + 1):
            if A[r - 1] <= c:
                T[r][c] = max(T[r - 1][c], A[r - 1] + T[r - 1][c - A[r - 1]])
            else:
                T[r][c] = T[r - 1][c]

    # print(T)

    if T[n][sumOfItemValues // 3] == sumOfItemValues // 3:
        return 1
    else:
        return 0


def partition3(A):
    for c in itertools.product(range(3), repeat=len(A)):
        sums = [None] * 3
        for i in range(3):
            sums[i] = sum(A[k] for k in range(len(A)) if c[k] == i)

        if sums[0] == sums[1] and sums[1] == sums[2]:
            return 1

    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(dpPartition3(A))

