import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
A = [[*map(int, input().split())] for _ in range(N)]
V = [[0] * M for _ in range(N)]

Q = deque()
for y in range(N):
    for x in range(M):
        if A[y][x] in [1, 2]:
            Q.append((y, x))
            V[y][x] = 1

while Q:
    y, x = Q.popleft()
    if A[y][x] == 3:
        continue

    for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        Y, X = y + dy, x + dx
        if -1 < Y < N and -1 < X < M:
            if A[Y][X] == 0:
                Q.append((Y, X))
                A[Y][X] = A[y][x]
                V[Y][X] = V[y][x] + 1
            elif A[Y][X] == 1:
                if A[y][x] == 2 and V[Y][X] == V[y][x] + 1:
                    A[Y][X] = 3
            elif A[Y][X] == 2:
                if A[y][x] == 1 and V[Y][X] == V[y][x] + 1:
                    A[Y][X] = 3

C = [0] * 3
for y in range(N):
    for x in range(M):
        if A[y][x] == 1:
            C[0] += 1
        elif A[y][x] == 2:
            C[1] += 1
        elif A[y][x] == 3:
            C[2] += 1

print(*C)
