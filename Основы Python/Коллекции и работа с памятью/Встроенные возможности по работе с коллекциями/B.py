group1 = input()
group2 = input()

[print(f'{i} - {j}') for i, j in zip(group1.split(', '), group2.split(', '))]