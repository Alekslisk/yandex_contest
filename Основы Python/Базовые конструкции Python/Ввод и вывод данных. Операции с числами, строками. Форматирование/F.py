name = input()

price = int(input())

weight = int(input())

cli_money = int(input())

print(f"""Чек
{name} - {weight}кг - {price}руб/кг
Итого: {price * weight}руб
Внесено: {cli_money}руб
Сдача: {cli_money - price * weight}руб""")