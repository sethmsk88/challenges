# python3


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
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product_fast(input_numbers))
