import sys
from collections import deque

input = sys.stdin.readline


def effect(n, r, c):
    B[r][c] = n

    for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        R, C = r + dr, c + dc
        if -1 < R < N and -1 < C < N and B[R][C] == 0:
            B[R][C] = n
            T.append((n, R, C))


N, K = map(int, input().split())
B = [[*map(int, input().split())] for _ in range(N)]
S, Y, X = map(int, input().split())
V = deque()
T = deque()

for r in range(N):
    for c in range(N):
        if B[r][c] != 0:
            V.append((B[r][c], r, c))

V = deque(sorted(V))

while S:
    while V:
        n, y, x = V.popleft()
        effect(n, y, x)

    V = T
    S -= 1

print(B[Y - 1][X - 1])
