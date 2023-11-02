import sys
from collections import deque

input = sys.stdin.readline


def bfs(y, x):
    queue = deque([(y, x)])
    visited[y][x] = 1

    while queue:
        y, x = queue.popleft()

        for dy, dx in delta:
            Y, X = y + dy, x + dx
            if -1 < Y < N and -1 < X < M and area[Y][X] == 1 and not visited[Y][X]:
                queue.append((Y, X))
                visited[Y][X] = 1
                area[Y][X] = area[y][x] + 1


N, M = map(int, input().split())
area = [list(map(int, list(input().strip()))) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]

bfs(0, 0)
print(area[N - 1][M - 1])
