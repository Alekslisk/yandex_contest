n = int(input())
total_sum = 0

for i in range(n):
    num = input()
    for j in num:
        total_sum += int(j)

print(total_sum)