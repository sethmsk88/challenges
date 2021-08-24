# python3
import sys


class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.__max_list = [0]

    def Push(self, a):
        self.__stack.append(a)
        if a >= self.__max_list[-1]:
            self.__max_list.append(a)

    def Pop(self):
        assert (len(self.__stack))
        num = self.__stack.pop()
        if num == self.__max_list[-1]:
            self.__max_list.pop()

    def Max(self):
        assert (len(self.__stack))
        return self.__max_list[-1]
        # return max(self.__stack)


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert (0)
