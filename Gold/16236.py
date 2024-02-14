import sys
from collections import deque

input = sys.stdin.readline


def find_fish(y, x):
    queue = deque([(y, x)])
    dist = [[-1] * N for _ in range(N)]
    dist[y][x] = 0

    fishes = []

    while queue:
        y, x = queue.popleft()
        for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            Y, X = y + dy, x + dx
            if Y < 0 or Y >= N or X < 0 or X >= N:
                continue
            if A[Y][X] > cur_size:
                continue
            if dist[Y][X] != -1:
                continue

            queue.append((Y, X))
            dist[Y][X] = dist[y][x] + 1

            if 0 < A[Y][X] < cur_size:
                fishes.append((dist[Y][X], Y, X))

    return sorted(fishes)[0] if fishes else (-1, -1, -1)


N = int(input())
A = [[*map(int, input().split())] for _ in range(N)]

cur_y, cur_x = -1, -1
cur_move = 0
cur_ate = 0
cur_size = 2

for y in range(N):
    for x in range(N):
        if A[y][x] == 9:
            cur_y, cur_x = y, x
            break

while True:
    dist, next_y, next_x = find_fish(cur_y, cur_x)
    if dist == -1:
        print(cur_move)
        break

    A[cur_y][cur_x] = 0
    A[next_y][next_x] = 9

    cur_y, cur_x = next_y, next_x
    cur_move += dist
    cur_ate += 1
    if cur_ate == cur_size:
        cur_ate = 0
        cur_size += 1
