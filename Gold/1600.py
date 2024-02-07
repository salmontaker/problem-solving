import sys
from collections import deque

input = sys.stdin.readline

K = int(input())
W, H = map(int, input().split())
A = [[*map(int, input().split())] for _ in range(H)]
D = [[[-1] * (K + 1) for _ in range(W)] for _ in range(H)]

DELTA1 = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
DELTA2 = [(-1, 0), (0, 1), (1, 0), (0, -1)]

Q = deque([(0, 0, 0)])
D[0][0] = [0] * (K + 1)

while Q:
    y, x, cnt = Q.popleft()

    if y == H - 1 and x == W - 1:
        print(D[y][x][cnt])
        exit()

    if cnt < K:
        for dy, dx in DELTA1:
            Y, X = y + dy, x + dx
            if -1 < Y < H and -1 < X < W:
                if A[Y][X] == 0 and D[Y][X][cnt + 1] == -1:
                    Q.append((Y, X, cnt + 1))
                    D[Y][X][cnt + 1] = D[y][x][cnt] + 1

    for dy, dx in DELTA2:
        Y, X = y + dy, x + dx
        if -1 < Y < H and -1 < X < W:
            if A[Y][X] == 0 and D[Y][X][cnt] == -1:
                Q.append((Y, X, cnt))
                D[Y][X][cnt] = D[y][x][cnt] + 1

print(-1)
