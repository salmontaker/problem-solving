import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
A = [[*input().strip()] for _ in range(N)]
D = [[-1] * M for _ in range(N)]
Q = deque()

for y in range(N):
    for x in range(M):
        if A[y][x] == "1":
            Q.append((y, x))
            D[y][x] = 0

while Q:
    y, x = Q.popleft()
    for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        Y, X = y + dy, x + dx
        if -1 < Y < N and -1 < X < M and D[Y][X] == -1:
            Q.append((Y, X))
            D[Y][X] = D[y][x] + 1

for d in D:
    print(*d)
