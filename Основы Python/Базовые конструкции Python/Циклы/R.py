n = int(input())

factors = []
divisor = 2

while n > 1:
    while n % divisor == 0:
        factors.append(divisor)
        n //= divisor
    divisor += 1
    
    if divisor * divisor > n and n > 1:
        factors.append(n)
        break

print(' * '.join(map(str, factors)))



