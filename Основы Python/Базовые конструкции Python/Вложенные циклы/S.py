n = int(input())

width = len(str(n - n // 2))

for i in range(n):
    for j in range(n):
        value = min(i, j, n - i - 1, n - j - 1) + 1
        print(f'{value:{width}}', end=' ')
    print()
