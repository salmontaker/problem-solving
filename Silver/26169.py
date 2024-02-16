import sys

input = sys.stdin.readline


def dfs(depth, cnt, y, x):
    if cnt >= 2:
        print(1)
        exit()
    if depth == 3:
        return

    for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        Y, X = y + dy, x + dx
        prev = A[y][x]

        if -1 < Y < 5 and -1 < X < 5 and A[Y][X] != -1:
            A[y][x] = -1
            dfs(depth + 1, cnt + A[Y][X], Y, X)
            A[y][x] = prev


A = [[*map(int, input().split())] for _ in range(5)]
R, C = map(int, input().split())
dfs(0, 0, R, C)
print(0)
