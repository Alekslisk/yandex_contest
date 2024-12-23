def format_receipt(product, price, weight, money):
    total_price = price * weight
    change = money - total_price
    f_str = f'{weight}кг * {price}руб/кг'

    # Использовал мини выражения для форматирования
    # https://docs.python.org/3/library/string.html#formatspec
    receipt = (
        "================Чек================\n"
        f"Товар: {product:>28}\n"
        f"Цена: {f_str:>29}\n"
        f"Итого: {total_price:>25}руб\n"
        f"Внесено: {money:>23}руб\n"
        f"Сдача: {change:>25}руб\n"
        "==================================="
    )
    return receipt


product = input().strip()  
price = int(input().strip())  
weight = int(input().strip())  
money = int(input().strip())  

print(format_receipt(product, price, weight, money))
