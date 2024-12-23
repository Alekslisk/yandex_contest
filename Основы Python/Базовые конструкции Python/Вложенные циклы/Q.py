def is_palindrom(num):
    num = str(num)

    return num == num[::-1]


n = int(input())
cnt = 0
for _ in range(n):
    num = int(input())
    if is_palindrom(num):
        cnt += 1

print(cnt)