from itertools import count

start, end, step = map(float, input().split())

for i in count(start, step):
    if i >= end:
        break
    print(round(i, 2))
    