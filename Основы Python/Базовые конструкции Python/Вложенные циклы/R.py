def x_mas_matrix(n):
    num = 1
    current_level = 1  
    x_matrix = []

    while n > 0:
        count = min(current_level, n)

        level = " ".join(str(num + i) for i in range(count))

        x_matrix.append(level)

        n -= count
        num += count
        current_level += 1
    return x_matrix


n = int(input())
result = x_mas_matrix(n)
width = len(result[len(result) - 1].strip())

for i in result:
    print(f'{i:^{width}}')