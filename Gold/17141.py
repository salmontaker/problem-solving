import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline
INF = sys.maxsize

N, M = map(int, input().split())
A = [[*map(int, input().split())] for _ in range(N)]
EMPTY = []
VIRUS = []

for y in range(N):
    for x in range(N):
        if A[y][x] == 0:
            EMPTY.append((y, x))
        elif A[y][x] == 2:
            VIRUS.append((y, x))

answer = INF

for virus in combinations(VIRUS, M):
    Q = deque()
    D = [[-1] * N for _ in range(N)]
    for y, x in virus:
        Q.append((y, x))
        D[y][x] = 0

    remain = len(EMPTY) + len(VIRUS) - M

    while Q:
        y, x = Q.popleft()
        for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            Y, X = y + dy, x + dx
            if -1 < Y < N and -1 < X < N and A[Y][X] != 1 and D[Y][X] == -1:
                Q.append((Y, X))
                D[Y][X] = D[y][x] + 1
                remain -= 1

    if remain == 0:
        answer = min(answer, D[y][x])

print(answer if answer != INF else -1)
