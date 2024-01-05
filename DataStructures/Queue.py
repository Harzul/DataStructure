from typing import Any


class QueueCapacityError(Exception):
    def __str__(self):
        return 'No empty space in queue'


class EmptyQueueError(IndexError):
    def __str__(self):
        return 'Queue is empty'


class Queue(object):
    def __init__(self):
        self._capacity = 255
        self._size = 0
        self._queue = list()

    def push(self, value: Any) -> None:
        if self._size == self._capacity:
            raise QueueCapacityError
        self._queue.append(value)
        self._size += 1

    def pop(self) -> Any:
        if self._size == 0:
            raise EmptyQueueError
        self._size -= 1
        return self._queue.pop(0)

    def empty(self) -> bool:
        return self._size == 0


def main():
    Q = Queue()
    try:
        Q.pop()
    except Exception as e:
        print(e)

    Q.push(1)
    Q.push(2)
    Q.push(3)
    Q.push(4)
    Q.push(5)
    Q.push(6)

    for i in range(1, 7):
        print(Q.pop())
    try:
        Q.pop()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
