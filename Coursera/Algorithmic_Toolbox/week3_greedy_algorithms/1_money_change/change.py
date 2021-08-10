# Uses python3
import sys

def get_change(m):
    #write your code here
    num_coins = 0
    coin_denominations = [10, 5, 1]

    for i in range(len(coin_denominations)):
        num_this_coin = (int)(m / coin_denominations[i])
        num_coins += num_this_coin
        m -= num_this_coin * coin_denominations[i]

    return num_coins

if __name__ == '__main__':
    m = int(input()) # input a single integer
    print(get_change(m))
