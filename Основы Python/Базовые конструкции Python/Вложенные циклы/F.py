def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


n = int(input())
my_gcd = int(input())

for _ in range(n - 1):
    num = int(input())
    my_gcd = gcd(num, my_gcd)
print(my_gcd)