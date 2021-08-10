# Uses python3
import sys


def get_majority_element(a, left, right):
    # Base case - empty array
    if left == right:
        return -1

    # Base case - array has one element, so it is the majority element
    if left + 1 == right:
        return a[left]

    mid = left + (right - left) // 2
    left_element = get_majority_element(a, left, mid)
    right_element = get_majority_element(a, mid + 1, right)

    if left_element == right_element:
        return left_element

    left_count = 0
    for i in range(left, right):
        if a[i] == left_element:
            left_count += 1

    if left_count > (right - left) // 2:
        return left_element

    right_count = 0
    for i in range(left, right):
        if a[i] == right_element:
            right_count += 1

    if right_count > (right - left) // 2:
        return right_element

    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))

    a.sort()

    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
