# Uses python3
import sys

# Possible operations on x are:
# x = x * 2
# x = x * 3
# x = x + 1

def dp_optimal_sequence2(n):
    sequence = []

    a = [0 for _ in range(n+1)]

    for i in range(1, n+1):
        a[i] = a[i-1] + 1

        if i % 2 == 0:
            x = a[i // 2]
            if x+1 < a[i]:
                a[i] = x+1

        if i % 3 == 0:
            x = a[i // 3]
            if x+1 < a[i]:
                a[i] = x+1

    i = n
    while i > 1:
        sequence.append(i)

        if a[i - 1] == a[i] - 1:
            i -= 1
        elif i % 2 == 0 and a[i // 2] == a[i] - 1:
            i = i // 2
        elif i % 3 == 0 and a[i // 3] == a[i] - 1:
            i = i // 3
        else:
            i -= 1

    sequence.append(1)

    return a[n]-1, sequence


# Naive solution
def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return sequence

input = sys.stdin.read()
n = int(input)

# sequence = optimal_sequence(n)
# num_ops = len(sequence) - 1
# print(num_ops)
# for i in reversed(sequence):
#     print(i, end=' ')
# print()

(num_ops, sequence) = dp_optimal_sequence2(n)
print(num_ops)
for i in reversed(sequence):
    print(i, end=' ')
