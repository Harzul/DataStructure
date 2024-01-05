from typing import Any


class StackCapacityError(Exception):
    def __str__(self):
        return 'No empty space in stack'


class EmptyStackError(IndexError):
    def __str__(self):
        return 'Stack is empty'


class Stack(object):
    def __init__(self):
        self._capacity = 255
        self._size = 0
        self._stack = list()

    def push(self, value: Any) -> None:
        if self._size == self._capacity:
            raise StackCapacityError
        self._stack.append(value)
        self._size += 1

    def pop(self) -> Any:
        if self._size == 0:
            raise EmptyStackError
        self._size -= 1
        return self._stack.pop(-1)

    def empty(self) -> bool:
        return self._size == 0


def main():
    S = Stack()
    try:
        S.pop()
    except Exception as e:
        print(e)

    S.push(1)
    S.push(2)
    S.push(3)
    S.push(4)
    S.push(5)
    S.push(6)

    for i in range(1, 7):
        print(S.pop())
    try:
        S.pop()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
