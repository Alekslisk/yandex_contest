n = int(input())
max_player = {'winner': [0, 'name']}

for _ in range(n):
    name = input()
    total = sum([int(i) for i in input()])

    if max_player['winner'][0] <= total:
        max_player['winner'] = [total, name]

print(max_player['winner'][1]) 