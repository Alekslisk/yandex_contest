orange = int(input())

combinations = []

for a in range(1, orange - 1):
    for b in range(1, orange - 1):
        c = orange - a - b
        if c >= 1:
            combinations.append([a, b, c])

print('А Б В')
for i in combinations:
    print(' '.join(list(map(str, i))))

    