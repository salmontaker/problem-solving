import sys

sys.setrecursionlimit(100000)


def dfs(y, x, h):
    area[y][x] = 0
    for dy, dx in DIR:
        Y, X = y + dy, x + dx
        if -1 < Y < N and -1 < X < N and area[Y][X] != 0 and area[Y][X] > h:
            dfs(Y, X, h)


input = sys.stdin.readline
answer = 0

N = int(input())
AREA = [list(map(int, input().split())) for _ in range(N)]
DIR = [(1, 0), (-1, 0), (0, 1), (0, -1)]
HEIGHT = max(map(max, AREA))

for h in range(HEIGHT + 1):
    area = [data[:] for data in AREA]
    cnt = 0
    for y in range(N):
        for x in range(N):
            if area[y][x] != 0 and area[y][x] > h:
                dfs(y, x, h)
                cnt += 1

    if answer < cnt:
        answer = cnt

print(answer)
