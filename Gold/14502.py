import sys, copy
from collections import deque

input = sys.stdin.readline


def make_wall(n):
    if n == 3:
        bfs()
        return

    for y in range(N):
        for x in range(M):
            if AREA[y][x] == "0":
                AREA[y][x] = "1"
                make_wall(n + 1)
                AREA[y][x] = "0"


def bfs():
    global answer

    queue = deque()
    area = copy.deepcopy(AREA)

    for y in range(N):
        for x in range(M):
            if area[y][x] == "2":
                queue.append((y, x))

    while queue:
        y, x = queue.popleft()

        for dy, dx in DIR:
            Y, X = y + dy, x + dx
            if -1 < Y < N and -1 < X < M and area[Y][X] == "0":
                queue.append((Y, X))
                area[Y][X] = "2"

    cnt = 0
    for y in range(N):
        for x in range(M):
            if area[y][x] == "0":
                cnt += 1

    answer = max(answer, cnt)


N, M = map(int, input().split())
AREA = [input().strip().split() for _ in range(N)]
DIR = [(1, 0), (-1, 0), (0, 1), (0, -1)]
answer = 0

make_wall(0)
print(answer)
