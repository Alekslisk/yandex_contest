N = int(input())

M = int(input())

K1 = int(input())

K2 = int(input())

# M * N = K1 * N1 + K2 * N2
# N = N1 + N2
# N1 = N - N2
# M = K1 * N + N2(K2 - K1)
# N2 = (M * N - K1 * N)/(K2 - K1)

N2 = int((M * N - K1 * N) / (K2 - K1))

print(f"{N - N2} {N2}")