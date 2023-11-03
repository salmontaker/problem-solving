import sys
from collections import deque

input = sys.stdin.readline


def bfs(y, x):
    queue = deque([(y, x)])
    visited[y][x] = 1

    while queue:
        y, x = queue.popleft()
        cnt = 0

        for dy, dx in delta:
            Y, X = y + dy, x + dx
            if -1 < Y < N and -1 < X < M and not visited[Y][X]:
                if area[Y][X] != 0:
                    queue.append((Y, X))
                    visited[Y][X] = 1
                else:
                    cnt += 1

        if cnt:
            melt.append((y, x, max(area[y][x] - cnt, 0)))


N, M = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(N)]
delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
melt = deque()
year = 0


while True:
    visited = [[0] * M for _ in range(N)]
    cnt = 0

    for y in range(N):
        for x in range(M):
            if area[y][x] != 0 and not visited[y][x]:
                bfs(y, x)
                cnt += 1

    if cnt >= 2:
        print(year)
        break

    elif cnt == 0:
        print(0)
        break

    while melt:
        y, x, n = melt.popleft()
        area[y][x] = n

    year += 1
