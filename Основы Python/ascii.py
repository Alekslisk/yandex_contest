integer_value_start = 64
file_path = input()

n = int(input())
for i in range(1, n + 1):
    with open(f'{file_path}/{chr(integer_value_start + i)}.py', 'w') as f:
        f.write('')

