import sys
from collections import deque

input = sys.stdin.readline


def move(y, x):
    queue = deque([(y, x, 0)])
    V[y][x] = 1

    while queue:
        y, x, d = queue.popleft()
        Y, X = y + B[y][x] * D[d][0], x + B[y][x] * D[d][1]

        if -1 < Y < N and -1 < X < M:
            if V[Y][X] < 4:
                queue.append((Y, X, (d + 1) % 4))
                V[Y][X] += 1
        else:
            return 0

    return 1


N, M = map(int, input().split())
B = [[*map(int, input().split())] for _ in range(N)]
D = [(0, 1), (1, 0), (0, -1), (-1, 0)]

answer = []
for i in range(N):
    V = [[0] * M for _ in range(N)]
    if move(i, 0):
        answer.append(i + 1)

print(len(answer))
if answer:
    print(*answer)
