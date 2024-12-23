cnt = 0
while True:
    say = input()
    if say == 'Приехали!':
        break
    if say.find('зайка') != -1:
        cnt += 1
print(cnt)