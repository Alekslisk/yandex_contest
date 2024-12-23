def is_palindrom(word):
    return word == word[::-1]


if is_palindrom(input()):
    print('YES')
else:
    print('NO')