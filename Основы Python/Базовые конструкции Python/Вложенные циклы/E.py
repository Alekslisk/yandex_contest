n = int(input())
cnt = 0

for i in range(n):
    flag_rabbit = False
    
    while True:
        say = input()

        if say == 'ВСЁ':
            break

        if say == 'зайка':
            flag_rabbit = True
    if flag_rabbit:
        cnt += 1
        
print(cnt)