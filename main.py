from Sorting.slow import *


def main():
    array = [i for i in range(100, -1, -1)]
    a = insertion_sort(array)
    print(a)


if __name__ == '__main__':
    main()
