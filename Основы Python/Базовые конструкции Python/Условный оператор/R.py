def triangle_check(a, b, c):
    a, b, c = sorted([a, b, c])

    cos_y = (a ** 2 + b ** 2 - c ** 2) / 2 * a * b

    if cos_y == 0:
        return '100%'
    if cos_y > 0:
        return 'крайне мала'
    return 'велика'


a = int(input())
b = int(input())
c = int(input())

print(triangle_check(a, b, c))