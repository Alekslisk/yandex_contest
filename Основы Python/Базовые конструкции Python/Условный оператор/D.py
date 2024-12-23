time_p = 43872 / int(input())
time_v = 43872 / int(input())
time_t = 43872 / int(input())

if time_p <= time_v and time_p <= time_t:
    if time_v <= time_t:
        print("1. Петя")
        print("2. Вася")
        print("3. Толя")
    else:
        print("1. Петя")
        print("2. Толя")
        print("3. Вася")
elif time_v <= time_p and time_v <= time_t:
    if time_p <= time_t:
        print("1. Вася")
        print("2. Петя")
        print("3. Толя")
    else:
        print("1. Вася")
        print("2. Толя")
        print("3. Петя")
else:
    if time_p <= time_v:
        print("1. Толя")
        print("2. Петя")
        print("3. Вася")
    else:
        print("1. Толя")
        print("2. Вася")
        print("3. Петя")