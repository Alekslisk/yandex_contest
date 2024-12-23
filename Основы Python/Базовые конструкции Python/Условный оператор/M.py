def superNumber(numbers):
    for i in range(len(numbers[0])):
        if numbers[0][i] == numbers[1][i] == numbers[2][i]:
            return numbers[1][i]


numbers = [input() for _ in range(3)]

print(superNumber(numbers))