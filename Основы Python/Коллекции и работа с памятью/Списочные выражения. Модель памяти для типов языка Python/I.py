# numbers = [3, 1, 2, 3, 2, 2, 1]
numbers = [1, 1, 3, 1, 10, 2, 4, 6, 7, 1, 2, 7]


print(' - '.join([str(i) for i in sorted({i for i in numbers})]))