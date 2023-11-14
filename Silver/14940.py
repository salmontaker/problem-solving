import sys
from collections import deque

input = sys.stdin.readline


def bfs(y, x):
    queue = deque([(y, x)])
    V[y][x] = 0

    while queue:
        y, x = queue.popleft()
        for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            Y, X = y + dy, x + dx
            if -1 < Y < N and -1 < X < M:
                if A[Y][X] == 0:
                    V[Y][X] = 0
                elif A[Y][X] == 1 and V[Y][X] == -1:
                    queue.append((Y, X))
                    V[Y][X] = V[y][x] + 1


N, M = map(int, input().split())
A, V = [], []

for _ in range(N):
    line = [*map(int, input().split())]
    A.append(line)
    V.append([*map(lambda x: -x, line)])

for y in range(N):
    for x in range(M):
        if A[y][x] == 2:
            bfs(y, x)
            break

for v in V:
    print(*v)
