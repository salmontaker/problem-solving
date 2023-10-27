import sys
from collections import deque

input = sys.stdin.readline
dir = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (1, 1), (-1, 1), (-1, -1)]


def bfs(y, x):
    queue = deque([(y, x)])
    while queue:
        y, x = queue.popleft()
        for dy, dx in dir:
            Y, X = y + dy, x + dx
            if -1 < Y < h and -1 < X < w and m[Y][X] != 0:
                queue.append((Y, X))
                m[Y][X] = 0


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    m = [list(map(int, input().split())) for _ in range(h)]
    c = 0

    for y in range(h):
        for x in range(w):
            if m[y][x] != 0:
                bfs(y, x)
                c += 1

    print(c)
