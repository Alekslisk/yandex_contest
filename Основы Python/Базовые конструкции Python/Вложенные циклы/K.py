def is_primary(num):
    # if num == 1:
    #    return False 
    # if num == 2: 
    #    return True
    # for i in range(2, num):
    #     if num % i == 0:
    #         return False
    # return True    
    if num == 1: 
        return False
    if num == 2: 
        return True
    for i in range(2, round(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


n = int(input())
cnt = 0

for _ in range(n):
    num = int(input())
    if is_primary(num):
        cnt += 1
print(cnt)
