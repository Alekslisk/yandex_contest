n = int(input())
cnt = 1

for i in range(n):
    for j in range(n):
        if i >= j:
            print(cnt, end=' ')
            cnt += 1
        if cnt > n:
            break
    if cnt > n:
        break
    print()