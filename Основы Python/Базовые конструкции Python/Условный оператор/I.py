def first_to_go(names):
    first = names[0]

    for i in names:
        if i < first:
            first = i
    
    return first


names = [input() for i in range(3)]

print(first_to_go(names))
    