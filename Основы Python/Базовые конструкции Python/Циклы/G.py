def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return abs(a * b) / gcd(a, b)

a = int(input())
b = int(input())

print(round(lcm(a, b)))