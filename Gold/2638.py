import sys
from collections import deque

input = sys.stdin.readline


def check(y, x):
    cnt = 0
    for dy, dx in delta:
        Y, X = y + dy, x + dx
        if not cheeze[Y][X] and visited[Y][X] == hour:
            cnt += 1

    return cnt >= 2


def bfs(y, x):
    queue = deque([(y, x)])
    visited[y][x] = hour

    while queue:
        y, x = queue.popleft()
        for dy, dx in delta:
            Y, X = y + dy, x + dx
            if -1 < Y < col and -1 < X < row and visited[Y][X] != hour:
                if cheeze[Y][X]:
                    melt.append((Y, X))
                else:
                    queue.append((Y, X))
                    visited[Y][X] = hour

    while melt:
        y, x = melt.pop()
        if check(y, x):
            cheeze[y][x] = 0


col, row = map(int, input().split())
cheeze = [list(map(int, input().split())) for _ in range(col)]
visited = [[-1] * row for _ in range(col)]
delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
melt = []
hour = 0

while True:
    if sum(map(sum, cheeze)) == 0:
        print(hour)
        break

    bfs(0, 0)
    hour += 1
