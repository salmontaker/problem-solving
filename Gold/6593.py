import sys
from collections import deque

input = sys.stdin.readline
delta = [(0, 1, 0), (0, 0, 1), (0, -1, 0), (0, 0, -1), (1, 0, 0), (-1, 0, 0)]  # z, y, x

while True:
    Z, Y, X = map(int, input().split())
    if Z == 0 and Y == 0 and X == 0:
        break

    B = [[[*input().strip()] for _ in range(Y + 1)][:Y] for _ in range(Z)]
    D = [[[-1] * X for _ in range(Y)] for _ in range(Z)]
    S, E = tuple(), tuple()

    for z in range(Z):
        for y in range(Y):
            for x in range(X):
                if B[z][y][x] == "S":
                    S = (z, y, x)
                    D[z][y][x] = 0
                elif B[z][y][x] == "E":
                    E = (z, y, x)

    Q = deque([S])
    while Q:
        z, y, x = Q.popleft()
        for dz, dy, dx in delta:
            nz, ny, nx = z + dz, y + dy, x + dx
            if -1 < nz < Z and -1 < ny < Y and -1 < nx < X and B[nz][ny][nx] != "#":
                if D[nz][ny][nx] == -1:
                    Q.append((nz, ny, nx))
                    D[nz][ny][nx] = D[z][y][x] + 1

    ans = D[E[0]][E[1]][E[2]]
    print(f"Escaped in {ans} minute(s)." if ans != -1 else "Trapped!")
