# Uses python3
import sys


def binary_search(a, x):
    left, right = 0, len(a)-1
    # write your code here

    return bs_helper(a, left, right, x)


def bs_helper(a, left, right, x):
    # base case - list is empty
    if right < left:
        return -1

    mid = left + (right - left) // 2

    if x == a[mid]:
        return mid
    elif x < a[mid]:
        return bs_helper(a, left, mid - 1, x)
    else:
        return bs_helper(a, mid + 1, right, x)


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1: n + 1]

    # sort the array ascending
    a.sort()

    result = []

    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        result.append(binary_search(a, x))
        #print(linear_search(a, x), end=' ')

    print(' '.join([str(r) for r in result]))
