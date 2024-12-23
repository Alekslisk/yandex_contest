x = 5

y = x
print(id(y))
print(y)
print(id(x))

x += 1
print(id(y))
print(y)
print(id(x))