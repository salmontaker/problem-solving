n, m = map(int, input().split())
b = [_ for _ in range(n + 1)]
for _ in range(m):
    i, j = map(int, input().split())
    for k in range((j - i + 1) // 2):
        temp = b[i + k]
        b[i + k] = b[j - k]
        b[j - k] = temp
print(" ".join(map(str, b[1:])))
