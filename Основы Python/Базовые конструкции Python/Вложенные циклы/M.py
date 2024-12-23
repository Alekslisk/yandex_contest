N = int(input())
M = int(input())

cnt = 1
len_f = len(str(N * M))

for i in range(N):
    cnt = i + 1
    for j in range(M):
        print(f'{cnt:{len_f}}', end=' ')
        cnt += N
    print()