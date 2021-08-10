# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here

    # insert weights and values into a list as tuples, then sort in descending order
    items = []
    for i in range(0, len(weights)):
        items.append((values[i] / weights[i], weights[i]))

    items.sort(reverse=True)

    # print(items)

    while capacity > 0 and len(items) > 0:
        # TODO: modify this to add fractional items

        item_value = items[0][0] * items[0][1]
        item_weight = items[0][1]

        # if there isn't enough space left, add fractional item
        if capacity - item_weight < 0:
            value += (capacity / item_weight) * item_value
            # print("adding partial item_value = " + str((capacity / item_weight) * item_value))
            # print("adding partial item_weight = " + str((capacity / item_weight) * item_weight))
            capacity = 0
        else:
            value += item_value
            capacity -= item_weight
            items.pop(0)
            # print("adding item_value = " + str(item_value))
            # print("adding item_weight = " + str(item_weight))

        # print("capacity = " + str(capacity))

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]

    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]

    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.4f}".format(opt_value))
