n = int(input())
k = int(input())

for i in range(1, n + 1): 
    for j in range(1, n + 1):
        print(f'{i * j:^{k}}', end='')
        if j < n:
            print('|', end='')
    if i < n:
        print('\n', "-" * (k * n + n - 1), sep='')