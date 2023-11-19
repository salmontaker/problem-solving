import sys
from collections import deque

input = sys.stdin.readline


def bfs(y, x, color_a, color_b):
    queue = deque([(y, x)])
    NEW_A[y][x] = color_b

    while queue:
        y, x = queue.popleft()
        for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            Y, X = y + dy, x + dx
            if -1 < Y < N and -1 < X < M:
                if A[Y][X] == color_a and NEW_A[Y][X] == "*":
                    queue.append((Y, X))
                    NEW_A[Y][X] = color_b


N, M = map(int, input().split())
A = [[*input().strip()] for _ in range(N)]
B = [[*input().strip()] for _ in range(N)]

NEW_A = [["*"] * M for _ in range(N)]

for y in range(N):
    for x in range(M):
        if NEW_A[y][x] == "*":
            bfs(y, x, A[y][x], B[y][x])

print("YES" if NEW_A == B else "NO")
