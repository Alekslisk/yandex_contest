N = int(input())
M = int(input())

cnt = 1
len_f = len(str(N * M))

for i in range(N):
    for j in range(M):
        print(f'{cnt:{len_f}}', end=' ')
        cnt += 1
    print()