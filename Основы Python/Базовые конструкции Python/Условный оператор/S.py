def is_in_dangerous_zone(x, y):
    # правый верх| нахождение в круге
    if x > 0 and y > 0:
        return x**2 + y**2 <= 25
    # Левый верх| нахождение в квадрате (4, -5) или в прямоугольном треугольнике 
    if x < 0 and y > 0:
        def first_cathet(x, y):
            return 5 * x - 3 * y + 35 <= 0

        def second_cathet(x, y):
            return x >= 6

        def hypotenuse(x, y):
            return (0 - (-5)) * (x - 6) - (8 - 6) * (y - (-5)) <= 0

        return (0 <= x <= -4 and 0 <= y <= 5) and (first_cathet(x, y) and second_cathet(x, y) and hypotenuse(x, y))
    # нижняя часть| нахождение внутри параболы
    return y >= (0.25 * x**2 + 0.5 * x - 35 / 4)


def is_in_safe_zone(x, y):
    return x**2 + y**2 <= 100  


def check_safety(x, y):
    if is_in_dangerous_zone(x, y):
        return "Опасность! Покиньте зону как можно скорее!"
    elif is_in_safe_zone(x, y):
        return "Зона безопасна. Продолжайте работу."
    return "Вы вышли в море и рискуете быть съеденным акулой!"


x = float(input())
y = float(input())

print(check_safety(x, y))