n = int(input())
max_num = ''

for _ in range(n):
    num = max([(i) for i in input()])

    max_num += num

print(max_num) 