def snake_matrix(n, m):
    snake_matrix = [[0] * m for _ in range(n)]
    
    left, right = 0, m - 1
    cnt = 1

    for i in range(n):
        if (i + 1) % 2 != 0:
            for j in range(left, right + 1):
                snake_matrix[i][j] = cnt 
                cnt += 1
        else:
            for j in range(right, left - 1, -1):
                snake_matrix[i][j] = cnt 
                cnt += 1

    return snake_matrix


n = int(input())
m = int(input())
len_f = len(str(n * m))

for i in snake_matrix(n, m):
    for j in i:
        print(f'{j:{len_f}}', end=' ')
    print()

