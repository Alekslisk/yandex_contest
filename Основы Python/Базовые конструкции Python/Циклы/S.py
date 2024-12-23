# Интересная задача: даешь интерактив)
def binary_game(num):
    left = 0
    right = num
    mid = (left + right) // 2
    while left <= right:
        print(mid)
        answer = input()
        if answer == 'Больше':
            left = mid + 1
        elif answer == 'Меньше':
            right = mid - 1
        else:
            break
        mid = (left + right) // 2


binary_game(1000)