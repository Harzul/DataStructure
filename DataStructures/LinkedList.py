from typing import Any


class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, value=None):
        self._head = Node(value) if value else None
        self._tail = self._head
        self._size = 0 if value is None else 1

    def __empty_head(self, value: Any) -> bool:
        if not self._head:
            self._head = Node(value)
            self._head.value = value
            self._tail = self._head
            self._size += 1
            return True
        return False

    def insert_back(self, value: Any) -> None:
        if self.__empty_head(value):
            return None
        tmp = self._head
        while tmp.next:
            tmp = tmp.next
        tmp.next = Node(value)
        self._tail = tmp.next
        self._size += 1
        return None

    def insert_front(self, value: Any) -> None:
        if self.__empty_head(value):
            return None
        tmp = Node(value)
        tmp.next = self._head
        self._head = tmp
        self._size += 1
        return None

    def insert(self, value: Any, index: int) -> None:
        if index > self._size - 1:
            print('Index is too big, adding new element to back')
            self.insert_back(value)
            return None
        if index <= 0:
            self.insert_front(value)
            return None
        t1 = self._head
        for _ in range(index - 1):
            t1 = t1.next
        t2 = t1.next
        t1.next = Node(value)
        t1.next.next = t2
        self._size += 1
        return None

    def delete(self, value: Any) -> None:
        if self._head.value == value:
            self._head = self._head.next
            self._size -= 1
            return None
        if not self._head:
            return None
        tmp = self._head
        while tmp.next:
            if tmp.next.value == value:
                break
            tmp = tmp.next
        else:
            print('No such element in list')
            return None
        if tmp.next.next is None:
            tmp.next = None
            self._tail = tmp
        else:
            tmp.next = tmp.next.next
        self._size -= 1
        return None

    def search(self, value: Any) -> bool:
        tmp = self._head
        while tmp:
            if tmp.value == value:
                return True
            tmp = tmp.next
        else:
            return False

    def at_index(self, index: int) -> Any:
        if index < 0 or index > self._size - 1:
            raise IndexError
        tmp = self._head
        for _ in range(index):
            tmp = tmp.next
        return tmp.value

    def copy(self):
        return self.__copy__()

    def deepcopy(self):
        return self.__deepcopy__()

    def __repr__(self):
        tmp = self._head
        result = ''
        while tmp:
            result += f'Value is: {tmp.value}\n'
            tmp = tmp.next
        return result

    def __copy__(self):
        return self

    def __deepcopy__(self):
        L = LinkedList()
        tmp = self._head
        while tmp:
            L.insert_back(tmp.value)
            tmp = tmp.next
        return L

    def __len__(self):
        return self._size

    def __contains__(self, value):
        return self.search(value)


def main():
    a = [1, 2, 3, 4, 5, 6]

    L = LinkedList(1)
    L.insert_back(2)
    L.insert_back(3)
    L.insert_back(4)
    L.insert_back(5)
    L.insert_back(6)
    L.insert(7, 2)
    L_dcopy = L.deepcopy()
    L.delete(6)
    print(L)
    print(L_dcopy)


if __name__ == '__main__':
    main()
