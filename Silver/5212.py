import sys

input = sys.stdin.readline


def check(y, x):
    cnt = 0
    for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        Y, X = y + dy, x + dx
        if Y < 0 or Y >= R or X < 0 or X >= C or A[Y][X] == ".":
            cnt += 1

    if cnt >= 3:
        B.append((y, x))


R, C = map(int, input().split())
A = [[*input().strip()] for _ in range(R)]
B = []

for y in range(R):
    for x in range(C):
        if A[y][x] == "X":
            check(y, x)

for y, x in B:
    A[y][x] = "."

min_y, min_x = R, C
max_y, max_x = 0, 0
for y in range(R):
    for x in range(C):
        if A[y][x] == "X":
            min_y, min_x = min(min_y, y), min(min_x, x)
            max_y, max_x = max(max_y, y), max(max_x, x)

for y in range(min_y, max_y + 1):
    print(*A[y][min_x : max_x + 1], sep="")
