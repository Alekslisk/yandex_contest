def validate_hash_block(N, blocks):
    h_prev = 0

    for i in range(N):
        b_n = blocks[i]
        h_n = b_n % 256
        r_n = (b_n // 256) % 256
        m_n = b_n // (256 * 256)

        expected_h_n = (37 * (m_n + r_n + h_prev)) % 256
        if h_n >= 100 or h_n != expected_h_n:
            return i
        h_prev = h_n
    return -1


n = int(input())

blocks = [int(input()) for _ in range(n)]

print(validate_hash_block(n, blocks))