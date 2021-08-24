# python3

def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    # Base case, there are less than 2 brackets
    if len(text) < 2:
        return 1    # index of first bracket

    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            index_bracket_tuple = (i, next)
            opening_brackets_stack.append(index_bracket_tuple)

        elif next in ")]}":
            # if no opening_brackets, then failure
            if len(opening_brackets_stack) == 0:
                return i+1

            # Process closing bracket, write your code here
            b_i, bracket = opening_brackets_stack.pop()

            # if the bracket at the top of the stack is the closing bracket that matches next
            if not are_matching(bracket, next):
                return i+1

    if len(opening_brackets_stack) > 0:
        mismatch_i, bracket = opening_brackets_stack[0]
        return mismatch_i+1

    return "Success"


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)


if __name__ == "__main__":
    main()
