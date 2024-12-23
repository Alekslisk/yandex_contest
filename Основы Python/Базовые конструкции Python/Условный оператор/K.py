def isPretty(number):
    numbers = [int(i) for i in number]
    max_number = numbers[0]
    min_number = numbers[0]
    index_max = 0
    index_min = 0

    for i, j in enumerate(numbers):
        if max_number < j:
            max_number = j
            index_max = i

        if min_number > j:
            min_number = j
            index_min = i

    if max_number + min_number == numbers[{0, 1, 2}.difference({index_max, index_min}).pop()] * 2:
        return True
    return False


number = input()
if isPretty(number):
    print('YES')
else:
    print('NO')