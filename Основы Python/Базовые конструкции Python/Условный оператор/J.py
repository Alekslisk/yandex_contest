def encoder(number):
    first = int(number[2]) + int(number[1])
    second = int(number[0]) + int(number[1])
    if first > second:
        return str(first) + str(second)
    return str(second) + str(first) 


print(encoder(input()))