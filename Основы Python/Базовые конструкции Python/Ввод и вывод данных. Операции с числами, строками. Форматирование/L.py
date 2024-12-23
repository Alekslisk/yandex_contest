num1 = input()
num2 = input()

max_len = max(len(num1), len(num2))
num1 = num1.zfill(max_len)
num2 = num2.zfill(max_len)

result = ""
for digit1, digit2 in zip(num1, num2):
    result += str((int(digit1) + int(digit2)) % 10)  

print(result)
