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
            if -1 < Y < N and -1 < X < N and board[Y][X] == "." and not visited[Y][X]:
                queue.append((Y, X))
                visited[Y][X] = 1


N = int(input())
board = [[*input().strip()] for _ in range(N)]
visited = [[0] * N for _ in range(N)]
delta = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 1)]

for y in range(N):
    for x in range(N):
        if board[y][x] == "F":
            bfs(y, x)
            break

print(sum(map(sum, visited)) - 1)
