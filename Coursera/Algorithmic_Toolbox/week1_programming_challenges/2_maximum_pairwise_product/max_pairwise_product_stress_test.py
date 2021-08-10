# python3
import random


def stress_test(n, m):
    while True:
        n = random.randint(2, n)
        a = []

        for i in range(0, n):
            a.append(random.randint(0, m))
        # print(a)

        res1 = max_pairwise_product(a)
        res2 = max_pairwise_product_fast(a)

        if res1 == res2:
            print("OK")
            pass
        else:
            print("Wrong answer: " + res1 + ", " + res2)
            return


def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product


def max_pairwise_product_fast(numbers):
    # get the largest two numbers, and multiply them together
    a_i = 0

    # get first largest num
    for i in range(1, len(numbers)):
        # print("i = " + str(i))
        if numbers[i] > numbers[a_i]:
            a_i = i

    # move largest element to the end of the numbers list
    temp = numbers[len(numbers) - 1]
    numbers[len(numbers) - 1] = numbers[a_i]
    numbers[a_i] = temp

    a_i = 0

    # get second largest num
    for i in range(1, len(numbers) - 1):
        if numbers[i] > numbers[a_i]:
            a_i = i

    return numbers[a_i] * numbers[len(numbers) - 1]


if __name__ == '__main__':
    n, m = map(int, input().split())
    stress_test(n, m)
