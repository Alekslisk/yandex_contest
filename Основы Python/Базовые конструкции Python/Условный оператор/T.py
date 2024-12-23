def rabbit_2(landscape):
    rabbit_lands = []

    for i in landscape:
        if i.find('зайка') != -1:
            rabbit_lands.append(i)
    
    result = sorted(rabbit_lands)[0]
    return result, len(result)


landscape = []
for _ in range(3):
    landscape.append(input())
answer = rabbit_2(landscape)
print(f'{answer[0]} {answer[1]}')