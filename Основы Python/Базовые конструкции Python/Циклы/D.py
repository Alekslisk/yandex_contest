def my_range(start, end, step=1):
    if start > end:
        step = -1
    while start != end:
        yield start
        start += step
    yield start


start = int(input())
end = int(input())
[print(i, end=' ') for i in my_range(start, end)]