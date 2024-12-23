import math


def math_check(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                return "Infinite solutions"
            return "No solution"
        return f"{-c / b:.2f}"
    else:
        D = b**2 - 4 * a * c
        if D > 0:
            x1 = (-b + math.sqrt(D)) / (2 * a)
            x2 = (-b - math.sqrt(D)) / (2 * a)
            if x1 > x2:
                return f"{x2:.2f} {x1:.2f}"
            return f"{x1:.2f} {x2:.2f}"
        elif D == 0:
            x = -b / (2 * a)
            return f"{x:.2f}"
        else:
            return "No solution"
        

a = float(input())

b = float(input())

c = float(input())

print(math_check(a, b, c))