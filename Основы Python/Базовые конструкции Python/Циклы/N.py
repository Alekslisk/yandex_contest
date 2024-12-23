def is_primal(num):
    if num == 1:
        return False
    if num == 2:
        return True
    for i in range(2, round(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


if is_primal(int(input())):
    print('YES')
else:
    print('NO')