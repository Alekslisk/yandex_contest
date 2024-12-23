from itertools import permutations


def divider(number):
    numbers_perm = []
    for i in permutations(number, 2):
        num = int(''.join(i))
        if num > 9:
            numbers_perm.append(num) 

    return f'{min(numbers_perm)} {max(numbers_perm)}'


print(divider(input()))