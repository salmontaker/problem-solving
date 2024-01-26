import sys
from collections import deque

input = sys.stdin.readline

N, M, A, B, K = map(int, input().split())
WALL = [[0] * M for _ in range(N)]
DIST = [[-1] * M for _ in range(N)]

for _ in range(K):
    y, x = map(int, input().split())
    WALL[y - 1][x - 1] = 1

y1, x1 = map(lambda n: int(n) - 1, input().split())
y2, x2 = map(lambda n: int(n) - 1, input().split())


def can_move(y, x):
    if not (-1 < y and y + A - 1 < N and -1 < x and x + B - 1 < M):
        return False

    for Y in range(y, y + A):
        for X in range(x, x + B):
            if WALL[Y][X]:
                return False

    return True


Q = deque([(y1, x1)])
DIST[y1][x1] = 0

while Q:
    y, x = Q.popleft()
    if y == y2 and x == x2:
        print(DIST[y][x])
        exit()

    for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        Y, X = y + dy, x + dx
        if can_move(Y, X) and DIST[Y][X] == -1:
            Q.append((Y, X))
            DIST[Y][X] = DIST[y][x] + 1

print(-1)
