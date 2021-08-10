# Uses python3
import sys

def optimal_weight(W, w):
    n = len(w) # number of items

    T = [[0 for _ in range(W+1)] for _ in range(n+1)]

    for r in range(n+1):
        for c in range(W+1):
            # fill first col and first row with zeros
            if r == 0 or c == 0:
                T[r][c] = 0
            elif w[r-1] <= c:
                T[r][c] = max(T[r-1][c], w[r-1] + T[r-1][c-w[r-1]])
            else:
                T[r][c] = T[r-1][c]

    return T[n][W]


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
