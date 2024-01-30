import sys

input = sys.stdin.readline

N = int(input())
D = [0, 1, 1, 2, 2, 1, 2, 1] + [0] * (N - 7 if N > 7 else 0)

for i in range(8, N + 1):
    D[i] = D[i - 1] + 1
    D[i] = min(D[i], D[i - 2] + 1)
    D[i] = min(D[i], D[i - 5] + 1)
    D[i] = min(D[i], D[i - 7] + 1)

print(D[N])
