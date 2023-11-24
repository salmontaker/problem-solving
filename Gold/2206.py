import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
B = [[*input().strip()] for _ in range(N)]
D = [[[-1] * M for _ in range(N)] for _ in range(2)]

Q = deque([(0, 0, 0)])
D[0][0][0] = D[1][0][0] = 1

while Q:
    broken, y, x = Q.popleft()
    if y == N - 1 and x == M - 1:
        print(D[broken][y][x])
        exit(0)
    for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        ny, nx = y + dy, x + dx
        if -1 < ny < N and -1 < nx < M:
            if B[ny][nx] == "0" and D[broken][ny][nx] == -1:
                Q.append((broken, ny, nx))
                D[broken][ny][nx] = D[broken][y][x] + 1
            if B[ny][nx] == "1" and D[1][ny][nx] == -1 and not broken:
                Q.append((1, ny, nx))
                D[1][ny][nx] = D[broken][y][x] + 1

print(-1)
