def snake_matrix(n, m):
    snake_matrix = [[0] * m for _ in range(n)]
    
    top, bottom = 0, n - 1
    cnt = 1

    for i in range(m):
        if (i + 1) % 2 != 0:
            for j in range(top, bottom + 1):
                snake_matrix[j][i] = cnt 
                cnt += 1
        else:
            for j in range(bottom, top - 1, -1):
                snake_matrix[j][i] = cnt 
                cnt += 1

    return snake_matrix


n = int(input())
m = int(input())
len_f = len(str(n * m))

for i in snake_matrix(n, m):
    for j in i:
        print(f'{j:{len_f}}', end=' ')
    print()

