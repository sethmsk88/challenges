# Uses python3

# Method: Dynamic Programming (Bottom-up)
# Runtime = O(s*t)
def edit_distance_dp(s, t, m, n):
    # Create a table to store results
    tbl = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # Fill table t from the bottom up
    for i in range(m + 1):
        for j in range(n + 1):

            # If first string is empty, only option is to
            # insert all characters of second string
            if i == 0:
                tbl[i][j] = j  # Min. operations = j

            # If second string is empty, only option is to
            # remove all characters of second string
            elif j == 0:
                tbl[i][j] = i  # Min. operations = i

            # If last characters are same, ignore last char
            # and recur for remaining string
            elif s[i - 1] == t[j - 1]:
                tbl[i][j] = tbl[i - 1][j - 1]

            # If last character are different, consider all
            # possibilities and find minimum
            else:
                tbl[i][j] = 1 + min(tbl[i][j - 1],  # Insert
                                    tbl[i - 1][j],  # Remove
                                    tbl[i - 1][j - 1])  # Replace

    return tbl[m][n]


# Method: Recursion
# Runtime = O(3^n)
def edit_distance_recursive(s, t, i, j):
    # Base cases for when one of the strings is empty
    if i == 0:
        return j
    if j == 0:
        return i

    # Starting from the end of the strings, if both characters are the same,
    # move to the next character, and recurse.
    if s1[i - 1] == s2[j - 1]:
        return edit_distance_recursive(s1, s2, i - 1, j - 1)

    # If the last 2 character are different, recurse for each operation,
    # and return the minimum number of operations.
    return 1 + min(edit_distance_recursive(s1, s2, i, j - 1),  # Insert
                   edit_distance_recursive(s1, s2, i - 1, j),  # Remove
                   edit_distance_recursive(s1, s2, i - 1, j - 1))  # Replace


if __name__ == "__main__":
    s1 = input()
    s2 = input()
    print(edit_distance_dp(s1, s2, len(s1), len(s2)))

    # Driver code
    # str1 = "sunday"
    # str2 = "saturday"
    # print
    # editDistance(str1, str2, len(str1), len(str2))
