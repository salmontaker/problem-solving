import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
A = [[*map(int, input().split())] for _ in range(N)]
EMPTY = []
VIRUS = []

for y in range(N):
    for x in range(M):
        if A[y][x] == 0:
            EMPTY.append((y, x))
        elif A[y][x] == 2:
            VIRUS.append((y, x))

answer = 0

for walls in combinations(EMPTY, 3):
    Q = deque()
    for y, x in VIRUS:
        Q.append((y, x))

    R = [row[:] for row in A]
    for y, x in walls:
        R[y][x] = 1

    safe = len(EMPTY) - 3

    while Q:
        y, x = Q.popleft()
        for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            Y, X = y + dy, x + dx
            if -1 < Y < N and -1 < X < M and R[Y][X] == 0:
                Q.append((Y, X))
                R[Y][X] = 2
                safe -= 1

    answer = max(answer, safe)

print(answer)
