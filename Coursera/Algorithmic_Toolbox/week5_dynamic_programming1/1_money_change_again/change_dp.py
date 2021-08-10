# Uses python3
import sys


# Return the least amount of coins that can be used to make change for m
# using the given coin denominations
def get_change(coins, m):
    min_ways = [0 for x in range(m + 1)]

    # base case
    min_ways[0] = 0

    # initialize array values as some max value
    for i in range(1, m+1):
        min_ways[i] = sys.maxsize

    # for each possible value
    for i in range(1, m+1):
        # for each coin smaller than the current value, i
        for j in range(len(coins)):
            if coins[j] <= i:
                result = min_ways[i - coins[j]]
                if result != sys.maxsize and result + 1 < min_ways[i]:
                    min_ways[i] = result + 1

        # print(min_ways)

    if min_ways[m] == sys.maxsize:
        return -1

    # print(min_ways)

    return min_ways[m]


# get the number of ways you can make each change amount
def num_ways_to_make_change(coins, m):
    # Create an array from 0 to m, and fill it with zeros
    # Each value in this array represents the number of ways to
    # make the index out of the set of coins.
    ways = [0 for x in range(m + 1)]

    # there is 1 way to make 0, which is 0 coins
    ways[0] = 1

    # Populate the ways array by comparing each coin to all indexes of
    # the ways array
    for i in range(len(coins)):
        for j in range(len(ways)):
            # if the coin value is <= to the index, increment the ways value
            if coins[i] <= j:
                ways[j] += ways[j - coins[i]]

    # print(ways)

    return ways[m]


def fib_dp(n):
    f = [0, 1]

    for i in range(2, n+1):
        f.append(f[i-1] + f[i-2])

    return f[n]


if __name__ == '__main__':
    m = int(sys.stdin.read())
    coins = [1, 3, 4]
    print(get_change(coins, m))
    #print(fib_dp(m))
