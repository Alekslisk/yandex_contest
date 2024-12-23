def maximazePower(numbers):
    max_number = max(numbers)
    min_number = min(numbers)
    numbers.remove(max_number)
    numbers.remove(min_number)

    return f'{max_number}{sum(numbers) % 10}{min_number}'


numbers = list(map(int, ''.join([input() for _ in range(2)])))

print(maximazePower(numbers))
