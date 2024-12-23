def isAllowed(numbers):
    for i in range(len(numbers)):
        current = numbers[i]
        other_sum = sum(numbers) - current

        if other_sum <= current:
            return False
    return True


numbers = [int(input()) for _ in range(3)]

if isAllowed(numbers):
    print('YES')
else:
    print('NO')