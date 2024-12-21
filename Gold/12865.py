import sys

input = sys.stdin.readline

N, K = map(int, input().split())
ITEMS = [[0, 0]] + [[*map(int, input().split())] for _ in range(N)]
DP = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for w in range(1, K + 1):
        weight, value = ITEMS[i]
        if weight > w:
            DP[i][w] = DP[i - 1][w]
        else:
            DP[i][w] = max(DP[i - 1][w], DP[i - 1][w - weight] + value)

print(DP[N][K])
