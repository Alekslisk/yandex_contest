total = 0
while True:
    price = float(input())
    if price == 0:
        break
    total += (price * 0.9 if price >= 500 else price)
print(total)   