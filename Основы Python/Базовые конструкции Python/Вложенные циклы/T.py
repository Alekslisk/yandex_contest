def convert_base(num, base):
    digits = []

    while num > 0:
        digits.append(num % base)
        num //= base
    
    return digits[::-1]


def find_best_sum(num):
    max_base = 0
    max_sum = 0

    for i in range(2, 11):
        base_sum = sum(convert_base(num, i))

        if base_sum > max_sum:
            max_base = i
            max_sum = base_sum

    return max_base


n = int(input())
print(find_best_sum(n))