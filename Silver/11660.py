import sys

input = sys.stdin.readline

N, M = map(int, input().split())
A = [[*map(int, input().split())] for _ in range(N)]
S = [[0] * (N + 1) for _ in range(N + 1)]

for y in range(1, N + 1):
    for x in range(1, N + 1):
        S[y][x] = A[y - 1][x - 1] + S[y - 1][x] + S[y][x - 1] - S[y - 1][x - 1]

for _ in range(M):
    y1, x1, y2, x2 = map(int, input().split())
    print(S[y2][x2] - S[y2][x1 - 1] - S[y1 - 1][x2] + S[y1 - 1][x1 - 1])
