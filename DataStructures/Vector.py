from typing import Union
from array import array


# Питонячий список по сути есть вектор, поэтому  некотороые методы реализованы в формате подражания С
class Vector(object):
    def __init__(self, type_=int, capacity=5):
        self._size = 0
        self._capacity = capacity
        self._type = type_
        self._vector = array('i' if type_ == int else 'f', [0] * capacity)

    def __extend(self) -> None:
        new_capacity = self._capacity * 2  # + 10
        tmp = Vector(self._type, new_capacity)
        for i, j in enumerate(self._vector):
            tmp._vector[i] = j
        self._capacity = new_capacity
        self._vector = tmp._vector
        del tmp
        return None

    def __compress(self):
        new_capacity = self._capacity // 2  # - 10
        tmp = Vector(self._type, new_capacity)
        for i, j in zip(range(self._size), self._vector):
            tmp._vector[i] = j
        self._capacity = new_capacity
        self._vector = tmp._vector
        del tmp
        return None

    def append(self, value: Union[int, float]) -> None:
        if self._size + 1 > self._capacity:
            self.__extend()
        self._vector[self._size] = value
        self._size += 1
        return None

    def insert(self, value: Union[int, float], index: int) -> None:
        if index > self._size - 1 or index < -self._size:
            raise IndexError
        if self._size + 1 > self._capacity:
            self.__extend()
        if index < 0:
            for i, j in enumerate(self._vector[self._size + index: self._size]):
                self._vector[self._size + index + 1 + i] = j
            self._vector[self._size + index] = value
        else:
            for i, j in enumerate(self._vector[index: self._size]):
                self._vector[i + index + 1] = j
            self._vector[index] = value
        self._size += 1
        return None

    def delete_last(self) -> None:
        if self._size == 0:
            raise IndexError
        if self._size - 1 < self._capacity * 0.3:
            self.__compress()
        self._vector[self._size - 1] = 0
        self._size -= 1
        return None

    def delete(self, index: int) -> None:
        if index > self._size - 1 or index < -self._size:
            raise IndexError
        if self._size - 1 < self._capacity * 0.3:
            self.__compress()
        if index < 1:
            self._vector[self._size + index] = 0
            for i, j in enumerate(self._vector[self._size + index + 1: self._size]):
                self._vector[i + index + self._size] = j
        else:
            self._vector[index] = 0
            for i, j in enumerate(self._vector[index + 1: self._size]):
                self._vector[i + index] = j
        self._vector[self._size - 1] = 0
        self._size -= 1
        return None

    def clear(self) -> None:
        for i in range(self._size):
            self._vector[i] = 0
        return None

    def copy(self):
        return self.__copy__()

    def deepcopy(self):
        return self.__deepcopy__()

    def __repr__(self):
        result = '['
        for i in range(self._size):
            if i == self._size - 1:
                result += f'{self._vector[i]}'
                break
            result += f'{self._vector[i]}, '
        result += ']'
        return result

    def __copy__(self):
        return self

    def __deepcopy__(self):
        V = Vector(type_=self._type, capacity=self._capacity)
        for _, j in zip(range(self._size), self._vector):
            V.append(j)
        return V

    def __len__(self):
        return self._size

    def __getitem__(self, index: int) -> Union[int, float]:
        if index > self._size - 1 or index < -self._size:
            raise IndexError
        if index < 1:
            return self._vector[self._size + index]
        else:
            return self._vector[index]


def main():
    V = Vector(int)
    V.append(1)
    V.append(2)
    V.append(3)
    V.append(4)
    V.append(5)
    V.append(6)
    print(V)
    V.delete(-1)
    V.delete(-1)
    V.delete(-1)
    print(V)


if __name__ == '__main__':
    main()
