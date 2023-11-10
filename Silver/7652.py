import sys
from collections import deque

input = sys.stdin.readline


def bfs(y, x):
    queue = deque([(y, x)])

    while queue:
        y, x = queue.popleft()
        if y == a and x == b:
            break
        for dy, dx in D:
            Y, X = y + dy, x + dx
            if -1 < Y < N and -1 < X < N and not board[Y][X]:
                queue.append((Y, X))
                board[Y][X] = board[y][x] + 1


D = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

for _ in range(int(input())):
    N = int(input())
    board = [[0] * N for _ in range(N)]
    y, x = map(int, input().split())
    a, b = map(int, input().split())

    bfs(y, x)
    print(board[a][b])
