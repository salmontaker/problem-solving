import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
A = [[*map(int, input().split())] for _ in range(N)]
V = [[0] * M for _ in range(N)]
D = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def bfs(y, x):
    Q = deque([(y, x)])
    V[y][x] = 1

    current = A[y][x]
    is_peak = 1

    while Q:
        y, x = Q.popleft()
        for dy, dx in D:
            Y, X = y + dy, x + dx
            if -1 < Y < N and -1 < X < M:
                if A[Y][X] == current and not V[Y][X]:
                    Q.append((Y, X))
                    V[Y][X] = 1
                if A[Y][X] > current:
                    is_peak = 0

    return is_peak


ans = 0
for y in range(N):
    for x in range(M):
        if not V[y][x]:
            ans += bfs(y, x)

print(ans)
