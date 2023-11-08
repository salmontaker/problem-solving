import sys

input = sys.stdin.readline


def spread():
    new_area = [[0] * C for _ in range(R)]

    for y in range(R):
        for x in range(C):
            if area[y][x] > 0:
                amount = area[y][x] // 5
                cnt = 0
                for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    ny, nx = y + dy, x + dx
                    if -1 < ny < R and -1 < nx < C and area[ny][nx] != -1:
                        new_area[ny][nx] += amount
                        cnt += 1
                new_area[y][x] += area[y][x] - amount * cnt
            elif area[y][x] == -1:
                new_area[y][x] = -1

    return new_area


def rotate():
    up_pos, down_pos = cleaner

    prev = 0
    for x in range(1, C):
        area[up_pos][x], prev = prev, area[up_pos][x]
    for y in reversed(range(0, up_pos)):
        area[y][C - 1], prev = prev, area[y][C - 1]
    for x in reversed(range(0, C - 1)):
        area[0][x], prev = prev, area[0][x]
    for y in range(1, up_pos):
        area[y][0], prev = prev, area[y][0]

    prev = 0
    for x in range(1, C):
        area[down_pos][x], prev = prev, area[down_pos][x]
    for y in range(down_pos + 1, R):
        area[y][C - 1], prev = prev, area[y][C - 1]
    for x in reversed(range(0, C - 1)):
        area[R - 1][x], prev = prev, area[R - 1][x]
    for y in reversed(range(down_pos + 1, R - 1)):
        area[y][0], prev = prev, area[y][0]


R, C, T = map(int, input().split())
area = [[*map(int, input().split())] for _ in range(R)]
cleaner = tuple()

for y in range(R):
    if area[y][0] == -1:
        cleaner = (y, y + 1)
        break

for _ in range(T):
    area = spread()
    rotate()

print(sum(map(sum, area)) + 2)
