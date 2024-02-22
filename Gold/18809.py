import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline
INF = sys.maxsize


def dfs(pos, depth, green, red):
    global answer

    if depth == G + R:
        answer = max(answer, bfs())
        return

    if green < G:
        POS_G.append(pos[depth])
        dfs(pos, depth + 1, green + 1, red)
        POS_G.pop()
    if red < R:
        POS_R.append(pos[depth])
        dfs(pos, depth + 1, green, red + 1)
        POS_R.pop()


def bfs():
    Q = deque()
    V = [[0] * M for _ in range(N)]
    cnt = 0

    for y, x in POS_G:
        Q.append((y, x))
        V[y][x] = -1
    for y, x in POS_R:
        Q.append((y, x))
        V[y][x] = 1

    while Q:
        y, x = Q.popleft()
        if V[y][x] == INF:
            continue

        for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            Y, X = y + dy, x + dx
            if -1 < Y < N and -1 < X < M and A[Y][X] != 0:
                if not V[Y][X]:
                    V[Y][X] = V[y][x] + (-1 if V[y][x] < 0 else 1)
                    Q.append((Y, X))
                elif V[Y][X] + V[y][x] + 1 == 0:
                    V[Y][X] = INF
                    cnt += 1

    return cnt


N, M, G, R = map(int, input().split())
A = [[*map(int, input().split())] for _ in range(N)]
POS = []
POS_G = []
POS_R = []

for y in range(N):
    for x in range(M):
        if A[y][x] == 2:
            POS.append((y, x))

answer = 0

for pos in combinations(POS, G + R):
    dfs(pos, 0, 0, 0)

print(answer)
